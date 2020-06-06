# import necessary libraries
from flask import Flask, render_template
import pymongo
import os, ssl
import requests
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import re
import time

def mars_news():
	latest_news = {}
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
	browser.visit(url)
	time.sleep(2)  # 10초 멈추기
	html = browser.html
	soup = bs(html, 'html.parser')
	news_data = soup.find("ul", class_="item_list")
	print(news_data.prettify())
	news_lists = news_data.find_all("div", class_="image_and_description_container")
	print(news_lists[0].prettify())
	latest_news_date = news_lists[0].find("div", class_="list_date").text
	latest_news_title = news_lists[0].find("div", class_="content_title").find("a").text
	latest_news_body_text = news_lists[0].find("div", class_="article_teaser_body").text
	latest_news_link = news_lists[0].find("div", class_="content_title").find("a")["href"]
	latest_news["news_date"] = latest_news_date
	latest_news["new_title"] = latest_news_title
	latest_news["news_link"] = latest_news_link
	latest_news["news_text"] = latest_news_body_text
	print(latest_news)
	browser.quit()
	return latest_news    

def mars_jpl_image():
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(jpl_url)
	html = browser.html
	time.sleep(2)  # 10초 멈추기
	soup = bs(html, 'html.parser')
	image_data = soup.find("div", class_="carousel_container")
	link = image_data.find("article")["style"].split(" ")[1].split("'")[1]
	featured_image_url = "https://www.jpl.nasa.gov"+link
	print(featured_image_url)
	browser.quit()
	return featured_image_url

def mars_weather():
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	tweeter_url = "https://twitter.com/marswxreport?lang=en"
	browser.visit(tweeter_url)
	time.sleep(2)  # 10초 멈추기
	html = browser.html
	soup = bs(html, 'html.parser')
	weather_data = soup.find("main")
	mars_weather = weather_data.find("section").find("div",{"lang":re.compile("en")}).text
	print(mars_weather)
	browser.quit()
	return mars_weather

def mars_fact():
	fact_url = "https://space-facts.com/mars/"
	tables = pd.read_html(fact_url)
	df = tables[0]
	df.columns=["params", "data"]
	df.set_index("params", inplace=True)
	table_html = df.to_html()
	result_html = table_html.replace("\n", "")
	print(result_html)
	return result_html

def mars_hemi():
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(hemis_url)
	time.sleep(2)  # 10초 멈추기
	html = browser.html
	soup = bs(html, 'html.parser')
	products = soup.find_all("a", class_="itemLink")
	link_list = []
	for product in products:
		link = product["href"]
		page_link = "https://astrogeology.usgs.gov"+link
		if page_link not in link_list:
			link_list.append(page_link)
	hemisphere_image_urls = []
	for link in link_list:
		browser.visit(link)
		html= browser.html
		soup = bs(html, 'html.parser')
		try:
			block = soup.find("img",class_="wide-image")["src"]
			astro_html_link = "https://astrogeology.usgs.gov" + block
			astro_title = soup.find("h2", class_="title").text
			page = { "title":astro_title,  "img_url":astro_html_link }
			hemisphere_image_urls.append(page)
		except:
			continue
	for i in range(len(hemisphere_image_urls)):
		print(hemisphere_image_urls[i]["title"])
		print(hemisphere_image_urls[i]["img_url"])
		print("-----")

	browser.quit()
	return hemisphere_image_urls
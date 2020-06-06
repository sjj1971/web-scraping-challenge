# import necessary libraries
from flask import Flask, render_template
from flask import Flask, render_template
import pymongo
import os, ssl
import requests
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import scrapping_data as scd
# from scrapping_data import mars_news, mars_jpl_image, mars_weather, mars_fact, mars_hemi

# @TODO: Initialize your Flask app here

def	scrape():

	result_scrape = {}
	a = scd.mars_news()
	b = scd.mars_jpl_image()
	c = scd.mars_weather()
	d = scd.mars_fact()
	e = scd.mars_hemi()

	result_scrape["latest_news"] = a
	result_scrape["jpl_image_url"] = b
	result_scrape["news_weather"] = c
	result_scrape["mars_table"] = d
	# pd.read_html(d)
	result_scrape["hemi_images"] = e

	return result_scrape

if __name__ == "__main__":

	mars_result_date = {}

	conn= "mongodb://localhost:27017"
	client = pymongo.MongoClient(conn)
	db = client.mars_DB
	collection = db.mars_scrape
	collection.drop()

	mars_result_data = scrape()
	print(mars_result_data)

	collection.insert_one(mars_result_data)

	teams = collection.find()
	print(teams)


	
# 	executable_path = {'executable_path': 'chromedriver.exe'}
# 	browser = Browser('chromedriver', **executable_path, headless=False)
# 	url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
# 	browser.visit(url)

# 	html = browser.html
# 	soup = bs(html, 'html.parser')
# 	data = soup.find("ul", class_="item_list")

# 	news_list = data.find_all("li", class_="slide")

# 	latest_news_date = news_list[0].find("div", class_="list_date").text
# 	latest_news_title = news_list[0].find("div", class_="content_title").find("a").text
# 	latest_news_body_text = news_list[0].find("div", class_="article_teaser_body").text
# 	latest_news_link = news_list[0].find("div", class_="content_title").find("a")["href"]

# 	print(latest_news_date)
# 	print(latest_news_title)
# 	print(latest_news_body_text)
# 	print(latest_news_link)


# 	url = 

# # @TODO:  Create a route and view function that takes in a string and renders index.html template
# # CODE GOES HERE
# @app.route("/")
# def main():
# 	name = "Jungje"
# 	hobby = "Fishing"
# 	return render_template("index.html", name = name, hobby = hobby)

# @app.route("/bonus")
# def bonus():
#     name = "Jungje_bonus"
#     hobby = "Fishing_bonus"
#     return render_template("bonus.html", name = name, hobby = hobby)


# if __name__ == "__main__":
#     app.run(debug=True)

# # CODE GOES HERE
# app = Flask(__name__)
# # @TODO:  Create a route and view function that takes in a string and renders index.html template
# # CODE GOES HERE
# @app.route("/")
# def main():
# 	name = "Jungje"
# 	hobby = "Fishing"
# 	return render_template("index.html", name = name, hobby = hobby)

# @app.route("/bonus")
# def bonus():
#     name = "Jungje_bonus"
#     hobby = "Fishing_bonus"
#     return render_template("bonus.html", name = name, hobby = hobby)


# if __name__ == "__main__":
#     app.run(debug=True)

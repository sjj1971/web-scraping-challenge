# import necessary libraries
from flask import Flask, render_template
import pymongo
import os, ssl
import requests
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import scrapping_data as scd

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
	result_scrape["hemi_images"] = e

	return result_scrape
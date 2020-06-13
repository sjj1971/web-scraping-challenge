from flask import Flask, render_template, redirect
import pymongo
# import os, ssl
# import requests
import pandas as pd
# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# import scrapping_data as scd
import scrape_mars


app = Flask(__name__)

conn= "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_DB
collection = db.mars_scrape

@app.route("/")
def index():
    listings = collection.find_one()
    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    collection.drop()
    mars_result_data = {}
    mars_result_data = scrape_mars.scrape()
    collection.update({},mars_result_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

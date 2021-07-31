import numpy as np
import pandas as pd
import datetime as dt
import pymongo

from flask import Flask, json, jsonify
import scrape_mars 

app = Flask(__name__)
@app.route("/")
def home():
    return ("hello world") 

@app.route("/scrape")
def scrape(): 
    #scrape the data and add the time of the scrape 
    data = scrape_mars.scrape() 
    data["date"] = dt.datetime.utcnow()
    
    #add the dictionary to the mongo database 
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client['scrape_database']
    collection = db['scrape_collection'] 
    collection.insert_one(data)

    return "1"

if __name__ == '__main__':
    app.run(debug=True)
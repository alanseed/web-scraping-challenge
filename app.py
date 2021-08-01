import numpy as np
import pandas as pd
import datetime as dt
import pymongo

from flask import Flask, render_template, redirect
import scrape_mars 

app = Flask(__name__)

#get the most recent scrape and fill out the html template 
@app.route("/")
def home():
    
    #read the most recent data off the database 
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Declare the database
    db = client['scrape_database']

    # Declare the collection
    collection = db['scrape_collection']

    results = collection.find().sort("date",pymongo.DESCENDING)
    message = f"{results[0]['date']}"
    return render_template("index.html", date=message )
    
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
    
    return redirect ("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)
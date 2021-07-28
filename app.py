import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func 
from sqlalchemy import inspect 

from flask import Flask, json, jsonify
import scrape_mars 

app = Flask(__name__)
@app.route("/")
def home():
    return () 

@app.route("/scrape")
def scrape(): 
    data = scrape_mars.scrape() 
    keys = data.keys() 
    for key in keys: 
        print(f"Key = {key}")
        print(data[key])
    return ()

if __name__ == '__main__':
    app.run(debug=True)
#Set Up the Flask Weather App
import datetime as dt
from typing_extensions import runtime
import numpy as np
import pandas as pd

#SQLAlchemy dependencies 
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Flask dependencies 
from flask import Flask, jsonify

#Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

#Access and query SQLite 
Base = automap_base()
Base.prepare(engine, reflect=True)

#References to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Session link from Pyhton
session = Session(engine)

#Set Up the Flask APP
app = Flask(__name__)

#Welcome route 
@app.route('/')
def welcome():
    return('''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#Satation Route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#Monthly Temprerature Route 
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Statistics Route 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

    

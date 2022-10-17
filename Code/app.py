import numpy as np

import sqlalchemy
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import Date, Float, func
from flask import Flask, jsonify
from flask_cors import CORS
import os


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///../Data/exchange_rates.sqlite")
engine2 = create_engine("sqlite:///../Data/avgCurnCountry.sqlite")
connection = engine2.connect()
resultColumn = connection.execute(f"SELECT * FROM avgCurnCountry")
resultColumn =["y1998", "y1999","y2000", "y2001", "y2002", "y2003", 
                "y2004", "y2005", "y2006", "y2007","y2008","y2009", 
                "y2010", "y2011", "y2012", "y2013","y2014", "y2015", 
                "y2016", "y2017", "y2018", "y2019", "y2020", "y2021","y2022"]

# rel_path = os.path.relpath("Data/exchange_rates.sqlite","Code")
# print(rel_path)
# engine = create_engine("sqlite:///"+ rel_path)

# reflect an existing database into a new model
Base = declarative_base()
#Create your class
class ExchangeRates(Base):
    __tablename__ = 'exchange_rates'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    month = Column(Integer)
    year = Column(Integer)
    aud = Column(Float)
    cad = Column(Float)
    eur = Column(Float)
    jpy = Column(Float)
    nzd = Column(Float)
    nok = Column(Float)
    sek = Column(Float)
    chf = Column(Float)
    gbp = Column(Float)
    usd = Column(Float)

# produce relationships
Base.metadata.create_all(engine)

#Create second class
class avgCurrency(Base):
    __tablename__ = 'avgCurnCountry'
    id = Column(Integer, primary_key=True)
    country = Column(String)
    y1998=Column(Float)
    y1999=Column(Float)
    y2000=Column(Float)
    y2001=Column(Float)
    y2002=Column(Float)
    y2003=Column(Float)
    y2004=Column(Float)
    y2005=Column(Float)
    y2006=Column(Float)
    y2007=Column(Float)
    y2008=Column(Float)
    y2009=Column(Float)
    y2010=Column(Float)
    y2011=Column(Float)
    y2012=Column(Float)
    y2013=Column(Float)
    y2014=Column(Float)
    y2015=Column(Float)
    y2016=Column(Float)
    y2017=Column(Float)
    y2018=Column(Float)
    y2019=Column(Float)
    y2020=Column(Float)
    y2021=Column(Float)
    y2022=Column(Float)
# produce relationships
Base.metadata.create_all(engine2)

# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# ExchangeRates = Base.classes.exchange_rates

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/by_date<br/>"
        f"/api/v1.0/data<br/>"
        f"/api/v1.0/time-series<br/>"
        f"/api/v1.0/cad<br/>"
    )


@app.route("/api/v1.0/by_date")
def exhcange_rates():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #"""Return a dictionary of all exhcange rates"""
    # Query all passengers
    results = session.query(ExchangeRates.id,
                            ExchangeRates.date,
                            ExchangeRates.month,
                            ExchangeRates.year,
                            ExchangeRates.aud,
                            ExchangeRates.cad,
                            ExchangeRates.eur,
                            ExchangeRates.jpy,
                            ExchangeRates.nzd,
                            ExchangeRates.nok,
                            ExchangeRates.sek,
                            ExchangeRates.chf,
                            ExchangeRates.gbp,
                            ExchangeRates.usd).all()

    session.close()

    
    all_rates = []
    # Convert list of rows into dict
    for row in results:
        all_rates.append(list(row))

    return jsonify(all_rates)

@app.route("/api/v1.0/data")
def data_json():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #"""Return a dictionary of all exhcange rates"""
    # Query all passengers
    results = session.query(ExchangeRates.id,
                            ExchangeRates.date,
                            ExchangeRates.month,
                            ExchangeRates.year,
                            ExchangeRates.aud,
                            ExchangeRates.cad,
                            ExchangeRates.eur,
                            ExchangeRates.jpy,
                            ExchangeRates.nzd,
                            ExchangeRates.nok,
                            ExchangeRates.sek,
                            ExchangeRates.chf,
                            ExchangeRates.gbp,
                            ExchangeRates.usd).all()

    session.close()

    results_tuple = []
    for i in range(len(results)):
        result_dict = {}
        result_dict["id"] = results[i][0]
        result_dict["date"] = results[i][1]
        result_dict["month"] = results[i][2]
        result_dict["year"] = results[i][3]
        result_dict["aud"] = results[i][4]
        result_dict["cad"] = results[i][5]
        result_dict["eur"] = results[i][6]
        result_dict["jpy"] = results[i][7]
        result_dict["nzd"] = results[i][8]
        result_dict["nok"] = results[i][9]
        result_dict["sek"] = results[i][10]
        result_dict["chf"] = results[i][11]
        result_dict["gbp"] = results[i][12]
        result_dict["usd"] = results[i][13]
        results_tuple.append(result_dict)

    return jsonify(results_tuple)

@app.route("/api/v1.0/time-series")
def time_series_data_json():
    session = Session(engine2)
    # Query table
    resultColumnheader =resultColumn
    results_AUD = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "AUD").all()
    results_CAD = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "CAD").all()
    results_EUR = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "EUR").all()
    results_JPY = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "JPY").all()
    results_NZD = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "NZD").all()
    results_NOK = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "NOK").all()                           
    results_SEK = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "SEK").all()                           
    
    results_CHF = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "CHF").all()                         
                            
                            
    results_GBP = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "GBP").all() 

    results_USD = session.query(avgCurrency.y1998,
                            avgCurrency.y1999,
                            avgCurrency.y2000,
                            avgCurrency.y2001,
                            avgCurrency.y2002,
                            avgCurrency.y2003,
                            avgCurrency.y2004,
                            avgCurrency.y2005,
                            avgCurrency.y2006,
                            avgCurrency.y2007,
                            avgCurrency.y2008,
                            avgCurrency.y2009,
                            avgCurrency.y2010,
                            avgCurrency.y2011,
                            avgCurrency.y2012,
                            avgCurrency.y2013,
                            avgCurrency.y2014,
                            avgCurrency.y2015,
                            avgCurrency.y2016,
                            avgCurrency.y2017,
                            avgCurrency.y2018,
                            avgCurrency.y2019,
                            avgCurrency.y2020,
                            avgCurrency.y2021,
                            avgCurrency.y2022).filter(avgCurrency.country == "USD").all()
    session.close()
    
    all_AUD = list(np.ravel(results_AUD))
    all_CAD = list(np.ravel(results_CAD))
    all_EUR = list(np.ravel(results_EUR))
    all_JPY = list(np.ravel(results_JPY))
    all_NZD = list(np.ravel(results_NZD))
    all_NOK = list(np.ravel(results_NOK))
    all_SEK = list(np.ravel(results_SEK))
    all_CHF = list(np.ravel(results_CHF))
    all_GBP = list(np.ravel(results_GBP))
    all_USD = list(np.ravel(results_USD))


    all_Years = list(np.ravel(resultColumnheader))
    #Create a dictionary from the row data and append to a list of all_year
    #create list 
    #all_years =[]
    #for year in results:
    return jsonify(all_Years,all_AUD,all_CAD,all_EUR,all_JPY,all_NZD,all_NOK,all_SEK,all_CHF,all_GBP,all_USD)

@app.route("/api/v1.0/cad")
def cad():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of CAD exhcange rates"""
    # Query all passengers
    results = session.query(ExchangeRates.cad).all()

    session.close()

    # Convert list of tuples into normal list
    all_cad = list(np.ravel(results))

    return jsonify(all_cad)

if __name__ == '__main__':
    app.run(debug=True)
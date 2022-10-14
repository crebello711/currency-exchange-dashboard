import numpy as np

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import Date, Float, func
from flask import Flask, jsonify
from flask_cors import CORS


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Data/exchange_rates.sqlite")

# reflect an existing database into a new model
Base = declarative_base()

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

    # print(results)
    
    # all_rates = {}
    # # Convert list of rows into dict
    # for row in results:
    #     all_rates[str(row)] = list(np.ravel(row))

    return jsonify(results)

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

    # print(results)
    
    # all_rates = {}
    # # Convert list of rows into dict
    # for row in results:
    #     all_rates[str(row)] = list(np.ravel(row))

    return jsonify(results_tuple)

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
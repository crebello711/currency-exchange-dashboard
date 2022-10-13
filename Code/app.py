import numpy as np

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import Date, Float, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Data/exchange_rates.sqlite")

# reflect an existing database into a new model
Base = declarative_base()

class ExchangeRates(Base):
    __tablename__ = 'exchange_rates'

    Date = Column(Date, primary_key=True)
    AUD = Column(String)
    CAD = Column(String)
    EUR = Column(String)
    JPY = Column(String)
    NZD = Column(String)
    NOK = Column(String)
    SEK = Column(String)
    CHF = Column(String)
    GBP = Column(String)
    USD = Column(String)

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


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/all_ratescd <br/>"
        f"/api/v1.0/cad<br/>"
    )


@app.route("/api/v1.0/all_rates")
def exhcange_rates():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dictionary of all exhcange rates"""
    # Query all passengers
    results = session.query(ExchangeRates.Date,
                            ExchangeRates.AUD,
                            ExchangeRates.CAD,
                            ExchangeRates.EUR,
                            ExchangeRates.JPY,
                            ExchangeRates.NZD,
                            ExchangeRates.NOK,
                            ExchangeRates.SEK,
                            ExchangeRates.CHF,
                            ExchangeRates.GBP,
                            ExchangeRates.USD).all()

    session.close()

    # print(results)
    
    # all_rates = {}
    # # Convert list of rows into dict
    # for row in results:
    #     all_rates[str(row)] = list(np.ravel(row))

    return results

@app.route("/api/v1.0/cad")
def cad():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of AUD exhcange rates"""
    # Query all passengers
    results = session.query(ExchangeRates.CAD).all()

    session.close()

    # Convert list of tuples into normal list
    all_cad = list(np.ravel(results))

    return jsonify(all_cad)

if __name__ == '__main__':
    app.run(debug=True)
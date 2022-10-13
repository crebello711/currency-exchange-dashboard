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


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/by_date<br/>"
        f"/api/v1.0/cad<br/>"
    )


@app.route("/api/v1.0/by_date")
def exhcange_rates():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dictionary of all exhcange rates"""
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
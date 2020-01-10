import os
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine(f"postgres://postgres:postgres@localhost:5432/houston_statistics_db")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
oil = Base.classes.oilprice
engy_employees = Base.classes.energy_extraction_employees
employees = Base.classes.nonfarm_employees
population = Base.classes.population
housing = Base.classes.housing_index

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
        f"Available Routes:<br>"
        f"/api/v1.0/houston_statistics<br>"
        f"/api/v1.0/houston_population<br>"
        f"/api/v1.0/houston_non-farm_employees<br>"
        f"/api/v1.0/houston_energy_extraction_employees<br>"
        f"/api/v1.0/houston_housing_index<br>"
        f"/api/v1.0/WTI Oil Price"
    )

@app.route("/api/v1.0/houston_statistics")
def stats():
    """Return Houston statistics data"""

    # Query data
    session = Session(engine)
    results = session.query(housing, oil, engy_employees, employees, population).filter(housing.year == oil.year, housing.year == engy_employees.year, housing.year == employees.year, housing.year == population.year).all()
    session.close()

    #Create a dictionary from the row data and append
    data = []
    for result in results:
        data_dict = {}
        data_dict["year"] = result.housing_index.year
        data_dict["population"] = result.population.population
        data_dict["employees"] = result.nonfarm_employees.employees
        data_dict["engy_employees"] = result.energy_extraction_employees.employees
        data_dict["oil_price(usd)"] = result.oilprice.oilprice_usd
        data_dict["housing_price_index"] = result.housing_index.housing_price_index
        data.append(data_dict)
    return jsonify(data)

@app.route("/api/v1.0/houston_population")
def pop():
    """Return Houston popuation data"""

    # Query data
    session = Session(engine)
    results = session.query(population).all()
    session.close()

    #Create a dictionary from the row data and append
    data = []
    for result in results:
        data_dict = {}
        data_dict["year"] = result.year
        data_dict["population"] = result.population
        data.append(data_dict)
    return jsonify(data)

@app.route("/api/v1.0/houston_non-farm_employees")
def emp():
    """Return Houston non-farm employees data"""

    # Query data
    session = Session(engine)
    results = session.query(employees).all()
    session.close()

    #Create a dictionary from the row data and append
    data = []
    for result in results:
        data_dict = {}
        data_dict["year"] = result.year
        data_dict["employees"] = result.employees
        data.append(data_dict)
    return jsonify(data)

@app.route("/api/v1.0/houston_energy_extraction_employees")
def engyemp():
    """Return Houston energy extraction employees data"""

    # Query data
    session = Session(engine)
    results = session.query(engy_employees).all()
    session.close()

    #Create a dictionary from the row data and append
    data = []
    for result in results:
        data_dict = {}
        data_dict["year"] = result.year
        data_dict["employees"] = result.employees
        data.append(data_dict)
    return jsonify(data)

@app.route("/api/v1.0/WTI Oil Price")
def price():
    """Return world oil price data"""

    # Query data
    session = Session(engine)
    results = session.query(oil).all()
    session.close()

    #Create a dictionary from the row data and append
    data = []
    for result in results:
        data_dict = {}
        data_dict["year"] = result.year
        data_dict["oil_price(usd)"] = result.oilprice_usd
        data.append(data_dict)
    return jsonify(data)

@app.route("/api/v1.0/houston_housing_index")
def index():
    """Return Houston housing index data"""

    # Query data
    session = Session(engine)
    results = session.query(housing).all()
    session.close()

    #Create a dictionary from the row data and append
    data = []
    for result in results:
        data_dict = {}
        data_dict["year"] = result.year
        data_dict["housing_price_index"] = result.housing_price_index
        data.append(data_dict)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

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
        f"/api/v1.0/WTI Oil Price"
    )

@app.route("/api/v1.0/houston_statistics")
def stats():
    """Return Houston statistics data"""

    # Query population
    session = Session(engine)
    results = session.query(housing, oil, engy_employees, employees, population).filter(housing.year == oil.year == engy_employees.year == employees.year == population.year).all()
    session.close()

    # Convert list of tuples into normal list
    stats = list(np.ravel(results))

    return jsonify(results)

@app.route("/api/v1.0/houston_population")
def pop():
    """Return Houston popuation data"""

    # Query population
    session = Session(engine)
    results = session.query(population).all()
    session.close()

    #Create a dictionary from the row data and append to station data
    pop = []
    for data in results:
        pop_dict = {}
        pop_dict["year"] = data.year
        pop_dict["population"] = data.population
        pop.append(pop_dict)
    return jsonify(pop)

    return jsonify(pop)

if __name__ == '__main__':
    app.run(debug=True)

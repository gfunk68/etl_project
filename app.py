import os
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
popuation = Base.classes.population
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
        f"Available Routes:<br/>"
        f"/api/v1.0/houston_statistics"
        f"/api/v1.0/houston_population<br/>"
        f"/api/v1.0/WTI Oil Price"
    )

@app.route("/api/v1.0/houston_statistics")
def stats():
    """Return Houston statistics data"""

    # Query population
    session = Session(engine)
    results = session.query(housing, oil, engy_employees, employees, population).filter(housing.year == oil.year == engy_employees.year == employees.years == population.years).all()
    session.close()

    # Convert list of tuples into normal list
    stats = list(np.ravel(results))

    return jsonify(stats)

@app.route("/api/v1.0/houston_population")
def pop():
    """Return Houston popuation data"""

    # Query population
    session = Session(engine)
    results = session.query(population).all()
    session.close()

    # Convert list of tuples into normal list
    pop = list(np.ravel(results))

    return jsonify(pop)

if __name__ == '__main__':
    app.run(debug=True)

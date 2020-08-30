import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

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
        f"<a href='/api/v1.0/precipitation'>precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>tobs</a> (temperature)<br/>"
        f"<a href='/api/v1.0/<start>'>start</a> (temperature)<br/>"
        f"<a href='/api/v1.0/<start>/<end>'>start and end</a> (temperature)"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of dates and precipitation"""
    # Query all dates and preciptation
    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()
    
    all_prcp= []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query all stations
    results = session.query(Station.id, Station.station, Station.name).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for id, station, name in results:
        station_dict = {}
        station_dict["id"] = id
        station_dict["station"] = station
        station_dict["name"] = name
        all_stations.append(station_dict)

    return jsonify(all_stations)

if __name__ == '__main__':
    app.run(debug=True)

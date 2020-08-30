import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

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
        f"<a href='/api/v1.0/<start>'>start date</a> (temperature)<br/>"
        f"<a href='/api/v1.0/<start>/<end>'>start and end date</a> (temperature)"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of dates and precipitation"""
    # Query all dates and preciptation
    results = session.query(Measurement.station, Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()
    
    all_prcp= []
    for station, date, prcp in results:
        prcp_dict = {}
        prcp_dict["station"] = station
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

    # Create a list of all the stations
    all_stations = list(np.ravel(results))
    # all_stations = []
    # for id, station, name in results:
    #     station_dict = {}
    #     station_dict["id"] = id
    #     station_dict["station"] = station
    #     station_dict["name"] = name
    #     all_stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of dates and tobs for the most active station in the last year"""
    # Query all dates and temeratures for the most active station in the last year
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23', Measurement.station == 'USC00519281').order_by(Measurement.date).all()

    session.close()

    # Create a list of list of all the tempearatures for the most active station in the last year.
    all_tobs = list(np.ravel(results))
    # all_tobs= []
    # for date, tobs in results:
    #     tobs_dict = {}
    #     tobs_dict[date] = tobs
    #     all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a tobs summary from the specfied date to the last entry"""
    # Query specfied date to the last entry for tobs summary
    sel = [func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start).order_by(Measurement.date).all()

    session.close()
    
    # Create a list of list of all the tempearatures for the most active station in the last year.
    tobs_summary = []
    for min, max, avg in results:
        tobs_dict = {}
        tobs_dict['tobs min'] = min
        tobs_dict['tobs max'] = max
        tobs_dict['tobs avg'] = avg

        tobs_summary.append(tobs_dict)

    return jsonify(tobs_summary)

@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a tobs summary for the specified date range"""
    # Query a date range and return the tobs summary
    sel = [func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    results = session.query(*sel).filter(Measurement.date >= start, Measurement.date <= end).order_by(Measurement.date).all()

    session.close()

    # Create a dictionary of the tobs summary for a date range
    tobs_summary = []
    for min, max, avg in results:
        tobs_dict = {}
        tobs_dict['tobs min'] = min
        tobs_dict['tobs max'] = max
        tobs_dict['tobs avg'] = avg

        tobs_summary.append(tobs_dict)

    return jsonify(tobs_summary)

if __name__ == '__main__':
    app.run(debug=True)

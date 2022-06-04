from asyncio import start_server
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station= Base.classes.station

app = Flask(__name__)



# ## Step 2 - Climate App

# Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

# * Use Flask to create your routes.

# ### Routes

# * `/`

#   * Home page.
#   * List all routes that are available.

@app.route("/")
def Greetings():
    return (
        f"Available Routes in Hawaii Climate API:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"

    )

# * `/api/v1.0/precipitation`

#   * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

#   * Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def rain():
    session=Session(engine)

    rain_by_date= session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23')

    session.close()

    rain_latestyear=[]
    for date, prcp in rain_by_date:
        rain_dictionary={}
        rain_dictionary["date"] = date
        rain_dictionary["prcp"] = prcp
        rain_latestyear.append(rain_dictionary)
    
    return jsonify(rain_latestyear)



# * `/api/v1.0/stations`
@app.route("/api/v1.0/stations")
def stations():
    session= Session(engine)

    #create a query for all stations in the dataset

    all_stations= session.query(Station.station).all()

    session.close()

    stations_list=list(np.ravel(all_stations))

    #   * Return a JSON list of stations from the dataset.

    return jsonify(stations_list)



# * `/api/v1.0/tobs`
#   * Query the dates and temperature observations of the most active station for the last year of data.

#   * Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs")
def temp():
    session=Session(engine)

    dates_temp_mostactive=active_station_recenttemp=session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.station=='USC00519281')\
        .filter(Measurement.date>= '2016-08-23').all()

    session.close()

    all_days_temp=list(np.ravel(dates_temp_mostactive))

    return jsonify(all_days_temp)

 

@app.route("/api/v1.0/<start>")
def start_temp(start):
    session=Session(engine)

    #   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
    specific_day_temp_stats=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs))\
    .filter(Measurement.date >=start).all()

    session.close()

    temps_pickday=list(np.ravel(specific_day_temp_stats))

    return jsonify(temps_pickday)





     












# @app.route("/api/v1.0/start/end")


# * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

# ## Hints

# * You will need to join the station and measurement tables for some of the queries.

# * Use Flask `jsonify` to convert your API data into a valid JSON response object.

# - - -

if __name__ == '__main__':
    app.run(debug=True)
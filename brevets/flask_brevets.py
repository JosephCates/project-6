"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import requests
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import logging


import os


BREVETS_PORT = os.environ.get('PORT')
API_PORT = os.environ.get("API_PORT")


###
# Globals
###
app = flask.Flask(__name__)

###
# Pages
###
@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")


    km = request.args.get('km', 999, type=float)
    distance = request.args.get('distance', 999, type=int)
    begin_date = request.args.get('begin_date')



    app.logger.debug("km={}".format(km))
    app.logger.debug("distance={}".format(distance))
    app.logger.debug("begin_date={}".format(begin_date))
    app.logger.debug("request.args: {}".format(request.args))
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!
    open_time = acp_times.open_time(km, distance, arrow.get(begin_date)).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, distance, arrow.get(begin_date)).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)



@app.route("/submit", methods=['POST'])
def submit():
    JSONrequest = request.get_json()

    data = {
        "length": JSONrequest['length'],
        "start_time": JSONrequest['start_time'],
        "checkpoints": JSONrequest['checkpoints'],
    }
    
    status = requests.post(f"http://api:{API_PORT}/api/brevets", json=data)
    print("status code:", status.status_code)
    return flask.Response(status=status.status_code)

@app.route("/display")
def display():
    data = requests.get(f"http://api:{API_PORT}/api/brevets").json()
    return flask.jsonify(brevets={"length": data[-1]['length'], "start_time": data[-1]['start_time'], "checkpoints": data[-1]['checkpoints']}, status=200)
#############








if __name__ == "__main__":
    app.run(port=BREVETS_PORT, host="0.0.0.0")

"""
Brevets RESTful API
"""
from flask import Flask
import os
from flask_restful import Api
from mongoengine import connect
from resources import BrevetAPI
from resources import BrevetsAPI



API_PORT = os.environ.get('API_PORT')


app = Flask(__name__)
api = Api(app)
connect(host="mongodb://db:27017/brevets")

api.add_resource(BrevetAPI, "/api/brevet/<id>")
api.add_resource(BrevetsAPI, "/api/brevets")


if __name__ == "__main__":
    app.run(port=API_PORT, host="0.0.0.0")

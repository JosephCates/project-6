import flask
from database import Brevets
from flask_restful import Resource


class BrevetAPI(Resource):
    def get(self, id):
        brevet = Brevets.objects.get(id=id).to_json()
        return flask.Response(brevet, mimetype="application/json", status=200)

    def put(self, id):
        JSONrequest = flask.request.json()
        Brevets.objects.get(id=id).update(**JSONrequest)
        return {'id': str(id), 'status': 'updated'}, 200

    def delete(self, id):
        Brevets.objects.get(id=id).delete()
        return {'id': str(id), 'status': 'deleted'}, 200

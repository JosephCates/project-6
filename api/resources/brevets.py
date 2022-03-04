from flask import Response, request
from database import Brevets
from flask_restful import Resource

class BrevetsAPI(Resource):
    def get(self):
        brevets = Brevets.objects().to_json()
        return Response(brevets, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        brevet = Brevets(**body).save()
        id = brevet.id
        return {'id': str(id), 'status': 'saved'}, 200

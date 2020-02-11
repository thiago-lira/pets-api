from flask import Blueprint
from flask_restful import Resource, Api


class Subscribers(Resource):
    def get(self):
        return {
            'name': 'oi'
        }


subscribers_bp = Blueprint('subscribers', __name__)
api = Api(subscribers_bp)
api.add_resource(Subscribers, '/v1/subscribers')

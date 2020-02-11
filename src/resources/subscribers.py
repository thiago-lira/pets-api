from flask import Blueprint
from flask_restful import Resource, Api
from src.models.subscriber import Subscriber


class Subscribers(Resource):
    def get(self):
        return Subscriber.find_all()


subscribers_bp = Blueprint('subscribers', __name__)
api = Api(subscribers_bp)
api.add_resource(Subscribers, '/v1/subscribers')

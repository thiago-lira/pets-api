from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from src.models.subscriber import Subscriber

parse = reqparse.RequestParser()
parse.add_argument('nome', required=True, type=str,
                   help='Necessário informar o nome')
parse.add_argument('total-gatinhos', required=True, type=str,
                   help='Necessário informar o total de gatinhos')
parse.add_argument('nivel', required=True, type=str,
                   help='Necessário informar o nível de conhecimento')
parse.add_argument('cor', required=True, type=str,
                   help='Necessário informar a/s cor/es')
parse.add_argument('filhote-castrado', required=True, type=str,
                   help='Necessário informar se o filhote é castrado')
parse.add_argument('estado', required=True, type=str,
                   help='Necessário informar o estado')


class Subscribers(Resource):
    def get(self):
        return {
            'data': [subscriber.to_dict()
                     for subscriber in Subscriber.find_all()]
        }

    def post(self):
        data = parse.parse_args()
        puppy_castrated = True if data['filhote-castrado'] == 'sim' else False
        mapping_data = {
            'name': data['nome'],
            'total_cats': data['total-gatinhos'],
            'cat_knowledge_level': data['nivel'],
            'color': data['cor'],
            'puppy_castrated': puppy_castrated,
            'br_state': data['estado']
        }
        try:
            subscriber = Subscriber(**mapping_data)
            subscriber.save()
            return subscriber.to_dict(), 201
        except Exception as error:
            return {
                'message': 'Houve algum erro ao tentar salvar os dados.'
            }, 500


subscribers_bp = Blueprint('subscribers', __name__)
api = Api(subscribers_bp)
api.add_resource(Subscribers, '/v1/subscribers')

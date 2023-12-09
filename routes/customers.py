from flask import request
from flask_restful import Resource

from models.Response import make_response_with_data


class CustomersRoute(Resource):
    def get(self):
        is_finished = request.args.get('is_finished')
        filter_fio = request.args.get('filter_fio')

        return make_response_with_data(None)

    def post(self):
        customer = request.get_json()

        return make_response_with_data(None)


class CustomerRoute(Resource):
    def get(self, customer_id):
        return make_response_with_data(None)

    def done(self, customer_id):
        # todo: вот здесь должна быть функциональность отправки писем на почту

        return make_response_with_data(None)

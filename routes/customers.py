from flask import request
from flask_restful import Resource


class CustomersRoute(Resource):
    def get(self):
        is_finished = request.args.get('is_finished')
        filter_fio = request.args.get('filter_fio')
        return {}

    def post(self):
        customer = request.get_json()

        return {}


class CustomerRoute(Resource):
    def get(self, customer_id):
        return {}

    def done(self, customer_id):
        return {}

from flask_restful import Resource

from models.Response import make_response_with_data


class PrintFileRoute(Resource):
    def get(self, customer_id):
        return make_response_with_data(None)


class CSVDumpRoute(Resource):
    def get(self):
        return make_response_with_data(None)

from flask_restful import Resource


class PrintFileRoute(Resource):
    def get(self, customer_id):
        return {}


class CSVDumpRoute(Resource):
    def get(self):
        return {}

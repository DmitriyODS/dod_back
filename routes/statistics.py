from flask_restful import Resource

from models.Response import make_response_with_data


class StatisticsRoute(Resource):
    def get(self):
        return make_response_with_data(None)

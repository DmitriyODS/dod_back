from flask import Flask, Blueprint
from flask_restful import Api

from routes.customers import CustomersRoute, CustomerRoute
from routes.generations import PrintFileRoute, CSVDumpRoute
from routes.statistics import StatisticsRoute


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    api_bp = Blueprint('routes', __name__)
    api = Api(api_bp)

    api.add_resource(CustomersRoute, '/customers')
    api.add_resource(CustomerRoute, '/customer/<user_id>')

    api.add_resource(StatisticsRoute, '/statistics')

    api.add_resource(PrintFileRoute, '/print_file/<user_id>')

    api.add_resource(CSVDumpRoute, '/csv_dump')

    app.register_blueprint(api_bp)

    return app

from flask import Flask
from flask_restful import Api

from routes.customers import CustomersRoute, CustomerRoute
from routes.generations import PrintFileRoute, CSVDumpRoute
from routes.statistics import StatisticsRoute


def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(CustomersRoute, '/customers')
    api.add_resource(CustomerRoute, '/customer/<int:user_id>')
    api.add_resource(CustomerRoute, '/customer/<int:user_id>', endpoint='done')
    api.add_resource(StatisticsRoute, '/statistics')
    api.add_resource(PrintFileRoute, '/print_file/<int:user_id>')
    api.add_resource(CSVDumpRoute, '/csv_dump')

    app.run(debug=True)


if __name__ == '__main__':
    main()

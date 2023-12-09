import os
from dotenv import load_dotenv

load_dotenv()

PSQL_URL = os.getenv('PSQL_URL')

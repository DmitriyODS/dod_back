from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

from app import app

Base = declarative_base()
metaData = Base.metadata
db = SQLAlchemy(app)

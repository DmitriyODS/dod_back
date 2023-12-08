# from models.ResponseModels import ResponseStatus
from .

def response_ok(data: dict):
    return {'status': ResponseStatus.success}
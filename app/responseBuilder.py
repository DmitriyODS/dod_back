from app.models.ResponseModels import ResponseStatus


def response_ok(data: dict):
    return {'status': ResponseStatus.success, 'data': data}

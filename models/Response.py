def make_response_with_data(data):
    return {
        'ok': True,
        'description': '',
        'data': data
    }


def make_response_with_err(description):
    return {
        'ok': False,
        'description': description,
        'data': None
    }

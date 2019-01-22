import json
from json.decoder import JSONDecodeError


def raise_response_error(response):
    try:
        data = json.loads(response.text)
    except JSONDecodeError:
        raise Exception('Something went wrong. Please try again later.')

    error = data['error']['errors'][0]
    exc = Exception

    # Create Exception type matching the
    # exception given by the API if it is given
    if error.get('reason'):
        exc = type(error['reason'], (Exception,), {})

    raise exc(error['message'])

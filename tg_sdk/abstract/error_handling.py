import json
from json.decoder import JSONDecodeError


def raise_response_error(response):
    try:
        data = json.loads(response.text)
    except JSONDecodeError:
        raise Exception('Something went wrong. Please try again later.')

    errors = data.get('error').get('errors')
    exc = Exception

    if errors[0].get('reason'):
        exc = type(errors[0].get('reason'),
                   (Exception,),
                   {})
    raise exc(errors[0].get('message'))

import json
import requests

import ticketguardian
from ticketguardian._project._decorators import affiliate_test_method


@affiliate_test_method
def test_retrieve_resource():
    for attr in vars(ticketguardian):
        cls = getattr(ticketguardian, attr)
        if hasattr(cls, 'resource') and hasattr(cls, 'retrieve'):
            response = requests.request(
                "GET",
                cls()._make_url(),
                headers=cls()._default_headers
            )
            # Get list of objects
            data = json.loads(response.text)
            objects = data.get('results')
            obj = objects[0]
            id_name = getattr(cls, 'id_name', 'id')
            alt_id_names = {
                'Order': 'order_number',
                'Policy': 'policy_number'
            }
            if cls.__name__ in alt_id_names:
                id_name = alt_id_names[cls.__name__]

            # Skip if object is customers since customer does not have an id
            # when listed.
            if cls.resource == 'customers':
                continue

            # Skip objects that have a null id
            if not obj.get(id_name):
                for i in objects[1:]:
                    if i[id_name]:
                        obj = i
                        break

            # Use sdk to retrieve object using the first objects id
            resource_object = cls().retrieve(obj[id_name])
            for attr in obj:
                assert hasattr(resource_object, attr)


@affiliate_test_method
def test_list_resource():
    for attr in vars(ticketguardian):
        cls = getattr(ticketguardian, attr)
        if hasattr(cls, 'resource') and hasattr(cls, 'list'):
            response = requests.request(
                "GET",
                cls()._make_url(),
                headers=cls()._default_headers
            )
            # Get list of objects
            data = json.loads(response.text)
            objects = data.get('results')
            obj = objects[0]

            # Get list using sdk
            resource_objects = cls().list()
            assert len(resource_objects) > 0
            assert len(resource_objects) == data.get('count')

            for attr in obj:
                assert hasattr(resource_objects[0], attr)

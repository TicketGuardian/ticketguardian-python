from ticketguardian.client import Client

from ticketguardian._project._decorators import affiliate_test_method


def test_client_patch():
    client = Client.list(limit=1)[0]
    patch_result = client.patch(
        client.id, name='test_patch')
    assert client.name == 'test_patch'

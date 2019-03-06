from ticketguardian.client import Client

from ticketguardian._project._decorators import affiliate_test_method


@affiliate_test_method
def test_client_patch():
    client = Client.list(limit=1)[0]
    client_name = client.name

    client.patch(client.id, name=client_name + 'test_patch')
    assert client.name == client_name + 'test_patch'

    # Change name back
    client.patch(client.id, name=client_name)

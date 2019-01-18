from ticketguardian.quote import Quote
from ticketguardian._project._decorators import client_test_method


@client_test_method
def test_get_quote():
    params = {
        "items": [
            {
                "name": "Ticket 00001 - Johnny Appleseed",
                "reference_number": "8M720WCMLO",
                "cost": "2000.00"
            },
            {
                "name": "Ticket 00002 - Tommy Appleseed",
                "reference_number": "8M720WCMLO",
                "cost": "30.00"
            }
        ],
        "currency": "CAD"
    }

    results = ["currency", "symbol", "total", "quote"]

    quote = Quote(**params)

    for key in results:
        assert hasattr(quote, key)

from ticketguardian.affiliate import Affiliate


def test_affiliate_patch():
    aff = Affiliate.list(limit=1)[0]
    aff_name = aff.name
    aff.patch(aff.id, name=aff_name + 'test_patch')
    assert aff.name == aff_name + 'test_patch'
    # Change name back
    aff.patch(aff.id, name=aff_name)

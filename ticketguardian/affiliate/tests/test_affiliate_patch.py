from ticketguardian.affiliate import Affiliate


def test_affiliate_patch():
    aff = Affiliate.list(limit=1)[0]
    patch_result = aff.patch(
        aff.id, name='test_patch')
    assert aff.name == 'test_patch'

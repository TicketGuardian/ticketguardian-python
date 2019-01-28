from ticketguardian.affiliate import Affiliate
from ticketguardian._project._decorators import affiliate_test_method


@affiliate_test_method
def test_affiliate_patch():
    aff = Affiliate.list(limit=1)[0]
    patch_result = aff.patch(
        aff.id, name='test_patch')
    assert aff.name == 'test_patch'

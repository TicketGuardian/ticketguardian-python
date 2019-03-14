from ticketguardian.user.user import User

from ticketguardian._project._decorators import affiliate_test_method


@affiliate_test_method
def test_user_patch():
    user = User.list()[0]
    first_name = user.first_name
    user.patch(first_name='test_patch')
    assert user.first_name == 'test_patch'
    user.patch(first_name=first_name)


@affiliate_test_method
def test_user_update():
    user = User.list()[0]
    user_info = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "is_active": user.is_active,
        "role": user.role
    }
    new_info = {
        "first_name": "SDK_update",
        "last_name": "test",
        "email": "sdkupdatetest@mail.com",
        "is_active": True,
        "role": "Sales"
    }
    user.patch(**new_info)
    for attr in new_info:
        assert getattr(user, attr) == new_info[attr]
    user.patch(**user_info)

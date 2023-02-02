from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


def test_user_diretor(user):
    if user.is_diretor or user.is_staff:
        return True
    raise PermissionDenied


class UserTypeTest(UserPassesTestMixin):
    user_type = None
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.tipo == self.user_type or user.is_staff
    

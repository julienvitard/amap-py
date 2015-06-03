
from django.contrib.auth import get_user_model
from django.test import TestCase
from amappy.users.models import User

from rest_framework import status


test_attributes = {
    "username":       "uset_test",
    "email":          "user_test+amappy@gmail.com",
    "first_name":     "User",
    "last_name":      "Test",
    "phone_number":   "6666666666",
    "is_distributor": False,
    "is_supervisor":  False,
}


class UserModelTest(TestCase):
    def setUp(self):
        self.model = get_user_model()

    def test_user_model(self):
        assert self.model is User

    def test_user_attributes(self):
        user = self.model.objects.create(**test_attributes)
        for attribute in test_attributes.keys():
            assert hasattr(user, attribute)

    def test_user_creation(self):
        user = self.model.objects.create(**test_attributes)
        assert isinstance(user, self.model)
        assert user.__unicode__() == user.username

    def test_users_list_view(self):
        empty_resp = self.client.get('/users/')
        assert empty_resp.status_code == status.HTTP_200_OK
        assert empty_resp.data == []

        self.model.objects.create(**test_attributes)
        resp = self.client.get('/users/')
        assert len(resp.data) == 1

    def test_users_list_index(self):
        self.model.objects.create(**test_attributes)
        resp = self.client.get('/users/1/')
        user = resp.data
        for key, value in test_attributes.items():
            assert user.get(key) == value

    def test_users_deny_delete(self):
        self.model.objects.create(**test_attributes)
        # no credentials to delete user
        resp = self.client.delete('/users/1/')
        assert resp.status_code == status.HTTP_403_FORBIDDEN
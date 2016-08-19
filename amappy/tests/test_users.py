#! /usr/bin/env python
# endcoding: utf8

import unittest


class TestUsers(unittest.TestCase):

    def test_get_users(self):
        from amappy.resources.users import get_users
        result = get_users()
        self.assertIsInstance(result, (list, ))

    def test_create_user(self):
        from amappy.resources.users import create_user
        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        result = create_user(data)
        self.assertEqual(len(result), 32)

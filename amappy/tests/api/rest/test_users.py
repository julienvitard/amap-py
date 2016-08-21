#! /usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import json
import unittest


class UsersTestCase(unittest.TestCase):

    def setUp(self):
        from amappy.api.rest import app
        from amappy.persistence import UsersDB

        self.app = app.test_client()
        self.app.testing = True
        UsersDB.reset()

    def test_get_users(self):
        url = '/users'
        result = self.app.get(url)
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(data, [])

    def test_get_user_unexisting(self):
        url = '/users/user_does_not_exist'
        result = self.app.get(url)
        self.assertEqual(result.status_code, 404)

    def test_get_user(self):
        from amappy.persistence import UsersDB

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        url = "/users"

        result = self.app.post(url, data=data)
        self.assertEqual(result.status_code, 200)

        url = "/users/1" 

        result = self.app.get(url)
        self.assertEqual(result.status_code, 200)



        # results = json.loads(result.get_data(as_text=True))
        # self.assertEqual(len(results), 1)

        # user = results[0]
        # self.assertEqual(user.get("id"), 1)
        # self.assertEqual(user.get("first_name"), data.get("first_name"))
        # self.assertEqual(user.get("name"), data.get("name"))
        # self.assertEqual(user.get("email"), data.get("email"))

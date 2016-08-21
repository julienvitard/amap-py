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

    def test_get_user_by_id(self):
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

        user = json.loads(result.get_data(as_text=True))
        self.assertEqual(user["first_name"], data["first_name"])
        self.assertEqual(user["name"], data["name"])
        self.assertEqual(user["email"], data["email"])

    def test_get_user_by_name(self):
        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        url = "/users"

        result = self.app.post(url, data=data)
        self.assertEqual(result.status_code, 200)

        url = "/users/Doe"

        result = self.app.get(url)
        self.assertEqual(result.status_code, 200)

        user = json.loads(result.get_data(as_text=True))
        self.assertEqual(user["first_name"], data["first_name"])
        self.assertEqual(user["name"], data["name"])
        self.assertEqual(user["email"], data["email"])

    def test_update_user_by_id(self):
        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        url = "/users"

        result = self.app.post(url, data=data)
        self.assertEqual(result.status_code, 200)

        newdata = {
            "first_name": "Jane",
            "email":      "jane.doe@example.net"
        }
        url = "/users/1"

        result = self.app.put(url, data=newdata)
        self.assertEqual(result.status_code, 200)

        user = json.loads(result.get_data(as_text=True))
        self.assertEqual(user["first_name"], newdata["first_name"])
        self.assertEqual(user["name"], data["name"])
        self.assertEqual(user["email"], newdata["email"])

    def test_update_user_by_name(self):
        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        url = "/users"

        result = self.app.post(url, data=data)
        self.assertEqual(result.status_code, 200)

        newdata = {
            "first_name": "Jane",
            "email":      "jane.doe@example.net"
        }
        url = "/users/Doe"

        result = self.app.put(url, data=newdata)
        self.assertEqual(result.status_code, 200)

        user = json.loads(result.get_data(as_text=True))
        self.assertEqual(user["first_name"], newdata["first_name"])
        self.assertEqual(user["name"], data["name"])
        self.assertEqual(user["email"], newdata["email"])

    def test_delete_user_by_id(self):
        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        url = "/users"

        result = self.app.post(url, data=data)
        self.assertEqual(result.status_code, 200)

        result = json.loads(result.get_data(as_text=True))
        self.assertEqual(result, {"id": 1})

        url = "/users/1"
        result = self.app.delete(url)
        self.assertEqual(result.status_code, 200)

        result = json.loads(result.get_data(as_text=True))
        self.assertIsNone(result)

    def test_delete_user_by_name(self):
        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        url = "/users"

        result = self.app.post(url, data=data)
        self.assertEqual(result.status_code, 200)

        result = json.loads(result.get_data(as_text=True))
        self.assertEqual(result, {"id": 1})

        url = "/users/Doe"
        result = self.app.delete(url)
        self.assertEqual(result.status_code, 200)

        result = json.loads(result.get_data(as_text=True))
        self.assertIsNone(result)



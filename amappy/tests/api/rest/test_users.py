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
        result = self.app.get('/users')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(data, [])

    def test_get_user_empty_db(self):
        url = '/users/{}'
        id_or_name = "user_does_not_exist"
        result = self.app.get(url.format(id_or_name))
        self.assertEqual(result.status_code, 404)


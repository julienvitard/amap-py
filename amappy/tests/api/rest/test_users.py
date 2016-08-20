#! /usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import unittest


class UsersTestCase(unittest.TestCase):

    def setUp(self):
        from amappy.api.rest import app
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_users(self):
        rv = self.app.get('/users')
        print(rv.data)

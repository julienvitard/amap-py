#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestUsersMemoryDB(unittest.TestCase):

    def setUp(self):
        from amappy.persistence.users import UsersMemoryDB
        UsersMemoryDB.reset()

    def test_init_db(self):
        from amappy.persistence.users import UsersMemoryDB
        self.assertEqual(UsersMemoryDB.USERS_BY_ID, {})
        self.assertEqual(UsersMemoryDB.USERS_BY_NAME, {})

    def test_get_id(self):
        from amappy.persistence.users import UsersMemoryDB
        self.assertEqual(UsersMemoryDB.get_id(), 1)

        UsersMemoryDB.USERS_BY_ID = {2: ""}
        self.assertEqual(UsersMemoryDB.get_id(), 3)

        UsersMemoryDB.USERS_BY_ID = {2: "", 5: ""}
        self.assertEqual(UsersMemoryDB.get_id(), 6)

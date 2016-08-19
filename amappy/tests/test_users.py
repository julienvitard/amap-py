#! /usr/bin/env python
# endcoding: utf8

import unittest


class TestUsers(unittest.TestCase):

    def setUp(self):
        from amappy.persistence import UsersDB
        UsersDB.reset()

    def test_get_users(self):
        from amappy.resources.users import get_users
        users = get_users()
        self.assertIsInstance(users, (list, ))
        self.assertEqual(users, [])

    def test_get_user_by_id(self):
        from amappy.resources.users import (
            create_user,
            get_user,
        )

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }

        identifier = create_user(data)
        self.assertIsNotNone(identifier)

        user = get_user(id=identifier)
        self.assertEqual(user["first_name"], data["first_name"])
        self.assertEqual(user["name"], data["name"])
        self.assertEqual(user["email"], data["email"])
        self.assertEqual(user["id"], identifier)

    def test_get_user_by_name(self):
        from amappy.resources.users import (
            create_user,
            get_user,
        )

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }

        identifier = create_user(data)
        self.assertIsNotNone(identifier)

        user = get_user(name=data["name"])
        self.assertEqual(user["first_name"], data["first_name"])
        self.assertEqual(user["name"], data["name"])
        self.assertEqual(user["email"], data["email"])
        self.assertEqual(user["id"], identifier)

    def test_create_user_new(self):
        from amappy.resources.users import (
            create_user,
            get_users,
        )

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }

        identifier = create_user(data)
        self.assertIsNotNone(identifier)

        users = get_users()
        self.assertIsInstance(users, (list, ))
        self.assertEqual(len(users), 1)

    def test_create_user_existing(self):
        from amappy.resources.users import (
            create_user,
        )

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }

        identifier = create_user(data)
        self.assertIsNotNone(identifier)

        data = {
            "name":       "Doe",
            "first_name": "Johnny",
            "email":      "johnny.doe@example.net"
        }

        with self.assertRaises(ValueError):
            identifier = create_user(data)

    def test_update_user_by_id(self):
        from amappy.resources.users import (
            create_user,
            get_user,
            update_user,
        )

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }

        identifier = create_user(data)

        newdata = {
            "first_name": "Jane",
            "email":      "jane.doe@example.net"
        }

        result = update_user(id=identifier, data=newdata)
        self.assertIsNone(result)

        user = get_user(id=identifier)
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], data["name"])
        self.assertEqual(user["first_name"], newdata["first_name"])
        self.assertEqual(user["email"], newdata["email"])
        self.assertEqual(user["id"], identifier)

    def test_update_user_by_name(self):
        from amappy.resources.users import (
            create_user,
            get_user,
            update_user,
        )

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }

        identifier = create_user(data)

        newdata = {
            "first_name": "Jane",
            "email":      "jane.doe@example.net"
        }

        result = update_user(name=data["name"], data=newdata)
        self.assertIsNone(result)

        user = get_user(id=identifier)
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], data["name"])
        self.assertEqual(user["first_name"], newdata["first_name"])
        self.assertEqual(user["email"], newdata["email"])
        self.assertEqual(user["id"], identifier)

    def test_delete_user_by_id(self):
        from amappy.resources.users import (
            create_user,
            get_users,
            delete_user,
        )

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        identifier = create_user(data)
        self.assertIsNotNone(identifier)

        users = get_users()
        self.assertIsInstance(users, (list, ))
        self.assertEqual(len(users), 1)

        result = delete_user(id=1)
        self.assertIsNone(result)

        users = get_users()
        self.assertIsInstance(users, (list, ))
        self.assertEqual(len(users), 0)

    def test_delete_user_by_name(self):
        from amappy.resources.users import (
            create_user,
            get_users,
            delete_user,
        )

        data = {
            "name":       "Doe",
            "first_name": "John",
            "email":      "john.doe@example.net"
        }
        identifier = create_user(data)
        self.assertIsNotNone(identifier)

        users = get_users()
        self.assertIsInstance(users, (list, ))
        self.assertEqual(len(users), 1)

        result = delete_user(name=data["name"])
        self.assertIsNone(result)

        users = get_users()
        self.assertIsInstance(users, (list, ))
        self.assertEqual(len(users), 0)


if __name__ == '__main__':
    unittest.main()

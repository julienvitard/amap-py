#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestInterface(unittest.TestCase):

    def test_persistence_interface(self):
        from amappy.persistence.base import Persistence

        self.assertTrue(getattr(Persistence, "create"))
        with self.assertRaises(NotImplementedError):
            Persistence.create()

        self.assertTrue(getattr(Persistence, "read"))
        with self.assertRaises(NotImplementedError):
            Persistence.read()

        self.assertTrue(getattr(Persistence, "update"))
        with self.assertRaises(NotImplementedError):
            Persistence.update()

        self.assertTrue(getattr(Persistence, "delete"))
        with self.assertRaises(NotImplementedError):
            Persistence.delete()

        self.assertTrue(getattr(Persistence, "reset"))
        with self.assertRaises(NotImplementedError):
            Persistence.reset()


class TestInMemoryDB(unittest.TestCase):
    def test_persistence_inmemorydb(self):
        from amappy.persistence.base import InMemoryDB
        del InMemoryDB

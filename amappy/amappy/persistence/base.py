#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Persistence interface
"""


class Persistence:

    @classmethod
    def create(cls, data=None):
        raise NotImplementedError

    @classmethod
    def read(cls, id=None, name=None):
        raise NotImplementedError

    @classmethod
    def update(cls, id=None, name=None, data=None):
        raise NotImplementedError

    @classmethod
    def delete(cls, id=None, name=None):
        raise NotImplementedError

    @classmethod
    def reset(cls):
        raise NotImplementedError


class InMemoryDB(Persistence):

    def __init__(self):
        pass

    @classmethod
    def create(cls, data=None):
        pass

    @classmethod
    def read(cls, key=None):
        pass

    @classmethod
    def update(cls, key=None, data=None):
        pass

    @classmethod
    def delete(cls, key=None):
        pass

    @classmethod
    def reset(cls):
        pass

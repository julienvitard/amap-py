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

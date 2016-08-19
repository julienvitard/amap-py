#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Persistence interface
"""


class Persistence:

    @classmethod
    def create(cls, user):
        raise NotImplemented

    @classmethod
    def read(cls, id=None, name=None):
        raise NotImplemented

    @classmethod
    def update(cls, id=None, name=None, data=None):
        raise NotImplemented

    @classmethod
    def delete(cls, id=None, name=None):
        raise NotImplemented

    @classmethod
    def reset(cls):
        raise NotImplemented

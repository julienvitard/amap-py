#! /usr/bin/env python
# endcoding: utf8

"""Amapy setup file

* install
* clean

"""

from setuptools import setup, find_packages
from setuptools import Command
from setuptools.command.test import test as TestCommand

import ast
import codecs
import os
import sys


class Clean(Command):
    """Customized cleaning command.

    Get rid of every temporary directories and files.
    """

    description = "run clean command"
    user_options = []

    def initialize_options(self):
        """init options"""
        self.to_remove = (
            "*.pyc", "*.pyo", "__pycache__", "./build", "./dist",
            "./*.egg-info/", "./docs/build/*",
            # "*.eggs",  # contains dowloaded packages for tests (saves time)
        )

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        os.system("rm -rf %(to_remove)s" % {
            "to_remove": " ".join(self.to_remove)
        })


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


class VersionFinder(ast.NodeVisitor):
    def __init__(self):
        self.data = {}

    def visit_Assign(self, node):
        targets = (
            '__version__', '__package_name__', '__author__',
            '__author_email__', '__url__'
        )
        if node.targets[0].id in targets:
            self.data[node.targets[0].id.strip("_")] = node.value.s


def read(*path_parts):
    filename = os.path.join(os.path.dirname(__file__), *path_parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_infos(*path_parts):
    finder = VersionFinder()
    node = ast.parse(read(*path_parts))
    docstring = ast.get_docstring(node)
    finder.visit(node)
    finder.data["description"] = docstring
    return finder.data


infos = find_infos('amapy/amapy', '__init__.py')
excluded_tests = ("*.tests", "*.tests.*", "tests.*", "tests", )

data = {
    "name":                 infos.get("package_name"),
    "version":              infos.get("version"),
    "package_dir":          {
        'amapy': 'amapy/amapy'
    },
    "packages":             find_packages("amapy", exclude=excluded_tests),
    "include_package_data": True,
    "description":          infos.get("description"),
    "long_description":     read('README.rst'),
    "url":                  infos.get("url"),
    "author":               infos.get("author"),
    "author_email":         infos.get("author_email"),
    "zip_safe":             False,
    "install_requires":     [],
    "tests_require":        [
        'pytest-cov',
        'pytest',      # need to be after packages which need it
    ],
    "cmdclass":             {
        "clean": Clean,
        "test":  PyTest,
    }
}

setup(**data)

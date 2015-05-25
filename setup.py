#! /usr/bin/env python
# endcoding: utf8

"""Amapy setup file

* install
* clean
* test

"""

from setuptools import setup, find_packages
from setuptools import Command
from setuptools.command.test import test as TestCommand


import ast
import codecs
import os
import sys

package = "amapy"


class Clean(Command):
    """Customized cleaning command.
    Get rid of every temporary directories and files.
    """

    description = "run clean command"
    user_options = []

    def initialize_options(self):
        """init options"""
        self.to_remove = (
            "./*/**/*.pyc", "./*/**/*.pyo", "./*/**/__pycache__", "./build",
            "./dist", "./*.egg-info/", "./docs/build/*",
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
    user_options = [
        ("verbose", 'v', "increase verbosity"),
        ("with-coverage", None, "show code coverage"),
        ("with-xml-coverage=", None, "produce coverage xml file"),
        ("with-xml-junit=", None, "produce junit xml file"),
    ]

    def initialize_options(self):
        self.distribution.verbose = 0
        TestCommand.initialize_options(self)
        self.verbose = 0
        self.with_coverage = None
        self.with_xml_coverage = None
        self.with_xml_junit = None
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

        if self.verbose:
            self.pytest_args.append("--verbose")

        if self.with_coverage:
            self.pytest_args.extend(["--cov-report", "term-missing"])
            self.pytest_args.extend(["--cov", package])

            if self.with_xml_coverage:
                self.pytest_args.extend(["--cov-report", "xml"])

        if self.with_xml_junit:
            self.pytest_args.extend(["--junitxml=", self.with_xml_junit])

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.pytest_args)

        if self.with_xml_coverage and not errno:
            coverage_path = os.path.abspath("./coverage.xml")
            if os.path.exists(coverage_path):
                os.rename(coverage_path, self.with_xml_coverage)

        sys.exit(errno)


class VersionFinder(ast.NodeVisitor):
    def __init__(self):
        self.data = {}

    def visit_Assign(self, node):
        targets = ("__version__", "__author__", "__author_email__", "__url__")
        if node.targets[0].id in targets:
            self.data[node.targets[0].id.strip("_")] = node.value.s


def read(*path_parts):
    filename = os.path.join(os.path.dirname(__file__), *path_parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


def find_infos(*path_parts):
    finder = VersionFinder()
    node = ast.parse(read(*path_parts))
    docstring = ast.get_docstring(node)
    finder.visit(node)
    finder.data["description"] = docstring
    return finder.data


infos = find_infos(
    '%(package)s/%(package)s' % {"package": package},
    '__init__.py',
)

excluded_tests = ("*.tests", "*.tests.*", "tests.*", "tests", )

data = {
    "name":                 package,
    "version":              infos.get("version"),
    "package_dir":          {
        package: '%(package)s/%(package)s' % {"package": package}
    },
    "packages":             find_packages(package, exclude=excluded_tests),
    "include_package_data": True,
    "description":          infos.get("description"),
    "long_description":     read('README.rst'),
    "url":                  infos.get("url"),
    "author":               infos.get("author"),
    "author_email":         infos.get("author_email"),
    "zip_safe":             False,
    "install_requires":     [],
    "tests_require":        [
        "pytest-cov",
        "pytest",      # need to be after packages which need it
    ],
    "cmdclass":             {
        "clean": Clean,
        "test":  PyTest,
    }
}

setup(**data)

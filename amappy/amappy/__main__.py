#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""REST API launcher
"""

import os
import sys


def main():
    """The main routine."""
    from amappy.api.rest import app
    app.run()


if __name__ == "__main__":
    main()
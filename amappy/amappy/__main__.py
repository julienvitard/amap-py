#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""REST API launcher
"""

import argparse
import os
import sys


def main(args):
    """The main routine."""
    from amappy.api.rest import app
    app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='amappy REST API launcher'
    )
    parser.add_argument(
        '--host', metavar='HOST', type=str, default="127.0.0.1",
        help='host ip to connect to'
    )
    parser.add_argument(
        '--port', dest='port', type=int, default=8000,
        help='port to connect to'
    )

    args = parser.parse_args()
    main(args)
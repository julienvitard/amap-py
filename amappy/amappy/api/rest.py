#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""REST API
"""

from flask import abort
from flask import Flask

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_users():
    import json
    from amappy.resources.users import get_users
    return json.dumps(get_users())


@app.route("/users/<id_or_name>", methods=["GET"])
def get_user(id_or_name=None):
    import json
    from amappy.resources.users import get_user
    key = "id" if isinstance(id_or_name, (int, )) else "name"
    users = get_user(**{key: id_or_name})

    if users is None:
        abort(404)

    return json.dumps(users)


@app.route("/users", methods=["POST"])
def create_user(id_or_name=None, data=None):
    return ""


@app.route("/users/<id_or_name>", methods=["PUT"])
def update_user(id_or_name=None, data=None):
    return ""


@app.route("/users/<id_or_name>", methods=["DELETE"])
def delete_user(id_or_name=None):
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0")

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""REST API
"""

from flask import abort
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_users():
    from amappy.resources.users import get_users
    return jsonify(get_users())


@app.route("/users/<id_or_name>", methods=["GET"])
def get_user(id_or_name=None):
    from amappy.resources.users import get_user
    users = get_user(id_or_name)
    if users is None:
        abort(404)
    return jsonify(users)


@app.route("/users", methods=["POST"])
def create_user(data=None):
    from amappy.resources.users import create_user
    from flask import request
    data = dict((key, request.form.get(key)) for key in request.form.keys())
    identifier = create_user(data=data)
    return jsonify({"id": identifier})


@app.route("/users/<id_or_name>", methods=["PUT"])
def update_user(id_or_name=None, data=None):
    from amappy.resources.users import update_user
    from flask import request
    data = dict((key, request.form.get(key)) for key in request.form.keys())
    user = update_user(id_or_name=id_or_name, data=data)
    return jsonify(user)


@app.route("/users/<id_or_name>", methods=["DELETE"])
def delete_user(id_or_name=None):
    from amappy.resources.users import delete_user
    result = delete_user(id_or_name=id_or_name)
    return jsonify(result)

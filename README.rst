.. |Amappy| replace:: **Amappy**


Amappy
======

.. image:: https://travis-ci.org/julienvitard/amappy.svg?branch=master
    :target: https://travis-ci.org/julienvitard/amappy
.. image:: https://coveralls.io/repos/github/julienvitard/amappy/badge.png?branch=master
    :target: https://coveralls.io/github/julienvitard/amappy?branch=master

    
|Amappy| is a tool with the ambition to manage your AMAP, easily.


Features
--------

* Open source tools
* REST based api, simple and accessible to anyone (developers and programs)
* users management (users, distributors, supervisors, ...)


Usage
-----

Prepare your environment::

   $ workon amappy
   $(amappy) cd amappy
   $(amappy) pip install -r requirements/test.txt
   $(amappy) python setup.py install


Launch REST API::

   $(amappy) python -m amappy
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

   or

   $(amappy) python -m amappy --host 0.0.0.0 --port 8000
   * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)


Examples:

* retrieve users::

   # GET /users:

   $ curl -k http://127.0.0.1:5000/users
   []

* create user::

   # POST /users:

   $ curl -k -X POST http://127.0.0.1:8000/users --data "firstname=John&name=Doe&email=john.doe@test.com"
   {
     "id": 1
   }

* retrieve user by id "1"::

   # GET /users/{id}:

   $ curl -k -X GET http://127.0.0.1:8000/users/1
   {
     "creation_date": "Sun, 04 Sep 2016 07:35:34 GMT",
     "firstname": "John",
     "name": "Doe"
     "email": "john.doe@test.com",
     "id": 1,
   }

* retrieve user by name "Doe"::

   # GET /users/{name}:

   $ curl -k -X GET http://127.0.0.1:8000/users/Doe
   {
     "creation_date": "Sun, 04 Sep 2016 07:35:34 GMT",
     "firstname": "John",
     "name": "Doe"
     "email": "john.doe@test.com",
     "id": 1,
   }


* modify user by id "1"::

   # PUT /users/{id}:

   $ curl -k -X PUT http://127.0.0.1:8000/users/1 -d email=jane.doe@test.com -d firstname=Jane
   {
     "creation_date": "Sun, 04 Sep 2016 07:35:34 GMT",
     "firstname": "John",
     "name": "Doe"
     "email": "john.doe@test.com",
     "id": 1,
   }

* modify user by name "Doe"::

   # PUT /users/{name}:

   $ curl -k -X PUT http://127.0.0.1:8000/users/Doe -d email=jany.doe@test.com -d firstname=Jany
   {
     "creation_date": "Sun, 04 Sep 2016 07:35:34 GMT",
     "firstname": "John",
     "name": "Doe"
     "email": "john.doe@test.com",
     "id": 1,
   }

.. Note::

   at the moment, there is no enforcement for the fields.

* delete user by id "1"::

   # DELETE /users/{id}:

   $ curl -k -X DELETE http://127.0.0.1:8000/users/1
   null

* delete user by name "Doe"::

   # DELETE /users/{name}:

   $ curl -k -X DELETE http://127.0.0.1:8000/users/Doe
   null

.. Note::

   at the moment, there is no enforcement for the fields.


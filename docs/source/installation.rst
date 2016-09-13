Installation
============

The simpler way to install ``amappy`` is inside a virtual environment:

.. code:: console

   $ mkvirtualenv -p /usr/bin/python3.5 amappy
   $(amappy) pip install -r requirements/test.txt




Managing the ``SECRET_KEY``:

.. code:: console

   $(amappy) export SECRET_KEY=$(cat amappy/SECRET_KEY)
   $(amappy) echo $SECRET_KEY


Running in ``debug`` mode:

.. code:: console

   $(amappy) export DEBUG=True
   $(amappy) cd amappy
   $(amappy) python manage.py runserver 127.0.0.1:8000
   Django-Debug-Toolbar installed
   Django-Debug-Toolbar installed
   Performing system checks...

   System check identified no issues (0 silenced).
   January 05, 2016 - 21:58:45
   Django version 1.9.1, using settings 'amappy.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.


Testing REST API with curl:

.. code:: console

   $(amappy) curl -i -X GET "Content-type: application/json" http://127.0.0.1:8000/curl -i -X GET "Content-type: application/json" http://127.0.0.1:8000/
   curl: (6) Could not resolve host: Content-type
   HTTP/1.0 200 OK
   Date: Tue, 05 Jan 2016 22:12:26 GMT
   Server: WSGIServer/0.2 CPython/3.5.0
   X-Frame-Options: SAMEORIGIN
   Vary: Accept, Cookie
   Content-Type: application/json
   Allow: GET, HEAD, OPTIONS

   {
       "users":"http://127.0.0.1:8000/users/",
       "distributors":"http://127.0.0.1:8000/distributors/",
       "supervisors":"http://127.0.0.1:8000/supervisors/"
   }


Building the documentation:

.. code:: console

   $(amappy) make -f Makefile html
   sphinx-build -b html -d build/doctrees   source build/html
   Running Sphinx v1.3.3
   loading pickled environment... done
   building [mo]: targets for 0 po files that are out of date
   building [html]: targets for 1 source files that are out of date
   updating environment: 0 added, 1 changed, 0 removed
   reading sources... [100%] installation

   looking for now-outdated files... none found
   pickling environment... done
   checking consistency... done
   preparing documents... done
   writing output... [100%] installation

   generating indices... genindex
   writing additional pages... search
   copying static files... done
   copying extra files... done
   dumping search index in English (code: en) ... done
   dumping object inventory... done
   build succeeded.

   Build finished. The HTML pages are in build/html.


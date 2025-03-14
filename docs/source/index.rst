.. GatorGuide documentation master file, created by
   sphinx-quickstart on Wed Feb 12 19:24:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GatorGuide documentation
========================

An app for building your UF Schedule!


Intro
=====

This project heavily utilizes SQLModel and SQL in general, but ideally (through the :class:`.DB_Engine` class) you should have all of that fully obfuscated!!

Users of this (which should primarily be the backend of the project) should instantiate one (1) object of the class :class:`.DB_Engine` class (having several within one program may lead to concurrency issues).

If there are things you would like from this object that do not yet exist, add a git issue (or solve it yourself if you want to join as a maintainer).

This project is very much open source, and we support, appreciate, and ask for anyone to provide their skills on this project!!!


Environment
===========

.. important::
   Must have Python and Node/NPM installed!!!

Install python dependencies

.. code-block:: bash

   python -m venv .venv
   ./.venv/Scipts/Activate
   pip install -e ./backend

.. important::

   If you are building the docs, don't forget to ``pip install -r requirements.dev.txt``!!!!

Install Node dependencies

.. code-block:: bash

   cd frontend
   npm install .

Environment files
   - Create a .env file in ``/frontend``
      - VITE_API_HOST={full_url_to_backend}

Building
========

Build the DB

.. code-block:: bash

   cd backend/src/GatorGuide/database
   python build_db.py

Build the frontend

.. code-block:: bash

   cd frontend
   npm run build

Build the docs

.. code-block:: bash

   cd backend/docs
   ./make.bat html

.. important::

   This will create an ``index.html`` file in the ``docs/build`` directory, serve this!!

Running
=======

++++++++
Dev Mode
++++++++

Start frontend server

.. code-block:: bash

   cd frontend
   npm run start

Start backend server

.. code-block:: bash

   ./.venv/scripts/Activate
   cd backend/src/GatorGuide/api
   fastapi dev --port {port} main.py

+++++++++++++++
Production Mode
+++++++++++++++

.. code-block:: bash

   ./.venv/scripts/Activate
   cd backend/src/GatorGuide/api
   fastapi run --port {port} main.py

Usage
=====

The items in this database are pydantic models, this provides a lot of functionality but most will not be needed.

- Use the :class:`.DB_Engine` to read the Courses/Major

   - Or create your own the same way you would a normal object

- Use these objects as you would normally

- When done working with them, save them with :meth:`.DB_Engine.write()`

   - Or delete them with :meth:`.DB_Engine.delete()`

.. note::

   You can use the ``.model_dump()`` method provided by pydantic to convert any of these DB objects to JSON

.. toctree::
   :maxdepth: 1
   :caption: Guides

   api_usage

.. toctree::
   :maxdepth: 2
   :caption: Classes

   models
   db_engine
   exceptions
   todo

.. toctree::
   :maxdepth: 2
   :caption: Endpoints

   user_endpoints
   major_endpoints
   course_endpoints

.. toctree::
   :caption: Libraries

   SQLModel <https://sqlmodel.tiangolo.com/>



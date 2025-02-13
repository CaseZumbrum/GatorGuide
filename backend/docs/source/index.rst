.. GatorGuide documentation master file, created by
   sphinx-quickstart on Wed Feb 12 19:24:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GatorGuide documentation
========================

An app for building your UF Schedule!

Quickstart
==========

Build Instructions

.. code-block:: bash

   cd backend
   python -m venv .venv
   ./.venv/Scipts/Activate
   pip install -e .

Intro
=====

This project heavily utilizes SQLModel and SQL in general, but ideally (through the :class:`.DB_Engine` class) you should have all of that fully obfuscated!!

Users of this (which should primarily be the backend of the project) should instantiate one (1) object of the class :class:`.DB_Engine` class (having several within one program may lead to concurrency issues).

If there are things you would like from this object that do not yet exist, add a git issue (or solve it yourself if you want to join as a maintainer).

This project is very much open source, and we support, appreciate, and ask for anyone to provide their skills on this project!!!

.. toctree::
   :maxdepth: 2
   :caption: Classes

   models
   db_engine

.. toctree::
   :caption: Libraries

   SQLModel <https://sqlmodel.tiangolo.com/>



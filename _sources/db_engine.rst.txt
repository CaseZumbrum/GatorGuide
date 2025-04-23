.. GatorGuide documentation master file, created by
   sphinx-quickstart on Wed Feb 12 19:24:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DB_Engine
========================

Use the DB_Engine to perform CRUD operations on the database

Create a DB_Engine with something like:

.. code-block:: python

   sqlite_file_name = Path(__file__).parent.resolve().joinpath("./testing_database.db")
   e = DB_Engine(sqlite_file_name)

This object shold be a singleton (you should not have several instances of it to avoid concurrency issues)

You will mainly use the :meth:`.read_course` and :meth:`.read_major` to get data from the DB (your Read operations).

.. important::
   These functions return Objects that represent the items, changes to these objects will not be represented in the Database until you use the :meth:`.write` method


To handle Deletion, use the :meth:`.delete` method, which takes in any of the objects the DB contains and removes them!

To handle Create or Update operations, use the :meth:`.write` method, which takes in an Object and will write it to the DB.

Example run for writing!!!

.. code-block:: python

   # This is a format I use to guarentee relative paths!!!
   sqlite_file_name = Path(__file__).parent.resolve().joinpath("./testing_database.db")

   e = DB_Engine(sqlite_file_name)

   # Create a Major object
    cpe = Major(
        name="Computer Engineering",
    )
    # Create a RequiredGroup, this will be for technical electives
    g = RequiredGroup(name="tech electives", credits=16)

   # Regex matching for all COP 3000 level (not including COP3520) and MHF 4000 level
    e.add_to_group(g, "^(?!.*(COP3520)).*^(COP3|MHF4)")

    # add tech electives to the CPE major
    cpe.groups.append(g)

   # Write CPE to the database (this will automatically write the Tech Electives group)
    e.write(cpe)

Example run for reading/updating

.. code-block:: python

   # This is a format I use to guarentee relative paths!!!
   sqlite_file_name = Path(__file__).parent.resolve().joinpath("./testing_database.db")

   e = DB_Engine(sqlite_file_name)

   # Read the CPE major from the DB
   cpe = e.read_major(name="Computer Engineering")

    # Read the DSA course from the DB
   DSA = e.read_course(code="COP3530")

   cpe.critical_tracking.append(DSA)

   # Write CPE to the database (this will update it to have DSA as a critical tracking course)
    e.write(cpe)

.. automodule:: GatorGuide.database.db_engine
   :members:



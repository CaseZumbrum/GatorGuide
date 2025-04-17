.. GatorGuide documentation master file, created by
   sphinx-quickstart on Wed Feb 12 19:24:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

api_usage
===========================

Here's some tips for development of using the GatorGuide API


+++++++++++++++++++
Important Endpoints
+++++++++++++++++++

* /users/{username}/login?password=
   Primary login endpoint, if you username and password match, a GatorGuide_Session cookie is set, this cookie is used by other Endpoints

   .. important::

      This cookie is only good for 24 hrs

* /users/{username}/me
   Once logged in, this returns the :class:`.User` object associated with the logged in user





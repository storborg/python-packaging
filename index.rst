How To Package Your Python Code
===============================

This tutorial aims to clarify the current state of Python packaging, and put forth an opinionated and specific pattern to make trouble-free packages for community use. The documentation herein doesn't describe the *only* way of doing things, merely one specific approach that works well.

In particular, those packages should make it easy:

* To install with ``pip`` or ``easy_install``.
* To specify as a dependency for another package.
* For other users to download and run tests.
* For other users to work on and have immediate familiary with the basic directory strucuture.
* To add and distribute documentation.

We'll walk through the basic steps of building up a contrived package **funniest** to support these things.

.. toctree::
   :maxdepth: 1

   minimal
   dependencies
   metadata
   testing
   command-line-scripts
   non-code-files
   documentation
   everything
   about

.. note::

   At this time, this documentation focuses on Python 2.x only, and may not be *as* applicable to packages targeted to Python 3.x.


Indices
=======

* :ref:`genindex`
* :ref:`search`

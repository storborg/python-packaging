Minimal Structure
=================

We'll start with some Python code. Native German speakers, `please proceed with caution <http://www.youtube.com/watch?v=ienp4J3pW7U>`_::

    def joke():
        return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
                u'Beiherhund das Oder die Flipperwaldt gersput.')

The beauty and elegance of this implementation simply demands that it be packaged properly for distribution.


Picking A Name
~~~~~~~~~~~~~~

Python module/package names should generally follow the following constraints:

* All lowercase
* Unique on pypi, even if you don't want to make your package publicly available (you might want to specify it privately as a dependency later)
* Underscore-separated or no word separators at all (don't use hyphens)

We've decided to turn our bit of code into a module called **funniest**.


Creating The Scaffolding
~~~~~~~~~~~~~~~~~~~~~~~~

The initial directory structure for **funniest** should look like this::

    funniest/
        funniest/
            __init__.py
        setup.py

The top level directory is the root of our SCM repo, e.g. ``funniest.git``. The subdir, also called ``funniest``, is the actual Python module.

For starters we'll put the ``joke()`` function in ``__init__.py``, so it just contains::

    def joke():
        return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
                u'Beiherhund das Oder die Flipperwaldt gersput.')

The main setup config file, ``setup.py``, should contain a single call to ``setuptools.setup()``, like so::

    from setuptools import setup

    setup(name='funniest',
          version='0.1',
          description='The funniest joke in the world',
          url='http://github.com/storborg/funniest',
          author='Flying Circus',
          author_email='flyingcircus@example.com',
          license='MIT',
          packages=['funniest'],
          zip_safe=False)

Now we can install the package locally (for use on our system), with::

    $ pip install .

We can also install the package with a symlink, so that changes to the source files will be immediately available to other users of the package on our system::

    $ pip install -e .

Anywhere else in our system using the same Python, we can do this now::

    >>> import funniest
    >>> print funniest.joke()


Publishing On PyPI
~~~~~~~~~~~~~~~~~~

The ``setup.py`` script is also our main entrypoint to register the package name on PyPI and upload source distributions.

Create an account
-----------------

First, you need a :term:`PyPI <Python Package Index (PyPI)>` user
account. There are two options:

1. Create an account manually `using the form on the PyPI website
   <https://pypi.python.org/pypi?%3Aaction=register_form>`_.

2. **(Not recommended):** Have an account created as part of
   registering your first project (not recommended due to the
   related security concerns.).

To "register" the package (this will reserve the name, upload package metadata, and create the pypi.python.org webpage) there are three methods::

1. Use `the form on the PyPI website
   <https://pypi.python.org/pypi?%3Aaction=submit_form>`_, to upload your
   ``PKG-INFO`` info located in your local project tree at
   ``myproject.egg-info/PKG-INFO``.  If you don't have that file or directory,
   then run ``python setup.py egg_info`` to have it generated.
2. Run ``twine register dist/mypkg.whl``, and :ref:`twine` will register your project
   based on the package metadata in the specified files. Your ``~/.pypirc``
   must already be appropriately configured for twine to work. You will also need to have twine installed.
   You can install twine by running ``pip install twine``
3. **(Not recommended):** Run ``python setup.py register``.  If you don't have
   a user account already, a wizard will create one for you. This approach is
   covered here due to it being mentioned in other guides, but it is not
   recommended as it may use a plaintext HTTP or unverified HTTPS connection
   on some Python versions, allowing your username and password to be intercepted
   during transmission.


At this point you can view the (very minimal) page on PyPI describing **funniest**:

http://pypi.python.org/pypi/funniest/0.1

Although users can follow the URL link to find our git repository, we'll probably want to upload a source distribution so that the package can be installed without cloning the repository. This will also enable automated installation and dependency resolution tools to install our package.

First create a source distribution with::

    $ python setup.py sdist

This will create ``dist/funniest-0.1.tar.gz`` inside our top-level directory. If you like, copy that file to another host and try unpacking it and install it, just to verify that it works for you.

That file can then be uploaded to PyPI using one of the two options::

1. Use :ref:`twine`

   ::

     twine upload dist/*

   The biggest reason to use twine is that ``python setup.py upload`` (option #2
   below) uploads files over plaintext. This means anytime you use it you expose
   your username and password to a MITM attack. Twine uses only verified TLS to
   upload to PyPI in order to protect your credentials from theft.

   Secondly it allows you to precreate your distribution files.  ``python
   setup.py upload`` only allows you to upload something that you've created in
   the same command invocation. This means that you cannot test the exact file
   you're going to upload to PyPI to ensure that it works before uploading it.

   Finally it allows you to pre-sign your files and pass the .asc files into the
   command line invocation (``twine upload twine-1.0.1.tar.gz
   twine-1.0.1.tar.gz.asc``). This enables you to be assured that you're typing
   your gpg passphrase into gpg itself and not anything else since *you* will be
   the one directly executing ``gpg --detach-sign -a <filename>``.


2. **(Not recommended):** Use :ref:`setuptools`:

   ::

    python setup.py bdist_wheel sdist upload

   This approach is covered here due to it being mentioned in other guides, but it
   is not recommended as it may use a plaintext HTTP or unverified HTTPS connection
   on some Python versions, allowing your username and password to be intercepted
   during transmission.


For a detailed list of all available setup.py commands, do::

    $ python setup.py --help-commands


Installing the Package
~~~~~~~~~~~~~~~~~~~~~~

At this point, other consumers of this package can install the package with ``pip``::

    $ pip install funniest

They can specify it as a dependency for another package, and it will be automatically installed when that package is installed (we'll get to how to do that later).


Adding Additional Files
~~~~~~~~~~~~~~~~~~~~~~~

Most of the time we'll want more than one file containing code inside of our module. Additional files should always be added inside the inner ``funniest`` directory.

For example, let's move our one function to a new ``text`` submodule, so our directory hierarchy looks like this::

    funniest/
        funniest/
            __init__.py
            text.py
        setup.py

In ``__init__.py``::

    from .text import joke

In ``text.py``::

    def joke():
        return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
                u'Beiherhund das Oder die Flipperwaldt gersput.')

All additional Python code belongs in the ``funniest/funniest/`` directory.


Ignoring Files (.gitignore, etc)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There's one more thing we'll probably want in a 'bare bones' package: a ``.gitignore`` file, or the equivalent for other SCMs. The Python build system creates a number of intermediary files we'll want to be careful to not commit to source control. Here's an example of what ``.gitignore`` should look like for **funniest**::

    # Compiled python modules.
    *.pyc

    # Setuptools distribution folder.
    /dist/

    # Python egg metadata, regenerated from source files by setuptools.
    /*.egg-info


That's All You Need
~~~~~~~~~~~~~~~~~~~

The structure described so far is all that's necessary to create reusable simple packages with no 'packaging bugs'. If every published Python tool or library used followed these rules, the world would be a better place.

**But wait, there's more!** Most packages will want to add things like command line scripts, documentation, tests, and analysis tools. Read on for more.

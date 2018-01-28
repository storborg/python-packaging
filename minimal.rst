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


We'll probably want to upload a source distribution so that the package can be installed without cloning the repository. This will also enable automated installation and dependency resolution tools to install our package.

First create a source distribution with the setup.py command::

    $ python setup.py sdist
    running sdist
        ...
    Writing funniest-0.1/setup.cfg
    Creating tar archive

This will create ``dist/funniest-0.1.tar.gz`` inside our top-level directory. If you like, copy that file to another host and try unpacking it and install it, just to verify that it works for you. The s in sdist is for ‘source’. You can also create pre-built wheels by using bdist, for more information about those, see PyPA’s page on packaging.

We can see in the run output that our package has been built.

Now that we have our built package, we can proceed to upload our code. PyPA recommends using Twine rather than setup.py commands, as setup.py may transmit your passwords in plaintext. So we will need to install Twine.
    
    $ pip install twine

After Twine is installed, we can open the Terminal (Alt+F12) and run

    $ twine upload dist/*

This will reserve the name, upload package metadata, and create the pypi.python.org webpage.

The ``setup.py`` script is also our main entrypoint to register the package name on PyPI and upload source distributions.

[Warning: the ``python setup.py`` method might not work anymore and if it does, might be less secure. Just make an account online.]
The other way to "register" the package ()::

    $ python setup.py register

If you haven't published things on PyPI before, you'll need to create an account by following the steps provided at this point.


At this point you can view the (very minimal) page on PyPI describing **funniest**:

http://pypi.python.org/pypi/funniest/0.1


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

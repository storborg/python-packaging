Command Line Scripts
====================

Many Python packages include command line tools. This is useful for distributing support tools which are associated with a library, or just taking advantage of the setuptools / PyPI infrastructure to distribute a command line tool that happens to use Python.

For **funniest**, we'll add a ``funniest-joke`` command line tool.

There are two mechanisms that ``setuptools.setup()`` provides to do this: the ``scripts`` keyword argument, and the ``console_scripts`` entry point.

The ``scripts`` Keyword Argument
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first approach is to write your script in a separate file, such as you might write a shell script.::

    funniest/
        funniest/
            __init__.py
            ...
        setup.py
        bin/
            funniest-joke
        ...

The ``funniest-joke`` script just looks like this::

    #!/usr/bin/env python

    import funniest
    print funniest.joke()

Then we can declare the script in ``setup()`` like this::

    setup(
        ...
        scripts=['bin/funniest-joke'],
        ...
    )

When we install the package, setuptools will copy the script to our PATH and make it available for general use.::

    $ funniest-joke

This has advantage of being generalizeable to non-python scripts, as well: ``funniset-joke`` could be a shell script, or something completely different.


The ``console_scripts`` Entry Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The second approach is called an 'entry point'. Setuptools allows modules to register entrypoints which other packages can hook into to provide certain functionality. It also provides a few itself, including the ``console_scripts`` entry point.

This allows Python *functions* (not scripts!) to be directly registered as command-line accessible tools.

In this case, we'll add a new file and function to support the command line tool::

    funniest/
        funniest/
            __init__.py
            command_line.py
            ...
        setup.py
        ...

The ``command_line.py`` submodule exists only to service the command line tool (which is a convenient organization method)::

    import funniest

    def main():
        print funniest.joke()

You can test the "script" by running it directly, e.g.::

    $ python
    >>> import funniest.command_line
    >>> funniest.command_line.main()
    ...

The ``main()`` function can then be registered like so::

    setup(
        ...
        entry_points = {
            'console_scripts': ['funniest-joke=funniest.command_line:main'],
        }
        ...
    )

Again, once the package has been installed, we can use it in the same way. Setuptools will generate a standalone script 'shim' which imports your module and calls the registered function.

This method has the advantage that it's very easily testable. Instead of having to shell out to spawn the script, we can have a test case that just does something like::

    from unittest import TestCase
    from funniest.command_line import main

    class TestConsole(TestCase):
        def test_basic(self):
            main()

In order to make that more useful, we'll probably want something like a context manager which temporarily captures ``sys.stdout``, but that is outside the scope of this tutorial.

Let There Be Tests
------------------

The **funniest** package needs some tests. These should be placed in a submodule of ``funniest.`` so that they can be imported, but won't pollute the global namespace.::

    funniest/
        funniest/
            __init__.py
            tests/
                __init__.py
                test_joke.py
        setup.py
        ...

The ``test_joke.py`` file is our first test file. Although it's overkill for now, we'll use a ``unittest.TestCase`` subclass to provide infrastructure for later development.::

    from unittest import TestCase

    import funniest

    class TestJoke(TestCase):
        def test_is_string(self):
            s = funniest.joke()
            self.assertTrue(isinstance(s, basestring))

The best way to get these tests going (particularly if you're not sure what to use) is `Nose <https://nose.readthedocs.org/en/latest/>`_. With those files added, it's just a matter of running this from the root of the repository::

    $ pip install nose
    $ nosetests

To integrate this with our ``setup.py``, and ensure that Nose is installed when we run the tests, we'll add a few lines to ``setup()``::

    setup(
        ...
        test_suite='nose.collector',
        tests_require=['nose'],
    )

Then, to run tests, we can simply do::

    $ python setup.py test

Setuptools will take care of installing nose and running the test suite.

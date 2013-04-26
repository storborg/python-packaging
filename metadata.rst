.. This document is licensed under `CC-BY-SA <http://creativecommons.org/licenses/by-sa/3.0/>`
.. (C) 2013, Scott Torberg

Better Package Metadata
=======================

The ``setuptools.setup()`` call accepts a variety of keyword arguments to specify additional metadata about your package. This can help people find your package and evaluate quickly whether or not it is what they're looking for.::

    from setuptools import setup

    setup(name='funniest',
          version='0.1',
          description='The funniest joke in the world',
          long_description='Really, the funniest around.',
          classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Text Processing :: Linguistic',
          ],
          keywords='funniest joke comedy flying circus',
          url='http://github.com/storborg/funniest',
          author='Flying Circus',
          author_email='flyingcircus@example.com',
          license='MIT',
          packages=['funniest'],
          install_requires=[
              'markdown',
          ],
          zip_safe=False)

For a full list of the possible arguments to ``classifiers``, visit http://pypi.python.org/pypi?%3Aaction=list_classifiers.


A README / Long Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You'll probably want a README file in your source distribution, and that file can serve double purpose as the ``long_description`` specified to PyPI. Further, if that file is written in reStructuredText, it can be formatted nicely.

For **funniest**, let's add two files::

    funniest/
        funniest/
            __init__.py
        setup.py
        README.rst
        MANIFEST.in

``README.rst`` contains::

    Funniest
    --------

    To use (with caution), simply do::

        >>> import funniest
        >>> print funniest.joke()

``MANIFEST.in`` contains::

    include README.rst

This file is necessary to tell setuptools to include the README.rst file when generating source distributions. Otherwise, only Python files will be included.

Now we can use it in setup.py like::

    from setuptools import setup

    def readme():
        with open('README.rst') as f:
            return f.read()

    setup(name='funniest',
          version='0.1',
          description='The funniest joke in the world',
          long_description=readme(),
          classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Text Processing :: Linguistic',
          ],
          keywords='funniest joke comedy flying circus',
          url='http://github.com/storborg/funniest',
          author='Flying Circus',
          author_email='flyingcircus@example.com',
          license='MIT',
          packages=['funniest'],
          install_requires=[
              'markdown',
          ],
          zip_safe=False)

When the repo is hosted on GitHub or BitBucket, the README.rst file will also automatically be picked up and used as a 'homepage' for the project.

Specifying Dependencies
=======================

If you're using Python, odds are you're going to want to use other public packages from PyPI or elsewhere.

Fortunately, setuptools makes it easy for us to specify those dependencies (assuming they are packaged correctly) and automatically install them when our packages is installed.

We can add some formatting spice to the **funniest** joke with `Markdown <http://pypi.python.org/pypi/Markdown/>`_.

In ``text.py``::

    from markdown import markdown

    def joke():
        return markdown(u'Wenn ist das Nunst\u00fcck git und Slotermeyer?'
                        u'Ja! ... **Beiherhund** das Oder die Flipperwaldt '
                        u'gersput.')

Now our package depends on the ``markdown`` package. To note that in ``setup.py``, we just add an ``install_requires`` keyword argument::

    from setuptools import setup

    setup(name='funniest',
          version='0.1',
          description='The funniest joke in the world',
          url='http://github.com/storborg/funniest',
          author='Flying Circus',
          author_email='flyingcircus@example.com',
          license='MIT',
          packages=['funniest'],
          install_requires=[
              'markdown',
          ],
          zip_safe=False)

To prove this works, we can run ``python setup.py develop`` again, and we'll see::

    $ python setup.py develop
    running develop
    running egg_info
    writing requirements to funniest.egg-info/requires.txt
    writing funniest.egg-info/PKG-INFO
    writing top-level names to funniest.egg-info/top_level.txt
    writing dependency_links to funniest.egg-info/dependency_links.txt
    reading manifest file 'funniest.egg-info/SOURCES.txt'
    writing manifest file 'funniest.egg-info/SOURCES.txt'
    running build_ext
    Creating /.../site-packages/funniest.egg-link (link to .)
    funniest 0.1 is already the active version in easy-install.pth

    Installed /Users/scott/local/funniest
    Processing dependencies for funniest==0.1
    Searching for Markdown==2.1.1
    Best match: Markdown 2.1.1
    Adding Markdown 2.1.1 to easy-install.pth file

    Using /.../site-packages
    Finished processing dependencies for funniest==0.1

When we publish this to PyPI, calling ``pip install funniest`` or similar will also install ``markdown``.


Packages Not On PyPI
~~~~~~~~~~~~~~~~~~~~
Sometimes you'll want to use packages that are properly arranged with setuptools, but aren't published to PyPI. In those cases, if you have pip version>=19.1, you can specify url of package in install_requires in PEP 508 format.

For example, if a library is published on GitHub, you can specify it like::

    setup(
        ...
        install_requires=['package @ git+https://github.com/user/repo.git@branch']
        ...
    )
  
For older pip versions, which doesnot support PEP 508 format, you can specify a list of one or more ``dependency_links`` URLs where the package can be downloaded, along with some additional hints, and setuptools will find and install the package correctly. This method is deprecated in newer pip versions.

For example, if a library is published on GitHub, you can specify it like::

    setup(
        ...
        dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0']
        ...
    )

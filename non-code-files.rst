Adding Non-Code Files
=====================

Often packages will need to depend on files which are not ``.py`` files: e.g. images, data tables, documentation, etc. Those files need special treatment in order for setuptools to handle them correctly.

The mechanism that provides this is the ``MANIFEST.in`` file. This is relatively quite simple: ``MANIFEST.in`` is really just a list of relative file paths specifying files or globs to include.::

    include README.rst
    include docs/*.txt
    include funniest/data.json

.. note::

    Files which are to be used by your installed library (e.g. data files to support a particular computation method) should usually be placed inside of the Python module directory itself. E.g. in our case, a data file might be at ``funniest/funniest/data.json``. That way, code which loads those files can easily specify a relative path from the consuming module's ``__file__`` variable.

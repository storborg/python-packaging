Putting It All Together
-----------------------

Our whole package, for reference, looks like this::

    funniest/
        funniest/
            __init__.py
            cmd.py
            tests/
                __init__.py
                test_joke.py
                test_cmd.py
        MANIFEST.in
        README.rst
        setup.py
        .gitignore

Here is the contents of each file:

**funniest/__init__.py**

.. literalinclude:: funniest/funniest/__init__.py

**funniest/cmd.py**

.. literalinclude:: funniest/funniest/cmd.py

**funniest/tests/__init__.py**

(empty)

**funniest/tests/test_joke.py**

.. literalinclude:: funniest/funniest/tests/test_joke.py

**funniest/tests/test_cmd.py**

.. literalinclude:: funniest/funniest/tests/test_cmd.py

**MANIFEST.in**

.. literalinclude:: funniest/MANIFEST.in

**README.rst**

.. literalinclude:: funniest/README.rst.example

**setup.py**

.. literalinclude:: funniest/setup.py

**.gitignore**

.. literalinclude:: funniest/.gitignore

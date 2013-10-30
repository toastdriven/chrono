======
chrono
======

A (BSD licensed) context manager for timing execution. Useful for benchmarking
everyday Python code easily/cleanly.


Usage
=====

Usage is trivial. Simply wrap your code in a ``Timer`` context manager.
Example::

    from chrono import Timer

    with Timer() as timed:
        # Put whatever logic you want here.
        # ``for`` loops are great here for timing things that are very fast.

    print("Time spent: {0} seconds".format(timed.elapsed))


Requirements
============

* Python 2.6+ or Python 3.3+ (may work on Python 2.5)


License
=======

BSD


Docs
====

http://chrono-bench.readthedocs.org/en/latest/


Shortcomings
============

This is implemented in pure Python, so it doesn't have the accuracy a C
extension would have. There's also overhead for the context manager function
calls, so don't use this to bench C code.

That said, for most everyday usage of Python, it's very helpful.


Running Tests
=============

Setup::

    $ git clone https://github.com/toastdriven/chrono.git
    $ cd chrono
    $ virtualenv -p python3 env3
    $ . env3/bin/activate
    $ pip install nose

Running::

    $ nosetests -s -v tests.py

``chrono`` is maintained with 100% passing tests at all times.


Changelog
=========

Dev
    * Added links to the docs

v1.0.1
    * Added initial docs
    * Fixed up the main docstring in ``Timer``

v1.0.0
    * Initial release

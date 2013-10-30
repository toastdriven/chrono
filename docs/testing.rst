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

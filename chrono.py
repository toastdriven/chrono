"""
chrono
======

A (BSD licensed) context manager for timing execution. Useful for benchmarking
everyday Python code easily/cleanly.


Usage
-----

Usage is trivial. Simply wrap your code in a ``Timer`` context manager.
Example::

    from chrono import Timer

    with Timer() as timed:
        # Put whatever logic you want here.
        # ``for`` loops are great here for timing things that are very fast.

    print("Time spent: {0} seconds".format(timed.elapsed))

"""
import time


__author__ = 'Daniel Lindsley'
__version__ = (1, 0, 2)
__license__ = 'BSD'


class Timer(object):
    """
    A context manager that times the code it wraps.

    Usage::

        with Timer() as timed:
            # Code goes here.

        print(timed.elapsed)

    """
    def __init__(self):
        self.start = None
        self.end = None
        self.elapsed = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, type, value, tb):
        if tb:
            return False

        self.end = time.time()
        self.elapsed = self.end - self.start

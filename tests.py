from __future__ import print_function
import time
import unittest

from chrono import Timer


class TimerTestCase(unittest.TestCase):
    def test_typical(self):
        with Timer() as timed:
            time.sleep(0.5)

        # Ballpark it.
        self.assertTrue(timed.elapsed > 0.5)
        self.assertTrue(timed.elapsed < 0.75)

        # Unless time suddenly starts flowing backwards...
        self.assertTrue(timed.end > timed.start)

    def test_exception(self):
        # Make sure exceptions properly bubble up.
        with self.assertRaises(ValueError):
            with Timer() as timed:
                calc = 1 + 1
                raise ValueError("nopenopenope")
                print("Should never get here.")

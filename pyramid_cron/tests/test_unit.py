from datetime import datetime
from unittest import TestCase

from .. import Task


def noop():
    pass


class TestUnit(TestCase):
    def test_wildcard_everything(self):
        task = Task(noop, min='*', hour='*', day='*', month='*', dow='*', idle=False)
        self.assertTrue(task.check(datetime(2014, 3, 1, 17, 32)))
        self.assertTrue(task.check(datetime(1961, 9, 3, 12, 17)))
        self.assertTrue(task.check(datetime(2003, 12, 20, 4, 00)))

    def test_specific_time(self):
        task = Task(noop, min='*', hour=17, day='*', month='*', dow='*', idle=False)
        self.assertTrue(task.check(datetime(2014, 3, 1, 17, 32)))
        self.assertFalse(task.check(datetime(1961, 9, 3, 12, 17)))
        self.assertFalse(task.check(datetime(2003, 12, 20, 4, 00)))

    def test_complex(self):
        task = Task(noop, min=range(0, 60, 10), hour=set([17, 11]),
                    day='*', month='*', dow='*', idle=False)
        self.assertFalse(task.check(datetime(2014, 3, 1, 17, 32)))
        self.assertFalse(task.check(datetime(1961, 9, 3, 12, 17)))
        self.assertFalse(task.check(datetime(2003, 12, 20, 4, 00)))

        self.assertTrue(task.check(datetime(2014, 3, 1, 17, 10)))
        self.assertTrue(task.check(datetime(1961, 9, 3, 17, 30)))
        self.assertTrue(task.check(datetime(2000, 8, 17, 17, 00)))

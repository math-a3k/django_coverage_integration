from django.test import TestCase


class Test1(TestCase):
    def test_something(self):
        self.assertTrue(True)


class Test2(TestCase):
    def test_something_else(self):
        self.assertFalse(False)

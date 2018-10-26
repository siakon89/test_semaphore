from django.test import TestCase


class TestingTheTest(TestCase):

    def test_simple(self):
        self.assertEqual(1, 1, 'OK.')

    def test_simple1(self):
        self.assertEqual(1, 1, 'OK.')

    def test_simple2(self):
        self.assertEqual(1, 1, 'OK.')

    def test_simple3(self):
        self.assertEqual(1, 1, 'OK.')

    def test_simple4(self):
        self.assertEqual(1, 1, 'OK.')

    def test_simple5(self):
        self.assertEqual(1, 1, 'OK.')

    def test_simple6(self):
        self.assertEqual(1, 1, 'OK.')

    def test_simple7(self):
        self.assertEqual(1, 1, 'OK.')

    def test_simple8(self):
        self.assertEqual(1, 2, 'Ooops.')

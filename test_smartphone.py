# file: test_smartphone.py
import unittest
from smartphone import Smartphone

class TestSmartphone(unittest.TestCase):
    def test_get_preu_web(self):
        iphone = Smartphone('iPhone', 1000, 10, '48MP')
        self.assertEqual(1215, iphone.get_preu_web())
# file: test_portatil.py
import unittest
from portatil import Portatil

class TestPortatil(unittest.TestCase):
    def test_create_portatil(self):
        ram = 16
        cpu = "M2"
        portatil = Portatil("MacBook", 1000, 5, ram, cpu)
        self.assertEqual(ram, portatil.ram)
        self.assertEqual(cpu, portatil.processador)

# file: test_producte.py
import unittest
from producte import Producte

class TestProducte(unittest.TestCase):
    def test_get_preu_web(self):
        producte = Producte('a', 1, 1)
        self.assertEqual(producte.get_preu_web(), 1.21)
    
    def test_vendre(self):
        producte = Producte('a', 1, 1)
        message_ok = '✅ Venda realitzada: 1 de 1'
        message_ko = '❌ Error: No hi ha prou stock de a'
        self.assertEqual(producte.vendre(1), message_ok)
        self.assertEqual(producte.vendre(1), message_ko)

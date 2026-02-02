# file; test_carret_compra.py
import unittest
from carret_compra import CarretCompra

class TestCarretCompra(unittest.TestCase):
    def test_afegir(self):
        carret = CarretCompra()
        mac = Portatil("MacBook", 1000, 5, 16, 'M2')
        iphone = Smartphone('iPhone', 1000, 10, '48MP')
        carret.afegir(mac)
        carret.afegir(iphone)
        self.assertEqual(2, len(carret.lista_productes))
        
    def test_checkout(self):
        carret = CarretCompra()
        mac = Portatil("MacBook", 1000, 5, 16, 'M2')
        iphone = Smartphone('iPhone', 1000, 10, '48MP')
        carret.afegir(mac)
        carret.afegir(iphone)
		result = "\n--- TIQUET DE COMPRA ---\n- MackBook: 1000€\n- iPhone: 1000€\n------------------------\nTOTAL A PAGAR: 2000€"
		self.assertEqual(result, carret.checkout())

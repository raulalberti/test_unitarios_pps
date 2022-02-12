import unittest
from practica_tests_unitarios import Suma, Resta

class TestsCalculadora(unittest.TestCase):

    def test_suma_esnumero(self):
#1 Definimos datos de entrada
        x = 'Hola'
        y = 4
#2 Hacemos la comprobacion de lo que queremos
#Que nos devuelva una excepción por consola.
        with self.assertRaises(ValueError) as exc:
            Suma(x=x, y=y)
        self.assertEqual(str(exc.exception), 'Los datos deben de ser números enteros')

    def test_resta_no_negativos(self):
#1 Definimos datos de entrada
        x = 2
        y = -2
#2 Hacemos la comprobacion de lo que queremo
#Que nos devuelva una excepción por consola.
        with self.assertRaises(ValueError) as exc:
            Resta(x=x, y=y)
        self.assertEqual(str(exc.exception), 'Los datos no pueden ser negativos')

if __name__ == '__main__':
    unittest.main()





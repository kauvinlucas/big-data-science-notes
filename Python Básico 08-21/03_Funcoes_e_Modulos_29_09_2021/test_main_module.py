import unittest

import main_module as main

class Filtr_n_Mult(unittest.TestCase):
    def test_filtr_n_mult(self):
        lista = [2,5,1,4,6,7,2,1]
        resultado = main.filtr_n_mult(lista)
        self.assertEqual(resultado, [15,3,21,3])

if __name__ == '__main__':
    unittest.main()

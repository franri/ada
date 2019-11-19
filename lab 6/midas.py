def midas(n, map):
    paradas = []
    paradas.append(0)
    tanque = n
    for ciudad in range(len(map)):
        if tanque < map[ciudad]:
            paradas.append(ciudad)
            tanque = n - map[ciudad]
        else:
            tanque -= map[ciudad]
    return paradas


import unittest

class TestMidas(unittest.TestCase):

    def test_midas_long_trip(self):
        map = [10, 10, 15, 2]
        n = 25
        # tiene 25 litros
        # carga en la primera ciudad 0
        # llega con 15 a la segunda, y precisa 10 para la tercera: sigue
        # llega con 5 a la tercera y precisa 15 para la cuarta: carga en la tercera ciudad 2
        # llega con 10 a la cuarta, y precisa 2 para la próxima: no carga  sigue
        self.assertEqual(midas(n, map), [0, 2])

    def test_midas_short_trip(self):
        map = [10, 10, 1, 2]
        n = 25
        # le da con un solo tanque para todo el viaje: carga sólo en la primera ciudad
        self.assertEqual(midas(n, map), [0])

if __name__ == '__main__':
    unittest.main()
import unittest
from crosscountry_trip import trip

class TestLab1(unittest.TestCase):

    def setUp(self):
        self.un_o = [40, 5, 3, 51, 5, 0, -4, 4]
        self.o = [-4, 0, 3, 4, 5, 5, 40, 51]
    
    def test_prof_curlys_crosscountry_trip(self):
        m = [
        [0,11,25,4,44],
        [0,0,1,4,1],
        [0,0,0,1,2],
        [0,0,0,0,9],
        [0,0,0,0,0]
        ]
        self.assertEqual(trip(m), (12, [1,2,5]))

        m = [
        [0,11,25,4,44],
        [0,0,1,4,99],
        [0,0,0,1,2],
        [0,0,0,0,9],
        [0,0,0,0,0]
        ]
        self.assertEqual(trip(m), (13, [1,4,5]))

        m = [
        [0,2,99,99,99],
        [0,0,99,2,99],
        [0,0,0,99,99],
        [0,0,0,0,2],
        [0,0,0,0,0]
        ]
        self.assertEqual(trip(m), (6, [1,2,4,5]))

if __name__ == '__main__':
    unittest.main()
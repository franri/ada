import unittest
from binary_search import binary_search
from selection_sort import selection_sort
from find_min import find_min
import random

class TestLab1(unittest.TestCase):

    def setUp(self):
        self.un_o = [40, 5, 3, 51, 5, 0, -4, 4]
        self.o = [-4, 0, 3, 4, 5, 5, 40, 51]
    
    def test_find_min(self):
        self.assertEqual(find_min(self.un_o), (6, -4))
        self.assertEqual(find_min(self.o), (0, -4))

    def test_binary_search(self):
        self.assertEqual(binary_search(self.o, 3), 2)
        self.assertEqual(binary_search(self.o, -4), 0)
        self.assertEqual(binary_search(self.o, 51), 7)
        self.assertEqual(binary_search(self.o, 40), 6)
        self.assertFalse(binary_search(self.o, 51) == 2)
        self.assertEqual(binary_search(self.o, 99), 'Not Found')

    def test_selection_sort(self):
        selection_sort(self.un_o)
        self.assertEqual(self.un_o, self.o)

    def test_selection_sort_1000(self):
        u_arr = [random.randint(0, 100) for _ in range(1, 1001)]
        copy = u_arr[:]
        selection_sort(u_arr)
        copy.sort()
        self.assertEqual(u_arr, copy)

if __name__ == '__main__':
    unittest.main()
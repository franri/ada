def payoff(a, b):
    a.sort()
    b.sort()
    count = 1
    for i in range(len(a)):
        count *= a[i]**b[i]
    return count

import unittest

class TestPayoff(unittest.TestCase):

    def test_payoff(self):
        a = [1, 3, 4, 2]
        b = [2, 3, 9, 0]
        self.assertEqual(payoff(a, b), 28311552)
        

if __name__ == '__main__':
    unittest.main()
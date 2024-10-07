import unittest
import ex_proj

class Test(unittest.TestCase):
    def test_square_of_num(self):
        self.assertEqual(ex_proj.square_of_numbers(4),16)
        self.assertEqual(ex_proj.square_of_numbers(-4),16)
        self.assertEqual(ex_proj.square_of_numbers(0),0)
    def test_add(self):
        self.assertEqual(ex_proj.add(10,3),13)

    def test_div(self):
        self.assertEqual(ex_proj.divide(10,1),10)
        self.assertRaises(ValueError, ex_proj.divide, 10,0)

if __name__ == '__main__':
    unittest.main()
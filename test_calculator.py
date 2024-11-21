import unittest
from calculator import divide, is_even

class TestCalculator(unittest.TestCase):

     def test_divide_by_zero(self):
         with self.assertRaises(ValueError):
              divide(10, 0)

     def test_is_even(self):
          self.assertTrue(is_even(4))
          self.assertFalse(is_even(3))

  if__name__=='__main__':
     unittest.main()

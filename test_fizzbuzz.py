import unittest
import fizzbuzz 

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        result = fizzbuzz.fbuzz(15)
        self.assertEqual(result, "Fizzbuzz")
    def test_add(self):
        result = fizzbuzz.fbuzz(3)
        self.assertEqual(result, "Fizz")
    

if __name__ == '__main__':
    unittest.main()
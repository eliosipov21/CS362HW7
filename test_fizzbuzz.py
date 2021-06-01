import unittest
import fizzbuzz 

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        result = fizzbuzz.fbuzz(15)
        self.assertEqual(result, "Fizzbuzz")
    def test_add2(self):
        result = fizzbuzz.fbuzz(3)
        self.assertEqual(result, "Fizz")
    def test_add3(self):
        result = fizzbuzz.fbuzz(5)
        self.assertEqual(result, "Buzz")
    

if __name__ == '__main__':
    unittest.main()
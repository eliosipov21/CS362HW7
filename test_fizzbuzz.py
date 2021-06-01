import unittest
import fizzbuzz 

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        result = fizzbuzz.fbuzz(15)
        self.assertEqual(result, "Fizzbuzz")
    

if __name__ == '__main__':
    unittest.main()
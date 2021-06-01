import unittest
import leapyr 

class testCaseAdd(unittest.TestCase):
    def test_leap1(self):
        result = leapyr.leapyear(404)
        self.assertEqual(result, True)
    def test_leap1(self):
        result = leapyr.leapyear(500)
        self.assertEqual(result, False)

    

if __name__ == '__main__':
    unittest.main()
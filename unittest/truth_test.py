import unittest

class TruthTest(unittest.TestCase):
    
    def test_assert_true(self):
        self.assertTrue((5-2) == 3)
        
    def test_assert_false(self):
        self.assertFalse((5-2) == 4)
        
    def test_not_equal(self):
        self.assertEqual(6, 8-2)        
        
    def test_equal(self):
        self.assertNotEqual(7, 4*2)
        
if __name__ == "__main__":
    unittest.main()
import unittest
import rectangle_perimeter
import sys
 
class TestArea(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter(10,5), 30)
        
    '''
    def test_error(self):
        self.assertRaises(ValueError, 
                         rectangle_perimeter.get_perimeter,
                         10,0)
    '''
    
    # assertTrue
    # assertFalse
    # assertRaises
    # assertEqual
    # assertNotEqual
    # assertIs
    # assertIsNot
    # assertIsNone
    # assertIsNotNone
    # assertIsInstance
    # assertIsNotInstance
    # assertIn
    # assertNotIn
    
    '''
    assertAlmostEqual(a, b)
    assertNotAlmostEqual(a, b)
    assertGreater(a, b)
    assertGreaterEqual(a, b)
    assertLess(a, b)
    assertLessEqual(a, b)
    assertRegex(s, r)
    assertNotRegex(s, r)
    assertCountEqual(a, b)
    '''
        
    #@unittest.skip('Temporarily skips error test')
    #@unittest.skipIf(sys.version_info[0]<3,'This test requires Python 3 or higher')
    #sys.version_info[0]>=3, 'thi stest required 2 python version or lower'
    #unless -> darwin for MACOS 
    @unittest.skipUnless(sys.platform.startswith('win'), 'required Windows')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 0)
            
            
if __name__ == "__main__":
    unittest.main()
    
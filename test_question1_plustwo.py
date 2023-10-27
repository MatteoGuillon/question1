'''
test_question1_plustwo.py

Test file for the Mini Assessment.

'''



import unittest

import question1 as q

class TestStructures(unittest.TestCase):   
    def test_plus_two_integer(self):
        '''
        Test with an integer
        '''
        result = q.plus_two(5)
        self.assertEqual(result, 7)
    
    def test_plus_two_decimal(self):
        '''
        Test with a floating point number
        '''
        result = q.plus_two(10.2)
        self.assertEqual(result, 12.2)
    
    
if __name__ == '__main__':
    unittest.main()
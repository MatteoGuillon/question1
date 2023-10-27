'''
test_question1_negativeerror.py

Test file for the Mini Assessment.

'''



import unittest

import question1 as q

class TestStructures(unittest.TestCase):   
    def test_negative_negative(self):
        '''
        Test with negative number
        '''
        with self.assertRaises(ValueError):
            result = q.negative_error(-3)
    
    def test_negative_positive(self):
        '''
        Test with positive number
        '''
        result = q.negative_error(22)


if __name__ == '__main__':
    unittest.main()
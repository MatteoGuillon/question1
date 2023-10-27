'''
test_question1_alwaystrue.py

Test file for the Mini Assessment.

'''



import unittest

import question1 as q

class TestStructures(unittest.TestCase):
    def test_always_true(self):
        '''
        Test that True is returned
        '''
        result = q.always_true()
        self.assertTrue(result)
    

if __name__ == '__main__':
    unittest.main()
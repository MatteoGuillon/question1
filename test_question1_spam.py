'''
test_question1.py

Test file for the Mini Assessment.

'''



import unittest

import question1 as q

class TestStructures(unittest.TestCase):   
    def test_spam(self):
        '''
        Test that spam is returned
        '''
        result = q.spam()
        self.assertEqual(result, 'spam')



if __name__ == '__main__':
    unittest.main()
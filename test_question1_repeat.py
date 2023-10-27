'''
test_question1_repeat.py

Test file for the Mini Assessment.

'''



import unittest

import question1 as q

class TestStructures(unittest.TestCase):
    def test_repeat(self):
        '''
        Test that input is repeated
        '''
        result = q.repeat('input text')
        self.assertEqual(result, ['input text','input text','input text'])
    

if __name__ == '__main__':
    unittest.main()
import unittest
from email_check import find_email

class testcases(unittest.TestCase):
    def caseone(self):
        testcase = [None, 'Blossom', 'Gill']
        expected = 'blossom@abc.edu'
        self.assertEqual(find_email(testcase), expected)

    def casetwo(self):
        testcase = [None, 'blossom']
        expected = 'Missing Parameters'
        self.assertEqual(find_email(testcase), expected)

unittest.main()
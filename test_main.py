import unittest
from main import capitalize_words

class TestMain(unittest.TestCase):
    def test_capitalize_words(self):
        # Test case where input string has two words
        self.assertEqual(capitalize_words('hello World'), 'Hello world')
        
        # Test case where input string has more than two words
        # self.assertEqual(capitalize_words('this IS A TEST'), 'This is a test')
        self.assertEqual(capitalize_words('this is a test'), 'This is a test')
        
        # Test case where input string has only one word
        self.assertEqual(capitalize_words('Hello'), 'Hello')
        
        # Test case where input string is empty
        self.assertEqual(capitalize_words(''), '')
        
        # Test case where input string has leading/trailing whitespace
        self.assertEqual(capitalize_words('   hello World  '), 'Hello world')

if __name__ == '__main__':
    unittest.main()


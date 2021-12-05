import unittest
from translator import english_to_french, french_to_english

class test_translator_en_to_fr(unittest.TestCase):
    """
    Class to test the function english to french
    """
    def test_en(self):
        """
        Function to test the function english to French
        """
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class test_translator_fr_to_en(unittest.TestCase):
    """
    Class to test the function french to english
    """
    def test_fr(self):
        """
        Function to test the function french to english
        """
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
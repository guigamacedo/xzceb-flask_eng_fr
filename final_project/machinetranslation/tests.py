import unittest
import translator

class TranslatorTestCase(unittest.TestCase):

    def test_null_input_english_to_french(self):
        text = None
        result = translator.english_to_french(text)
        self.assertEqual(result, False)
    
    def test_valid_input_english_to_french(self):
        text = "Hello"
        result = translator.english_to_french(text)
        self.assertEqual(result, "Bonjour")

    def test_null_input_french_to_english(self):
        text = None
        result = translator.french_to_english(text)
        self.assertEqual(result, False)
    
    def test_valid_input_french_to_english(self):
        text = "Bonjour"
        result = translator.french_to_english(text)
        self.assertEqual(result, "Hello")

if __name__ == "__main__":
    unittest.main()
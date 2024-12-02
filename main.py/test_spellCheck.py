import unittest
from main import load_wordlist, is_one_edit_away, suggest_spelling

class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        """Set up the word list for testing."""
        self.wordlist = load_wordlist()

    def test_load_wordlist(self):
        """Test that the word list loads correctly."""
        self.assertIn("apple", self.wordlist)
        self.assertIn("computer", self.wordlist)
        self.assertNotIn("nonexistentword", self.wordlist)

    def test_exact_match(self):
        """Test exact matches in the word list."""
        self.assertTrue("apple" in self.wordlist)
        self.assertTrue("dog" in self.wordlist)

    def test_is_one_edit_away(self):
        """Test the one-edit-away functionality."""
        self.assertTrue(is_one_edit_away("apple", "appl"))  # Deletion
        self.assertTrue(is_one_edit_away("aple", "apple"))  # Insertion
        self.assertTrue(is_one_edit_away("bpple", "apple"))  # Replacement
        self.assertFalse(is_one_edit_away("aappple", "apple"))  # Too many edits
        self.assertFalse(is_one_edit_away("banana", "orange"))  # Unrelated words

    def test_suggest_spelling(self):
        """Test spelling suggestions."""
        self.assertEqual(suggest_spelling("appl", self.wordlist), "apple")
        self.assertEqual(suggest_spelling("bpple", self.wordlist), "apple")
        self.assertEqual(suggest_spelling("computr", self.wordlist), "computer")
        self.assertEqual(suggest_spelling("doge", self.wordlist), "dog")
        self.assertIsNone(suggest_spelling("aappple", self.wordlist))  # Too many edits
        self.assertIsNone(suggest_spelling("unknownword", self.wordlist))  # No match



    def test_no_suggestions_found(self):
        """Test no suggestions for words not in the wordlist."""
        self.assertIsNone(suggest_spelling("xyz", self.wordlist))  # Random string
        self.assertIsNone(suggest_spelling("nonexistentword", self.wordlist))  # Long string

    def test_case_sensitivity(self):
        """Test handling of different cases."""
        self.assertTrue("apple" in self.wordlist)  # lowercase match
        self.assertFalse("Apple" in self.wordlist)  # Uppercase "A" doesn't match the list as it's lowercase
        self.assertTrue("APPLE" not in self.wordlist)  # Uppercase doesn't exist in the list

if __name__ == "__main__":
    unittest.main()

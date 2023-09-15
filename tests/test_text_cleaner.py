import unittest

import text_cleaner


class TextCleanerTest(unittest.TestCase):

    def test_removes_emojis(self):
        self.assertEqual(text_cleaner.remove_emoji('😀 hi'), ' hi')
        self.assertEqual(text_cleaner.remove_emoji(' hi'), ' hi')

    def test_remove_specific_characters(self):
        self.assertEqual(text_cleaner.remove_specific_characters('hi£££££££'), 'hi')
        self.assertEqual(text_cleaner.remove_specific_characters('hi'), 'hi')
        self.assertEqual(text_cleaner.remove_specific_characters('hi.'), 'hi.')

    def test_replace_contractions(self):
        self.assertEqual(text_cleaner.replace_contractions('hi btw ma\'am'), 'hi by the way madam')
        self.assertEqual(text_cleaner.replace_contractions('hi by the way madam'), 'hi by the way madam')


if __name__ == '__main__':
    unittest.main()

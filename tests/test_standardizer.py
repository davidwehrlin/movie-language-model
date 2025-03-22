import unittest
from movie_scraper.standardizer import Standardizer

class TestStandardizer(unittest.TestCase):

    def test_remove_page_numbers(self):
        test_cases = [
            ("141. through 142A.  ", ""),
        ]

        for input_line, expected_output in test_cases:
            with self.subTest(input_line=input_line, expected_output=expected_output):
                self.assertEqual(Standardizer.remove_page_numbers(input_line), expected_output)

if __name__ == '__main__':
    unittest.main()
import unittest
from logic.utils import rename_chronologically


class TestUtils(unittest.TestCase):
    def test_rename_chronologically(self):
        # given
        files = {"file.jpg": 1,
                 "abc.JPG": 10}

        expected = {"file.jpg": "basename_001.jpg",
                    "abc.JPG": "basename_002.JPG"}

        # when
        output = rename_chronologically("basename", files)

        # then
        self.assertDictEqual(expected, output)

    def test_rename_chronologically_omit_directories(self):
        # given
        files = {"dummy_directory": 1,
                 "abc.JPG": 10}

        expected = {"abc.JPG": "basename_001.JPG"}

        # when
        output = rename_chronologically("basename", files)

        # then
        self.assertDictEqual(expected, output)


if __name__ == '__main__':
    unittest.main()

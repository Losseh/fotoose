import unittest
from logic.utils import map_to_chronological_names, retain_letters


class TestUtils(unittest.TestCase):
    def test_rename_chronologically(self):
        # given
        files = {"zfile.jpg": 1.0,
                 "test.jpg": 1.0,
                 "test1.jpg": 2.0,
                 "test2.jpg": 122.0,
                 "test3.jpg": 4.0,
                 "test4.jpg": 11.0,
                 "cdf.jpg": 1.0,
                 "123.jpg": 21.0,
                 "testowy.jpg": 34.0,
                 "abc.JPG": 10.0}

        expected = {"cdf.jpg": "basename001.jpg",
                    "test.jpg": "basename002.jpg",
                    "zfile.jpg": "basename003.jpg",
                    "test1.jpg": "basename004.jpg",
                    "test3.jpg": "basename005.jpg",
                    "abc.JPG": "basename006.JPG",
                    "test4.jpg": "basename007.jpg",
                    "123.jpg": "basename008.jpg",
                    "testowy.jpg": "basename009.jpg",
                    "test2.jpg": "basename010.jpg"}

        # when
        output = map_to_chronological_names("basename", files)

        # then
        self.assertDictEqual(expected, output)

    def test_rename_chronologically_omit_directories(self):
        # given
        files = {"dummy_directory": 1.0,
                 "abc.JPG": 10.0}

        expected = {"abc.JPG": "basename001.JPG"}

        # when
        output = map_to_chronological_names("basename", files)

        # then
        self.assertDictEqual(expected, output)

    #TODO we should omit non-image files

    def test_retain_letters(self):
        self.assertEqual("avxname", retain_letters(".;123a.vx-123n ame"))


if __name__ == '__main__':
    unittest.main()

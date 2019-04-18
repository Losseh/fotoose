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

        expected = {"cdf.jpg": "basename0001.jpg",
                    "test.jpg": "basename0002.jpg",
                    "zfile.jpg": "basename0003.jpg",
                    "test1.jpg": "basename0004.jpg",
                    "test3.jpg": "basename0005.jpg",
                    "abc.JPG": "basename0006.JPG",
                    "test4.jpg": "basename0007.jpg",
                    "123.jpg": "basename0008.jpg",
                    "testowy.jpg": "basename0009.jpg",
                    "test2.jpg": "basename0010.jpg"}

        # when
        output = map_to_chronological_names("basename", files)

        # then
        self.assertDictEqual(expected, output)

    def test_rename_lots_of_files_does_not_produce_same_new_filenames(self):
        # given
        number_of_files = 1912
        files = {"photo{}.jpg".format(i): float(i) for i in xrange(number_of_files)}

        # when
        output = map_to_chronological_names("base", files)

        # then
        self.assertEqual(12, len(output.values()[0]))
        self.assertEqual(number_of_files, len(set(output.values())))

    def test_rename_chronologically_omit_directories(self):
        # given
        files = {"dummy_directory": 1.0,
                 "abc.JPG": 10.0}

        expected = {"abc.JPG": "basename0001.JPG"}

        # when
        output = map_to_chronological_names("basename", files)

        # then
        self.assertDictEqual(expected, output)

    #TODO we should omit non-image files

    def test_retain_letters(self):
        self.assertEqual("avxname", retain_letters(".;123a.vx-123n ame"))


if __name__ == '__main__':
    unittest.main()

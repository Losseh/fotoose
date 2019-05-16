import unittest
from logic.utils import map_to_chronological_names, retain_letters
from datetime import datetime


class TestUtils(unittest.TestCase):
    def test_rename_chronologically(self):
        # given
        files = {"zfile.jpg": datetime(2018, 1, 1),
                 "test.jpg": datetime(2018, 1, 1),
                 "test1.jpg": datetime(2018, 1, 2),
                 "test2.jpg": datetime(2019, 4, 5),
                 "test3.jpg": datetime(2018, 1, 4),
                 "test4.jpg": datetime(2018, 1, 11),
                 "cdf.jpg": datetime(2018, 1, 1),
                 "123.jpg": datetime(2018, 1, 21),
                 "testowy.jpg": datetime(2018, 2, 1),
                 "abc.JPG": datetime(2018, 1, 10)}

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
        files = {"photo{}.jpg".format(i): self.int_to_datetime(i) for i in xrange(number_of_files)}

        # when
        output = map_to_chronological_names("base", files)

        # then
        self.assertEqual(12, len(output.values()[0]))
        self.assertEqual(number_of_files, len(set(output.values())))

    @staticmethod
    def int_to_datetime(number):
        days_in_month = 25
        months_in_year = 12
        day = 1 + number % days_in_month
        month = 1 + (number / days_in_month) % months_in_year
        year = 2000 + (number / days_in_month / months_in_year)
        return datetime(year, month, day)

    def test_rename_chronologically_given_directory_raises_assertionerror(self):
        # given
        files = {"dummy_directory": datetime(2018, 1, 1),
                 "abc.JPG": datetime(2018, 1, 10)}

        # when / then
        with self.assertRaises(AssertionError):
            map_to_chronological_names("basename", files), AssertionError

    def test_rename_chronologically_nonimage_raises_assertionerror(self):
        # given
        files = {"some_file.txt": datetime(2018, 1, 1),
                 "abc.JPG": datetime(2018, 1, 10)}

        # when / then
        with self.assertRaises(AssertionError):
            map_to_chronological_names("basename", files), AssertionError

    def test_retain_letters(self):
        self.assertEqual("avxname", retain_letters(".;123a.vx-123n ame"))


if __name__ == '__main__':
    unittest.main()

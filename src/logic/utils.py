from datetime import datetime


def rename_file(basename, extension, number):
    return '{}{:0>4}.{}'.format(basename, number, extension)


def get_extension(filename):
    split = filename.split(".")
    parts_number = len(split)
    assert parts_number == 1 or parts_number == 2

    if parts_number == 1:
        return None

    if parts_number == 2:
        return split[1]


def map_to_chronological_names(basename, files):
    """
    Sorts the files chronologically and returns a dictionary containing
    old filename as key and new filename as value.

    !Important: dates must be datetime typed

    >>> map_to_chronological_names("base", {"f.jpg", datetime'2015:03:21 22:59:31'})
    {"f.jpg": "base001.jpg"}
    """

    assert_all_files_are_images(files.keys())
    date_to_files = gather_files_by_date(files)

    output = {}
    counter = 1
    for date, files in sorted(date_to_files.iteritems()):
        files.sort()
        for old_file in files:
            output[old_file] = rename_file(basename, get_extension(old_file), counter)
            counter += 1

    return output


def gather_files_by_date(files):
    date_to_files = {}
    for f, date in files.iteritems():
        assert isinstance(date, datetime), "given date {} is not an instance of datetime class".format(date)
        if get_extension(f) is not None:
            if date in date_to_files:
                date_to_files[date].append(f)
            else:
                date_to_files[date] = [f]

    return date_to_files


def assert_all_files_are_images(filepaths):
    for path in filepaths:
        assert is_image_file(path), "{} is not an image file".format(path)


def is_image_file(filepath):
    #TODO checks if the the filepath refers to a image file
    #TODO this should be some kind of constant
    allowed_extensions = {'jpg', 'png', 'JPG', 'PNG'}
    path_and_extension = filepath.split(".")

    return len(path_and_extension) != 0 and path_and_extension[-1].lower() in allowed_extensions


def retain_letters(text):
    return ''.join(x for x in text if x.isalpha())

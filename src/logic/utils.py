
def rename_file(basename, extension, number):
    return '{}_{:0>3}.{}'.format(basename, number, extension)


def get_extension(filename):
    split = filename.split(".")
    parts_number = len(split)
    assert parts_number == 1 or parts_number == 2

    if parts_number == 1:
        return None

    if parts_number == 2:
        return split[1]


def rename_chronologically(basename, files):
    """
    Sorts the files chronologically and returns a dictionary containing
    old filename as key and new filename as value

    >>> rename_chronologically("base", {"f.jpg", 1})
    {"f.jpg": "base001.jpg"}
    """

    date_to_file = {date: f for f, date in files.iteritems() if get_extension(f) is not None}

    dates = date_to_file.keys()
    dates.sort()

    file_to_number = {date_to_file[date]: i + 1 for i, date in enumerate(dates)}

    output = {}

    for date, old_file in date_to_file.iteritems():
        output[old_file] = rename_file(basename, get_extension(old_file), file_to_number[old_file])

    return output


def is_image_file(filepath):
    #TODO checks if the the filepath refers to a image file

    #TODO this should be some kind of constant
    allowed_extensions = {'jpg', 'png'}
    path_and_extension = filepath.split(".")

    return len(path_and_extension) != 0 and path_and_extension[-1].lower() in allowed_extensions

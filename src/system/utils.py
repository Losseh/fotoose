from os import rename
from os.path import join, getmtime


def rename_files(directory, rename_map):
    for old_name, new_name in rename_map.iteritems():
        old_path = join(directory, old_name)
        new_path = join(directory, new_name)
        rename(old_path, new_path)


def map_files_to_creation_time(directory, files):
    return {f: getmtime(join(directory, f)) for f in files}

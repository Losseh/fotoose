from os import rename, mkdir, rmdir
from os.path import join, getmtime
import tempfile
import logging


def is_rename_map_identity(rename_map):
    for old, new in rename_map.iteritems():
        if old != new:
            return False

    return True


def rename_files(directory, rename_map):
    logger = logging.getLogger(__name__)

    if is_rename_map_identity(rename_map):
        logger.debug("rename_files: Nothing to change, breaking")
        return

    # create temporary directory
    temporary_dir = "temp" + next(tempfile._get_candidate_names());
    temporary_dir_path = join(directory, temporary_dir)
    mkdir(temporary_dir_path)

    # first move every file to a temp directory
    for old_name, new_name in rename_map.iteritems():
        old_path = join(directory, old_name)
        temp_path = join(directory, temporary_dir, old_name)
        rename(old_path, temp_path)

    # then move each file from temp dir to the old dir and rename it
    for old_name, new_name in rename_map.iteritems():
        temp_path = join(directory, temporary_dir, old_name)
        new_path = join(directory, new_name)
        rename(temp_path, new_path)

    # remove temporary directory
    rmdir(temporary_dir_path)
    logger.debug("rename_files: Renamed {} files successfully".format(len(rename_map)))


def map_files_to_creation_time(directory, files):
    return {f: getmtime(join(directory, f)) for f in files}

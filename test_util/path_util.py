import os


def listfiles(path):
    files_found = []
    for (_, _, files) in os.walk(path):
        files_found.extend(files)
    return files_found


def pf(wd, path):
    return os.path.join(wd, path)

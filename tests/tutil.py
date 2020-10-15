from path import Path


def dir_files(dir, match):
    ls = Path(dir).walkfiles(match)
    return list(ls)

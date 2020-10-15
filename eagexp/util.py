from os.path import abspath, expanduser, expandvars, normpath


def norm_path(s):
    s = expandvars(s)
    s = expanduser(s)
    s = normpath(s)
    s = abspath(s)
    return s


def read_text(fname, encoding=None):
    with open(fname, encoding=encoding) as f:
        return f.read()


def write_text(fname, s):
    with open(fname, "w") as f:
        return f.write(s)

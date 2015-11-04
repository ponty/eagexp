from path import Path


def norm_path(s):
    s = Path(s).expand().abspath()
    return s

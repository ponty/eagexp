from path import path

def norm_path(s):
    s=path(s).expand().abspath()
    return s
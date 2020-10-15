from os.path import exists, join

from backports import tempfile

from eagexp.image3d import export_image3d
from tutil import dir_files

VISIBLE = 0
EXAMPLES = "/usr/share/eagle/projects/examples"


def export(fin, **kwargs):
    with tempfile.TemporaryDirectory() as temp_dir:
        fout = join(temp_dir, "out.png")
        export_image3d(fin, fout, showgui=VISIBLE, **kwargs)
        assert exists(fout)


def test_all():
    brd_ls = dir_files(EXAMPLES, "*.brd")

    for x in brd_ls:
        export(x)


def test_options():
    brd_ls = dir_files(EXAMPLES, "*.brd")

    export(brd_ls[0], timeout=65)
    export(brd_ls[0], size=(200, 100))
    export(brd_ls[0], size=(2000, 1000))

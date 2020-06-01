from backports import tempfile
from path import Path

from eagexp.image3d import export_image3d

VISIBLE = 0
EXAMPLES = Path("/usr/share/eagle/projects/examples")


def export(fin, **kwargs):
    with tempfile.TemporaryDirectory() as temp_dir:
        fout = Path(temp_dir) / "out.png"
        export_image3d(fin, fout, showgui=VISIBLE, **kwargs)
        assert fout.exists()


def test_all():
    brd_ls = EXAMPLES.walkfiles("*.brd")
    brd_ls = list(brd_ls)

    for x in brd_ls:
        export(x)


def test_options():
    brd_ls = EXAMPLES.walkfiles("*.brd")
    brd_ls = list(brd_ls)

    export(brd_ls[0], timeout=65)
    export(brd_ls[0], size=(200, 100))
    export(brd_ls[0], size=(2000, 1000))

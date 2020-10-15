from os.path import exists, join

from backports import tempfile

from eagexp.image import export_image
from tutil import dir_files

VISIBLE = 0
EXAMPLES = "/usr/share/eagle/projects/examples"


def export(fin, **kwargs):
    with tempfile.TemporaryDirectory() as temp_dir:
        fout = join(temp_dir, "out.png")
        export_image(fin, fout, showgui=VISIBLE, **kwargs)
        assert exists(fout)


def test_all():
    sch_ls = dir_files(EXAMPLES, "*.sch")
    brd_ls = dir_files(EXAMPLES, "*.brd")
    all = sch_ls + brd_ls

    for x in all:
        export(x)


def test_options():
    sch_ls = dir_files(EXAMPLES, "*.sch")
    brd_ls = dir_files(EXAMPLES, "*.brd")
    all = sch_ls + brd_ls

    export(brd_ls[0], layers=["top"])
    export(brd_ls[0], layers=["top bottom"])

    export(brd_ls[0], mirror=1)

    export(brd_ls[0], command="display all")

    export(all[0], resolution=50)
    #        export(all[0], resolution=300)
    #        export(all[0], resolution=1000)

    export(all[0], palette=None)
    export(all[0], palette="white")
    export(all[0], palette="black")
    export(all[0], palette="colored")

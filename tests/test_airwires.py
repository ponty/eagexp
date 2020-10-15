from os.path import join

from eagexp.airwires import airwires
from tutil import dir_files

EXAMPLES = "/usr/share/eagle/projects/examples"


def test_values():
    assert airwires(join(EXAMPLES, "singlesided/singlesided.brd")) == 39
    assert airwires(join(EXAMPLES, "tutorial/demo2.brd")) == 0


def air(fin, **kwargs):
    print(airwires(fin, **kwargs))


def test_all():
    # sch_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.sch')
    brd_ls = dir_files(EXAMPLES, "*.brd")
    #        all = sch_ls + brd_ls

    for x in brd_ls:
        air(x)

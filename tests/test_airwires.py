from path import Path

from eagexp.airwires import airwires

EXAMPLES = Path("/usr/share/eagle/projects/examples")


def test_values():
    assert airwires(EXAMPLES / "singlesided/singlesided.brd") == 39
    assert airwires(EXAMPLES / "tutorial/demo2.brd") == 0


def air(fin, **kwargs):
    print(airwires(fin, **kwargs))


def test_all():
    # sch_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.sch')
    brd_ls = EXAMPLES.walkfiles("*.brd")
    #        sch_ls = list(sch_ls)
    brd_ls = list(brd_ls)
    #        all = sch_ls + brd_ls

    for x in brd_ls:
        air(x)

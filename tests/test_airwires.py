from eagexp.airwires import airwires
from nose.tools import eq_
from unittest import TestCase
from path import Path


def test_values():
    eq_(airwires('~/.eagle/projects/examples/singlesided/singlesided.brd'), 39)
    eq_(airwires('~/.eagle/projects/examples/tutorial/demo2.brd'), 0)


def air(fin, **kwargs):
    print(airwires(fin, **kwargs))


class Test(TestCase):

    def test_all(self):
# sch_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.sch')
        brd_ls = Path(
            '~/.eagle/projects/examples/').expand().walkfiles('*.brd')
#        sch_ls = list(sch_ls)
        brd_ls = list(brd_ls)
#        all = sch_ls + brd_ls

        for x in brd_ls:
            air(x)

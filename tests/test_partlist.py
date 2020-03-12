from eagexp.partlist import raw_partlist, structured_partlist
from path import Path
from pprint import pprint
from unittest import TestCase

EXAMPLES = Path("/usr/share/eagle/projects/examples")


def export(fin, **kwargs):
    pprint(raw_partlist(fin, **kwargs), width=1)
    pprint(structured_partlist(fin, **kwargs), width=1)


def check_dir(d):
    sch_ls = Path(d).expand().walkfiles("*.sch")
    brd_ls = Path(d).expand().walkfiles("*.brd")
    sch_ls = list(sch_ls)
    brd_ls = list(brd_ls)
    all = sch_ls + brd_ls

    for x in all:
        export(x)


class Test(TestCase):
    def test_examples(self):
        check_dir(EXAMPLES)

    def test_data(self):
        data = Path(__file__).parent / "data"
        check_dir(data)

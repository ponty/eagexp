from eagexp.partlist import raw_partlist, structured_partlist
from nose.tools import eq_
from path import path
from prettyprint.prettyprint import pp
from unipath.path import Path
from unittest import TestCase
import tempfile


def export(fin, **kwargs):
    pp(raw_partlist(fin, **kwargs))
    pp(structured_partlist(fin, **kwargs))
    
class Test(TestCase):       
    def test(self):
        sch_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.sch')
        brd_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.brd')
        sch_ls = list(sch_ls)
        brd_ls = list(brd_ls)
        all = sch_ls + brd_ls

        for x in all:
            export(x)
        
        

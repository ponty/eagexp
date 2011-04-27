from eagexp.partlist import raw_partlist, structured_partlist
from nose.tools import eq_
from path import path
from prettyprint.prettyprint import pp
from unipath.path import Path
from unittest import TestCase
import tempfile


def export(fin, **kwargs):
    #fout = tempfile.NamedTemporaryFile(suffix='.partlist', delete=0)
    #fout = Path(fout.name)
    #export_partlist(fin, fout, **kwargs)
    #data = parse_partlist(fout.read_file())
    pp(raw_partlist(fin, **kwargs))
    pp(structured_partlist(fin, **kwargs))
    #path(fout.name).remove()
    
class Test(TestCase):       
    def test(self):
        sch_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.sch')
        brd_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.brd')
        sch_ls = list(sch_ls)
        brd_ls = list(brd_ls)
        all = sch_ls + brd_ls

        for x in all:
            export(x)
        
        

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

def check_dir(d):
    sch_ls = path(d).expand().walkfiles('*.sch')
    brd_ls = path(d).expand().walkfiles('*.brd')
    sch_ls = list(sch_ls)
    brd_ls = list(brd_ls)
    all = sch_ls + brd_ls

    for x in all:
        export(x)
    
class Test(TestCase):       
    def test_examples(self):
        check_dir('~/.eagle/projects/examples/')
    
    def test_data(self):
        data = path(__file__).parent / 'data'
        check_dir(data)
        
        

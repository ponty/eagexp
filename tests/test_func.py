from eagexp.image import export_image
from nose.tools import eq_
from path import path
from unipath.path import Path
from unittest import TestCase
import tempfile

VISIBLE=0

def export(fin, **kwargs):
    fout = tempfile.NamedTemporaryFile(prefix='eagexp_test_', suffix='.png', delete=0)
    fout=Path(fout.name)
    export_image(fin, fout, showgui=VISIBLE, **kwargs)
    assert fout.exists() 
    #path(fout.name).remove()

class Test(TestCase):       
    def test_all(self):
        sch_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.sch')
        brd_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.brd')
        sch_ls = list(sch_ls)
        brd_ls = list(brd_ls)
        all = sch_ls + brd_ls

        for x in all:
            export(x)
        
    def test_options(self):
        sch_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.sch')
        brd_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.brd')
        sch_ls = list(sch_ls)
        brd_ls = list(brd_ls)
        all = sch_ls + brd_ls

        
        export(brd_ls[0], layers=['top'])
        export(brd_ls[0], layers=['top bottom'])
        
        export(brd_ls[0], mirror=1)
        
        export(brd_ls[0], command='display all')
        
        export(all[0], resolution=50)
        export(all[0], resolution=300)
        export(all[0], resolution=1000)
        
        export(all[0], palette=None)
        export(all[0], palette='white')
        export(all[0], palette='black')
        export(all[0], palette='colored')
        

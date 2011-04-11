from eag2img import export_eagle_image
from nose.tools import eq_
from path import path
from unittest import TestCase
import tempfile


def export(fin, **kwargs):
    fout = tempfile.NamedTemporaryFile(suffix='.png', delete=0)
    export_eagle_image(fin, fout.name, **kwargs)
    #path(fout.name).remove()

class Test(TestCase):
       
    def test(self):
        eq_(0, 0)
        sch_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.sch')
        brd_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.brd')
        sch_ls = list(sch_ls)
        brd_ls = list(brd_ls)
        all = sch_ls + brd_ls
        for x in all:
            export(x)
        
        export(all[0], resolution=50)
        export(all[0], resolution=300)
        export(all[0], resolution=1000)
        
        export(all[0], palette=None)
        export(all[0], palette='white')
        export(all[0], palette='black')
        export(all[0], palette='colored')
        
        
        

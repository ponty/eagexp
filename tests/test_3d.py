from eagexp.image3d import export_image3d
from path import path
from unittest import TestCase
import tempfile

VISIBLE=0

def export(fin, **kwargs):
    fout = tempfile.NamedTemporaryFile(prefix='eagexp_test_', suffix='.png', delete=0)
    fout=path(fout.name)
    export_image3d(fin, fout, showgui=VISIBLE, **kwargs)
    assert fout.exists() 
    #path(fout.name).remove()

class Test(TestCase):       
    def test_all(self):
        brd_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.brd')
        brd_ls = list(brd_ls)

        for x in brd_ls:
            export(x)
        
    def test_options(self):
        brd_ls = path('~/.eagle/projects/examples/').expand().walkfiles('*.brd')
        brd_ls = list(brd_ls)

        
        export(brd_ls[0], timeout=65)
        export(brd_ls[0], size=(200,100))
        export(brd_ls[0], size=(2000,1000))

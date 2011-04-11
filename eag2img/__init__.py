from easyprocess import Proc
from entrypoint import entrypoint
import logging
import os
import shutil
import tempfile
import threading

USE_DISPLAY = 0
try:
    from pyvirtualdisplay.display import Display
    USE_DISPLAY = 1
except:
    import warnings
    warnings.warn('pyvirtualdisplay was not found, no background GUI work is possible')



__version__ = '0.0.0'

log = logging.getLogger(__name__)
#log=logging

log.debug('version=' + __version__)

VISIBLE = 0

@entrypoint
def export_eagle_image(fin, fout, timeout=20, palette='white', resolution=150):
    '''palette=[None,black,white,colored]
    resolution=The resolution parameter defines the image resolution (in 'dpi'). 
    
    Exporting an IMAGE generates an image file with a format corresponding 
    to the given filename extension. 
    The following image formats are available: 

    .bmp    Windows Bitmap Files
    .png    Portable Network Graphics Files
    .pbm    Portable Bitmap Files
    .pgm    Portable Grayscale Bitmap Files
    .ppm    Portable Pixelmap Files
    .tif    TIFF Files
    .xbm    X Bitmap Files
    .xpm    X Pixmap Files

    '''
    resolution = int(resolution)
    def normpath(f):
        return os.path.abspath(os.path.expandvars(os.path.expanduser(f)))
        
    fin = normpath(fin)
    fout = normpath(fout)
    
    #with dot
    ext = os.path.splitext(fin)[1]
    assert ext in ['.brd', '.sch']
    
    # popup window is displayed, if outfile exists
    if os.path.exists(fout):
        os.remove(fout)
    
    script = ''
    
    undo = 0
    
    # this method does not work:
    # both sch and brd windows can be opened,
    # so we should activate the correct one
    #script += 'EDIT {ext};'.format(ext=ext)
    
    
    # copy input into empty directory, otherwise both sch and brd will be opened
    tdir = tempfile.mkdtemp(prefix='eag2img')
    tfin = os.path.join(tdir, os.path.split(fin)[1])
    shutil.copy(fin, tfin)
    
    if palette is not None:
        script += 'SET PALETTE {palette};'.format(palette=palette)
        undo += 1
    
    # redraw
    script += 'WINDOW;'
    
    script += 'EXPORT IMAGE {fout} {resolution};'.format(fout=fout, resolution=resolution)
    
    for x in range(undo):
        # make UNDO, otherwise popup is displayed
        script += 'UNDO;'
    
    script += 'QUIT;'
    
    # this method is not used currently
    # write script into file
    #fscript = tempfile.NamedTemporaryFile(suffix='.scr', delete=0)
    #fscript.write(script)
    #cmd = ['eagle', '-C SCRIPT '+ fscript.name+'', fin]
    
    cmd = ['eagle', '-C ' + script, tfin]
    
    def call_eagle():    
        p = Proc(cmd).call(timeout=timeout)
        assert p.return_code == 0, 'eagle return code is not zero'
    
    if USE_DISPLAY:
        f = Display(visible=VISIBLE, size=(800, 600)).wrap(call_eagle)
        f()
    else:
        call_eagle()
    
    shutil.rmtree(tdir)
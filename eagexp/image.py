from eagexp import __version__
from eagexp.exp import export_eagle
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)
log.debug('version=' + __version__)



@entrypoint
def export_image(input, output, timeout=20, palette='white', resolution=150, showgui=False):
    '''    
    Exporting eagle .sch or .brd file into image file.
    GUI is not displayed if PyVirtualDisplay is installed.
    If export is blocked somehow (e.g. popup window is displayed) then after timeout operation is canceled with exception.
    Problem can be investigated by setting 'showgui' flag.
        
    Exporting generates an image file with a format corresponding 
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

    :param input: eagle .sch or .brd file name
    :param output: image file name, existing file will be removed first!
    :param palette: background color [None,black,white,colored]
    :param resolution: image resolution in dpi (50..2400)
    :param timeout: operation is canceled after this timeout (sec) 
    :param showgui: eagle GUI is displayed
    :rtype: None
    '''
        
    if palette:
        palette = palette.lower()
        
    if palette == 'none':
        palette = None
            
    if palette is not None:
        commands = ['SET PALETTE {palette};'.format(palette=palette)]
    else:
        commands=[]
    export_eagle(input=input, output=output, output_type='image',
                 timeout=timeout, commands=commands, showgui=showgui, 
                 resolution=resolution)
    


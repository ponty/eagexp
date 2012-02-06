from eagexp import __version__
from eagexp.cmd import command_eagle
from eagexp.exp import export_command
from eagexp.util import norm_path
from entrypoint2 import entrypoint
from path import path
import Image
import ImageOps
import logging
import tempfile

log = logging.getLogger(__name__)
log.debug('version=' + __version__)



@entrypoint
def export_image(input, output, timeout=20, palette='white', resolution=150, layers=None, command=None, mirror=False, showgui=False):
    '''    
    Exporting eagle .sch or .brd file into image file.
    GUI is not displayed if ``pyvirtualdisplay`` is installed.
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
    :param layers: list, layers to be displayed ['top','pads'] 
    :param command: string, direct eagle command
    :param mirror: Bool
    :rtype: None
    '''
    input=norm_path(input)
    output=norm_path(output)
        
    if palette:
        palette = palette.lower()
        
    if palette == 'none':
        palette = None
            
    cmds = []
    if palette is not None:
        cmds += ['SET PALETTE {palette}'.format(palette=palette)]

    if layers is not None:
        cmds += ['DISPLAY NONE ' + ' '.join(layers)]
        
    if command is not None:
        cmds += [command]

    if mirror:
        f = tempfile.NamedTemporaryFile(suffix='.png', prefix='eagexp_')
        fout = f.name
    else:
        fout = output

    commands = export_command(output=fout, output_type='image',
                              commands=cmds, resolution=resolution)
    command_eagle(input=input, timeout=timeout, commands=commands, showgui=showgui)

    if mirror:
        im = Image.open(fout)
        # save dpi info
        info = im.info
        im = ImageOps.mirror(im)
        im.save(output, **info)




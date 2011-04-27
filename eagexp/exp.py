from eagexp import USE_DISPLAY
from easyprocess import Proc
from pyvirtualdisplay import Display
import os
import shutil
import tempfile


class EagleError(Exception):
    '''eagexp error'''


def export_eagle(input, output, output_type, timeout=60, commands=[], showgui=False, resolution=None):
    def normpath(f):
        return os.path.abspath(os.path.expandvars(os.path.expanduser(f)))
        
    input = normpath(input)
    output = normpath(output)

    if resolution:
        resolution = int(resolution)
        if resolution > 2400 or resolution < 50:
            raise ValueError('resolution should be inrange 50-2400! current=' + str(resolution))
    else:
        resolution = ''
    
    if not commands:
        commands = []
    #with dot
    ext = os.path.splitext(input)[1]
    if ext not in ['.brd', '.sch']:
        raise ValueError('Input extension is not in [.brd, .sch], input=' + str(input))
    
    # popup window is displayed, if outfile exists
    if os.path.exists(output):
        os.remove(output)
    
    script = ''
    
    undo = 0
    
    # this method does not work:
    # both sch and brd windows can be opened,
    # so we should activate the correct one
    #script += 'EDIT {ext};'.format(ext=ext)
    
    
    # copy input into empty directory, otherwise both sch and brd will be opened
    tmp_dir = tempfile.mkdtemp(prefix='eagexp')
    tmp_input = os.path.join(tmp_dir, os.path.split(input)[1])
    shutil.copy(input, tmp_input)
    
    for x in commands:
        script += x
        undo += 1
    
    # redraw
    script += 'WINDOW;'
    
    script += 'EXPORT {output_type} {output} {resolution};'.format(
        output_type=output_type,output=output, resolution=resolution)
    
    for x in range(undo):
        # make UNDO, otherwise popup is displayed
        script += 'UNDO;'
    
    script += 'QUIT;'
    
    # this method is not used currently
    # write script into file
    #fscript = tempfile.NamedTemporaryFile(suffix='.scr', delete=0)
    #fscript.write(script)
    #cmd = ['eagle', '-C SCRIPT '+ fscript.name+'', input]
    
    cmd = ['eagle', '-C ' + script, tmp_input]
    
    def call_eagle():    
        p = Proc(cmd).call(timeout=timeout)
        if p.return_code != 0:
            raise EagleError('eagle return code is not zero, proc=' + str(p))

    if USE_DISPLAY:
        f = Display(visible=showgui, size=(800, 600)).wrap(call_eagle)
        f()
    else:
        call_eagle()
    
    shutil.rmtree(tmp_dir)


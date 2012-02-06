from eagexp import USE_DISPLAY
from eagexp.util import norm_path
from easyprocess import Proc
from path import path
from pyvirtualdisplay import Display
import os
import shutil
import tempfile


class EagleError(Exception):
    '''eagexp error'''


def command_eagle(input, commands=[], timeout=60, showgui=False, callback=None):
    input=norm_path(input)
    
    if not commands:
        commands = []
    #with dot
    ext = os.path.splitext(input)[1]
    if ext not in ['.brd', '.sch']:
        raise ValueError('Input extension is not in [.brd, .sch], input=' + str(input))
    
    
    # this method does not work:
    # both sch and brd windows can be opened,
    # so we should activate the correct one
    #script += 'EDIT {ext};'.format(ext=ext)
    
    
    # copy input into empty directory, otherwise both sch and brd will be opened
    tmp_dir = tempfile.mkdtemp(prefix='eagexp')
    tmp_input = os.path.join(tmp_dir, os.path.split(input)[1])
    shutil.copy(input, tmp_input)
    
    script = ''
    for x in commands:
        script += x
        script += ';'
    
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

    curdir=path.getcwd()
    curdir=norm_path(curdir)
    
    os.chdir(tmp_dir)

    if USE_DISPLAY:
        f = Display(visible=showgui, size=(800, 600)).wrap(call_eagle)
        f()
    else:
        call_eagle()
    
    os.chdir(curdir)

    if callback:
        callback(tmp_dir, tmp_input)

    shutil.rmtree(tmp_dir)


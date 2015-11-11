from eagexp import USE_DISPLAY
from eagexp.util import norm_path
from eagexp.version import version
from easyprocess import Proc, EasyProcess
import os
from path import Path
from pyvirtualdisplay import Display
import shutil
import tempfile
import time
# import pyscreenshot


TIMEOUT = 60


class EagleError(Exception):
    '''eagexp error'''
    
def accept_freeware_license():
    '''different Eagle versions need differnt TAB count.
    6.5  -> 2
    6.6  -> 3
    7.4  -> 2
    '''
    ntab = 3 if version().startswith('6.6.') else 2
    for _ in range(ntab):
        EasyProcess('xdotool key KP_Tab').call()
        time.sleep(0.5)
    EasyProcess('xdotool key KP_Space').call()

    time.sleep(0.5)
    
    # say OK to any more question
    EasyProcess('xdotool key KP_Space').call()
    
def command_eagle(input, commands=[], timeout=TIMEOUT, showgui=False, callback=None):
    input = norm_path(input)

    if not commands:
        commands = []
    # with dot
    ext = os.path.splitext(input)[1]
    if ext not in ['.brd', '.sch']:
        raise ValueError(
            'Input extension is not in [.brd, .sch], input=' + str(input))

    # this method does not work:
    # both sch and brd windows can be opened,
    # so we should activate the correct one
    # script += 'EDIT {ext};'.format(ext=ext)
    # copy input into empty directory, otherwise both sch and brd will be
    # opened
    tmp_dir = tempfile.mkdtemp(prefix='eagexp')
    tmp_input = os.path.join(tmp_dir, os.path.split(input)[1])
    shutil.copy(input, tmp_input)

    script = ''
    for x in commands:
        script += x
        script += ';'

    # this method is not used currently
    # write script into file
    # fscript = tempfile.NamedTemporaryFile(suffix='.scr', delete=0)
    # fscript.write(script)
    # cmd = ['eagle', '-C SCRIPT '+ fscript.name+'', input]

    cmd = ['eagle', '-C ' + script, tmp_input]

    def call_eagle():
        t = 0
        accept_tries = 0
        with EasyProcess(cmd) as p:
            while p.is_alive():
                time.sleep(0.5)
                t += 0.5
                if t > timeout / 2:
                    if accept_tries == 0:
                        accept_freeware_license()
                        accept_tries += 1
                if t > timeout:
#                     pyscreenshot.grab_to_file('/vagrant/xxx.png')
                    raise EagleError('eagle return code is not zero, proc=' + str(p))
#                     break
                    
#         p = Proc(cmd).call(timeout=timeout)
#         if p.return_code != 0:
#             raise EagleError('eagle return code is not zero, proc=' + str(p))

    curdir = Path.getcwd()
    curdir = norm_path(curdir)

    os.chdir(tmp_dir)

    if USE_DISPLAY:
        with Display(visible=showgui, size=(800, 600)):
            time.sleep(1)
            call_eagle()
    else:
        call_eagle()

    os.chdir(curdir)

    if callback:
        callback(tmp_dir, tmp_input)

    shutil.rmtree(tmp_dir)

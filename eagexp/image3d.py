from eagexp import __version__
from eagexp.cmd import command_eagle, EagleError
from eagexp.util import norm_path
from easyprocess import Proc
from entrypoint2 import entrypoint
from path import path
import Image
import logging
import os
import tempfile

log = logging.getLogger(__name__)
log.debug('version=' + __version__)


@entrypoint
def export_image3d(input, output, size=(800, 600), pcb_rotate=(0, 0, 0), timeout=20, showgui=False):
    '''
    Exporting eagle .brd file into 3D image file
    using Eagle3D and povray.
    GUI is not displayed if ``pyvirtualdisplay`` is installed.
    If export is blocked somehow (e.g. popup window is displayed) then after timeout operation is canceled with exception.
    Problem can be investigated by setting 'showgui' flag.

    :param input: eagle .brd file name
    :param output: image file name (.png)
    :param timeout: operation is canceled after this timeout (sec)
    :param showgui: eagle GUI is displayed
    :param size: tuple(width, size), image size
    :rtype: None
    '''
    input = norm_path(input)
    output = norm_path(output)

    ext = os.path.splitext(input)[1]
    if ext not in ['.brd']:
        raise ValueError('Input extension is not ".brd", brd=' + str(input))

    commands = []
    eagle3d = path(__file__).dirname() / 'eagle3d'
    ulp = (eagle3d / '3d50.ulp').abspath()

    commands += ['RUN ' + ulp]
    commands += ['QUIT']

    def render(dir, f):
        # povray has strange file access policy,
        # better to generate under tmp

        # cli doc:
        # http://library.thinkquest.org/3285/language/cmdln.html

        templ = '#local pcb_rotate_%s = %s'
        pov = path(f.replace('.brd', '.pov'))
        if pcb_rotate != (0, 0, 0):
            s = pov.text()
            s = s.replace(templ % ('x', 0), templ % ('x', pcb_rotate[0]))
            s = s.replace(templ % ('y', 0), templ % ('y', pcb_rotate[1]))
            s = s.replace(templ % ('z', 0), templ % ('z', pcb_rotate[2]))
            pov.write_text(s)
        fpng = path(f.replace('.brd', '.png'))
        cmd = []
        cmd += ["povray"]
        cmd += ["-d"]  # no display
        cmd += ["-a"]  # anti-aliasing
        cmd += ['+W' + str(size[0])]  # width
        cmd += ['+H' + str(size[1])]  # height
        cmd += ['-o' + fpng]
        cmd += ['-L' + eagle3d]
        cmd += [pov]
        p = Proc(cmd).call()
        if not fpng.exists():
            raise EagleError('povray error, proc=' + str(p))
        fpng.copy(output)

    command_eagle(input=input, timeout=timeout, commands=commands,
                  showgui=showgui, callback=render)


def pil_image3d(input, size=(800, 600), pcb_rotate=(0, 0, 0), timeout=20, showgui=False):
    '''
    same as export_image3d, but there is no output file, PIL object is returned instead
    '''
    f = tempfile.NamedTemporaryFile(suffix='.png', prefix='eagexp_')
    output = f.name

    export_image3d(input, output=output, size=size,
                   pcb_rotate=pcb_rotate, timeout=timeout, showgui=showgui)

    im = Image.open(output)
    return im

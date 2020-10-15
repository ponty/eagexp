import logging
import os
from os.path import dirname, exists, join
from shutil import copy

from backports import tempfile
from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from PIL import Image

from eagexp import __version__
from eagexp.cmd import EagleError, command_eagle
from eagexp.util import norm_path, read_text, write_text

log = logging.getLogger(__name__)
log.debug("version=" + __version__)


@entrypoint
def export_image3d(
    input, output, size=(800, 600), pcb_rotate=(0, 0, 0), timeout=20, showgui=False
):
    """
    Exporting eagle .brd file into 3D image file
    using Eagle3D and povray.
    If export is blocked somehow (e.g. popup window is displayed) then after timeout operation is canceled with exception.
    Problem can be investigated by setting 'showgui' flag.

    :param input: eagle .brd file name
    :param output: image file name (.png)
    :param timeout: operation is canceled after this timeout (sec)
    :param showgui: eagle GUI is displayed
    :param size: tuple(width, size), image size
    :rtype: None
    """
    input = norm_path(input)
    output = norm_path(output)
    if not output.endswith(".png"):
        raise ValueError("use .png extension!")

    ext = os.path.splitext(input)[1]
    if ext not in [".brd"]:
        raise ValueError('Input extension is not ".brd", brd=' + str(input))

    commands = []
    eagle3d = join(dirname(__file__), "eagle3d")
    ulp = norm_path(join(eagle3d, "3d50.ulp"))

    commands += ["RUN " + ulp]
    commands += ["QUIT"]

    def render(dir, f):
        # povray has strange file access policy,
        # better to generate under tmp

        # cli doc:
        # http://library.thinkquest.org/3285/language/cmdln.html

        templ = "#local pcb_rotate_%s = %s"
        pov = f.replace(".brd", ".pov")
        if not exists(pov):
            raise EagleError("missing pov file: %s" % pov)
        # log.debug("pov file %s content: %s", pov, pov.read_text())
        if pcb_rotate != (0, 0, 0):
            s = read_text(pov)
            s = s.replace(templ % ("x", 0), templ % ("x", pcb_rotate[0]))
            s = s.replace(templ % ("y", 0), templ % ("y", pcb_rotate[1]))
            s = s.replace(templ % ("z", 0), templ % ("z", pcb_rotate[2]))
            write_text(pov, s)
        fpng = f.replace(".brd", ".png")
        cmd = []
        cmd += ["povray"]
        cmd += ["-d"]  # no display
        cmd += ["-a"]  # anti-aliasing
        cmd += ["+W" + str(size[0])]  # width
        cmd += ["+H" + str(size[1])]  # height
        cmd += ["-o" + fpng]
        cmd += ["-L" + eagle3d]
        cmd += [pov]
        p = EasyProcess(cmd).call()
        if not exists(fpng):
            raise EagleError("povray error, proc=%s" % p)
        copy(fpng, output)

    command_eagle(
        input=input,
        timeout=timeout,
        commands=commands,
        showgui=showgui,
        callback=render,
    )


def pil_image3d(
    input, size=(800, 600), pcb_rotate=(0, 0, 0), timeout=20, showgui=False
):
    """
    same as export_image3d, but there is no output file, PIL object is returned instead
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        output = join(temp_dir, "out.png")

        export_image3d(
            input,
            output=output,
            size=size,
            pcb_rotate=pcb_rotate,
            timeout=timeout,
            showgui=showgui,
        )

        im = Image.open(output)
        return im

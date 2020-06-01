import logging
import tempfile

from entrypoint2 import entrypoint
from PIL import Image, ImageOps

from eagexp import __version__
from eagexp.cmd import command_eagle
from eagexp.exp import export_command
from eagexp.util import norm_path

log = logging.getLogger(__name__)
log.debug("version=" + __version__)


@entrypoint
def export_image(
    input,
    output,
    timeout=20,
    palette="white",
    resolution=150,
    layers=None,
    command=None,
    mirror=False,
    showgui=False,
):
    """
    Exporting eagle .sch or .brd file into image file.
    If export is blocked somehow (e.g. popup window is displayed) then after timeout operation is canceled with exception.
    Problem can be investigated by setting 'showgui' flag.
    Exporting generates an image file. Only PNG format is supported

    :param input: eagle .sch or .brd file name
    :param output: image file name (e.g. 'eagle.png')
    :param palette: background color [None,black,white,colored]
    :param resolution: image resolution in dpi (50..2400)
    :param timeout: operation is canceled after this timeout (sec)
    :param showgui: eagle GUI is displayed
    :param layers: list, layers to be displayed ['top','pads']
    :param command: string, direct eagle command
    :param mirror: Bool
    :rtype: None
    """
    input = norm_path(input)
    output = norm_path(output)
    if not output.endswith(".png"):
        raise ValueError("use .png extension!")

    if palette:
        palette = palette.lower()

    if palette == "none":
        palette = None

    cmds = []
    if palette is not None:
        cmds += ["SET PALETTE {palette}".format(palette=palette)]

    if layers is not None:
        cmds += ["DISPLAY NONE " + " ".join(layers)]

    if command is not None:
        cmds += [command]

    if mirror:
        f = tempfile.NamedTemporaryFile(suffix=".png", prefix="eagexp_")
        fout = f.name
    else:
        fout = output

    commands = export_command(
        output=fout, output_type="image", commands=cmds, resolution=resolution
    )
    command_eagle(input=input, timeout=timeout, commands=commands, showgui=showgui)

    if mirror:
        im = Image.open(fout)
        # save dpi info
        info = im.info
        im = ImageOps.mirror(im)
        im.save(output, **info)

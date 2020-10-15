from os.path import join

from backports import tempfile
from easyprocess import EasyProcess
from pyvirtualdisplay.display import Display

from tutil import dir_files

EXAMPLES = "/usr/share/eagle/projects/examples"


def export(params, fail=0):
    # mod=path(__file__).parent.parent / 'eagexp.py'
    # cmd='python '+mod+' '+params
    cmd = "python -m eagexp.image " + params
    p = EasyProcess(cmd).call()
    if fail:
        assert p.return_code != 0
    else:
        assert p.return_code == 0


def test():
    with tempfile.TemporaryDirectory() as temp_dir:
        o = join(temp_dir, "out.png")

        sch_ls = dir_files(EXAMPLES, "*.sch")
        brd_ls = dir_files(EXAMPLES, "*.brd")
        all = sch_ls + brd_ls

        i = all[0]

        export("-h")
        export("--help")
        export("-xxx", fail=1)

        export("%s %s" % (i, o))
        export("--debug %s %s" % (i, o))
        export("%s %s --debug" % (i, o))

        # test palette
        export("--timeout 200 %s %s" % (i, o))
        export("--timeout x200 %s %s" % (i, o), fail=1)

        # test palette
        export("--palette none %s %s" % (i, o))
        export("--palette colored %s %s" % (i, o))
        export("--palette white %s %s" % (i, o))
        export("--palette BLACK %s %s" % (i, o))
        export("--palette xxx", fail=1)

        # test resolution
        export("--resolution 50 %s %s" % (i, o))
        #        export('--resolution 500 %s %s' % (i,o))
        export("--resolution x200 %s %s" % (i, o), fail=1)

        # test showgui
        with Display():
            export("--showgui %s %s" % (i, o))

        for x in all:
            export("%s %s" % (x, o))

        # path(fout.name).remove()

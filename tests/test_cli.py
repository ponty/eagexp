from easyprocess import Proc
from nose.tools import eq_
from path import Path
from pyvirtualdisplay.display import Display
from unittest import TestCase
import tempfile

EXAMPLES = Path("/usr/share/eagle/projects/examples")


def export(params, fail=0):
    # mod=path(__file__).parent.parent / 'eagexp.py'
    # cmd='python '+mod+' '+params
    cmd = "python -m eagexp.image " + params
    p = Proc(cmd).call()
    if fail:
        eq_(p.return_code != 0, True)
    else:
        eq_(p.return_code, 0)


class Test(TestCase):
    def test(self):
        fout = tempfile.NamedTemporaryFile(suffix=".png", delete=0)
        o = fout.name

        sch_ls = EXAMPLES.walkfiles("*.sch")
        brd_ls = EXAMPLES.walkfiles("*.brd")
        sch_ls = list(sch_ls)
        brd_ls = list(brd_ls)
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
        def func():
            export("--showgui %s %s" % (i, o))

        Display().wrap(func)()

        for x in all:
            export("%s %s" % (x, o))

        # path(fout.name).remove()

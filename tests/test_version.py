from nose.tools import eq_

from eagexp.version import extract_version

V65 = """EAGLE Version 6.5.0 Copyright (c) 1988-2013 CadSoft
Syntax: eagle [options] [filename [layer...]]"""

V66 = """EAGLE Version 6.6.0 Copyright (c) 1988-2014 CadSoft
Syntax: eagle [options] [filename [layer...]]"""

V74 = """EAGLE Version 7.4.0 Copyright (c) 1988-2015 CadSoft
Syntax: eagle [options] [filename [layer...]]"""


def test_version():
    eq_("6.5.0", extract_version(V65))
    eq_("6.6.0", extract_version(V66))
    eq_("7.4.0", extract_version(V74))

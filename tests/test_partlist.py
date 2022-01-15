from os.path import dirname, join
from pprint import pprint

from tutil import dir_files

from eagexp.partlist import parse_partlist, raw_partlist, structured_partlist
from eagexp.util import norm_path

EXAMPLES = "/usr/share/eagle/projects/examples"


def export(fin, **kwargs):
    pprint(raw_partlist(fin, **kwargs), width=1)
    pprint(structured_partlist(fin, **kwargs), width=1)


def check_dir(d):
    sch_ls = dir_files(norm_path(d), "*.sch")
    brd_ls = dir_files(norm_path(d), "*.brd")
    sch_ls = list(sch_ls)
    brd_ls = list(brd_ls)
    all = sch_ls + brd_ls

    for x in all:
        export(x)


def test_examples():
    check_dir(EXAMPLES)


def test_data():
    data = join(dirname(__file__), "data")
    check_dir(data)


RAW_PARTLIST_singlesided_sch = """
  Partlist

  Exported from singlesided.sch at 2016.03.05. 8:58

  EAGLE Version 6.5.0 Copyright (c) 1988-2013 CadSoft

  Assembly variant:

  Part     Value          Device          Package      Library        Sheet

  C1       10u            E2,5-6          E2,5-6       polcap         1
  C2       10u            E2,5-6          E2,5-6       polcap         1
  C3       10n            C-EU025-025X050 C025-025X050 rcl            1
  C4       10n            C-EU025-025X050 C025-025X050 rcl            1
  C5       27p            C2.5/2          C2,5-2       capacitor-wima 1
  C6       27p            C2.5/2          C2,5-2       capacitor-wima 1
  D1       1N4148         1N4148          DO35-10      diode          1
  IC1      16F84          PIC16F84AP      DIL18        microchip      1
  J1                      PINHD-1X20      1X20         PINHEAD        1
  Q1                      XTAL/S          QS           special        1
  R1       2.2k           R-EU_0207/10    0207/10      rcl            1
  U1       78L05          78LXXZ          TO92         linear         1

  """

RAW_PARTLIST_singlesided_brd = """
  Partlist

  Exported from singlesided.brd at 2016.03.05. 8:58

  EAGLE Version 6.5.0 Copyright (c) 1988-2013 CadSoft

  Assembly variant:

  Part     Value          Package      Library        Position (mil)        Orientation

  C1       10u            E2,5-6       polcap         (1950 400)            R0
  C2       10u            E2,5-6       polcap         (1950 900)            R0
  C3       10n            C025-025X050 rcl            (1950 200)            R180
  C4       10n            C025-025X050 rcl            (1950 1100)           R180
  C5       27p            C2,5-2       capacitor-wima (1700 500)            R270
  C6       27p            C2,5-2       capacitor-wima (1250 250)            R90
  D1       1N4148         DO35-10      diode          (900 200)             R0
  IC1      16F84          DIL18        microchip      (1100 700)            R180
  J1                      1X20         PINHEAD        (1050 1400)           R180
  Q1                      QS           special        (1550 250)            R0
  R1       2.2k           0207/10      rcl            (900 350)             R0
  U1       78L05          TO92         linear         (1950 650)            R270

  """
PARTLIST_singlesided_sch = (
    [u"part", u"value", u"device", u"package", u"library", u"sheet"],
    [
        {
            u"sheet": u"1",
            u"package": u"E2,5-6",
            u"library": u"polcap",
            u"part": u"C1",
            u"value": u"10u",
            u"device": u"E2,5-6",
        },
        {
            u"sheet": u"1",
            u"package": u"E2,5-6",
            u"library": u"polcap",
            u"part": u"C2",
            u"value": u"10u",
            u"device": u"E2,5-6",
        },
        {
            u"sheet": u"1",
            u"package": u"C025-025X050",
            u"library": u"rcl",
            u"part": u"C3",
            u"value": u"10n",
            u"device": u"C-EU025-025X050",
        },
        {
            u"sheet": u"1",
            u"package": u"C025-025X050",
            u"library": u"rcl",
            u"part": u"C4",
            u"value": u"10n",
            u"device": u"C-EU025-025X050",
        },
        {
            u"sheet": u"1",
            u"package": u"C2,5-2",
            u"library": u"capacitor-wima",
            u"part": u"C5",
            u"value": u"27p",
            u"device": u"C2.5/2",
        },
        {
            u"sheet": u"1",
            u"package": u"C2,5-2",
            u"library": u"capacitor-wima",
            u"part": u"C6",
            u"value": u"27p",
            u"device": u"C2.5/2",
        },
        {
            u"sheet": u"1",
            u"package": u"DO35-10",
            u"library": u"diode",
            u"part": u"D1",
            u"value": u"1N4148",
            u"device": u"1N4148",
        },
        {
            u"sheet": u"1",
            u"package": u"DIL18",
            u"library": u"microchip",
            u"part": u"IC1",
            u"value": u"16F84",
            u"device": u"PIC16F84AP",
        },
        {
            u"sheet": u"1",
            u"package": u"1X20",
            u"library": u"PINHEAD",
            u"part": u"J1",
            u"value": u"",
            u"device": u"PINHD-1X20",
        },
        {
            u"sheet": u"1",
            u"package": u"QS",
            u"library": u"special",
            u"part": u"Q1",
            u"value": u"",
            u"device": u"XTAL/S",
        },
        {
            u"sheet": u"1",
            u"package": u"0207/10",
            u"library": u"rcl",
            u"part": u"R1",
            u"value": u"2.2k",
            u"device": u"R-EU_0207/10",
        },
        {
            u"sheet": u"1",
            u"package": u"TO92",
            u"library": u"linear",
            u"part": u"U1",
            u"value": u"78L05",
            u"device": u"78LXXZ",
        },
    ],
)

PARTLIST_singlesided_brd = (
    [u"part", u"value", u"package", u"library", u"position", u"orientation"],
    [
        {
            u"orientation": u"R0",
            u"package": u"E2,5-6",
            u"library": u"polcap",
            u"part": u"C1",
            u"value": u"10u",
            u"position": u"(1950 400)",
        },
        {
            u"orientation": u"R0",
            u"package": u"E2,5-6",
            u"library": u"polcap",
            u"part": u"C2",
            u"value": u"10u",
            u"position": u"(1950 900)",
        },
        {
            u"orientation": u"R180",
            u"package": u"C025-025X050",
            u"library": u"rcl",
            u"part": u"C3",
            u"value": u"10n",
            u"position": u"(1950 200)",
        },
        {
            u"orientation": u"R180",
            u"package": u"C025-025X050",
            u"library": u"rcl",
            u"part": u"C4",
            u"value": u"10n",
            u"position": u"(1950 1100)",
        },
        {
            u"orientation": u"R270",
            u"package": u"C2,5-2",
            u"library": u"capacitor-wima",
            u"part": u"C5",
            u"value": u"27p",
            u"position": u"(1700 500)",
        },
        {
            u"orientation": u"R90",
            u"package": u"C2,5-2",
            u"library": u"capacitor-wima",
            u"part": u"C6",
            u"value": u"27p",
            u"position": u"(1250 250)",
        },
        {
            u"orientation": u"R0",
            u"package": u"DO35-10",
            u"library": u"diode",
            u"part": u"D1",
            u"value": u"1N4148",
            u"position": u"(900 200)",
        },
        {
            u"orientation": u"R180",
            u"package": u"DIL18",
            u"library": u"microchip",
            u"part": u"IC1",
            u"value": u"16F84",
            u"position": u"(1100 700)",
        },
        {
            u"orientation": u"R180",
            u"package": u"1X20",
            u"library": u"PINHEAD",
            u"part": u"J1",
            u"value": u"",
            u"position": u"(1050 1400)",
        },
        {
            u"orientation": u"R0",
            u"package": u"QS",
            u"library": u"special",
            u"part": u"Q1",
            u"value": u"",
            u"position": u"(1550 250)",
        },
        {
            u"orientation": u"R0",
            u"package": u"0207/10",
            u"library": u"rcl",
            u"part": u"R1",
            u"value": u"2.2k",
            u"position": u"(900 350)",
        },
        {
            u"orientation": u"R270",
            u"package": u"TO92",
            u"library": u"linear",
            u"part": u"U1",
            u"value": u"78L05",
            u"position": u"(1950 650)",
        },
    ],
)
# -#


def test_parse():
    assert parse_partlist(RAW_PARTLIST_singlesided_sch) == PARTLIST_singlesided_sch

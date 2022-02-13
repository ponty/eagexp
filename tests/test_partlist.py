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
    ["part", "value", "device", "package", "library", "sheet"],
    [
        {
            "sheet": "1",
            "package": "E2,5-6",
            "library": "polcap",
            "part": "C1",
            "value": "10u",
            "device": "E2,5-6",
        },
        {
            "sheet": "1",
            "package": "E2,5-6",
            "library": "polcap",
            "part": "C2",
            "value": "10u",
            "device": "E2,5-6",
        },
        {
            "sheet": "1",
            "package": "C025-025X050",
            "library": "rcl",
            "part": "C3",
            "value": "10n",
            "device": "C-EU025-025X050",
        },
        {
            "sheet": "1",
            "package": "C025-025X050",
            "library": "rcl",
            "part": "C4",
            "value": "10n",
            "device": "C-EU025-025X050",
        },
        {
            "sheet": "1",
            "package": "C2,5-2",
            "library": "capacitor-wima",
            "part": "C5",
            "value": "27p",
            "device": "C2.5/2",
        },
        {
            "sheet": "1",
            "package": "C2,5-2",
            "library": "capacitor-wima",
            "part": "C6",
            "value": "27p",
            "device": "C2.5/2",
        },
        {
            "sheet": "1",
            "package": "DO35-10",
            "library": "diode",
            "part": "D1",
            "value": "1N4148",
            "device": "1N4148",
        },
        {
            "sheet": "1",
            "package": "DIL18",
            "library": "microchip",
            "part": "IC1",
            "value": "16F84",
            "device": "PIC16F84AP",
        },
        {
            "sheet": "1",
            "package": "1X20",
            "library": "PINHEAD",
            "part": "J1",
            "value": "",
            "device": "PINHD-1X20",
        },
        {
            "sheet": "1",
            "package": "QS",
            "library": "special",
            "part": "Q1",
            "value": "",
            "device": "XTAL/S",
        },
        {
            "sheet": "1",
            "package": "0207/10",
            "library": "rcl",
            "part": "R1",
            "value": "2.2k",
            "device": "R-EU_0207/10",
        },
        {
            "sheet": "1",
            "package": "TO92",
            "library": "linear",
            "part": "U1",
            "value": "78L05",
            "device": "78LXXZ",
        },
    ],
)

PARTLIST_singlesided_brd = (
    ["part", "value", "package", "library", "position", "orientation"],
    [
        {
            "orientation": "R0",
            "package": "E2,5-6",
            "library": "polcap",
            "part": "C1",
            "value": "10u",
            "position": "(1950 400)",
        },
        {
            "orientation": "R0",
            "package": "E2,5-6",
            "library": "polcap",
            "part": "C2",
            "value": "10u",
            "position": "(1950 900)",
        },
        {
            "orientation": "R180",
            "package": "C025-025X050",
            "library": "rcl",
            "part": "C3",
            "value": "10n",
            "position": "(1950 200)",
        },
        {
            "orientation": "R180",
            "package": "C025-025X050",
            "library": "rcl",
            "part": "C4",
            "value": "10n",
            "position": "(1950 1100)",
        },
        {
            "orientation": "R270",
            "package": "C2,5-2",
            "library": "capacitor-wima",
            "part": "C5",
            "value": "27p",
            "position": "(1700 500)",
        },
        {
            "orientation": "R90",
            "package": "C2,5-2",
            "library": "capacitor-wima",
            "part": "C6",
            "value": "27p",
            "position": "(1250 250)",
        },
        {
            "orientation": "R0",
            "package": "DO35-10",
            "library": "diode",
            "part": "D1",
            "value": "1N4148",
            "position": "(900 200)",
        },
        {
            "orientation": "R180",
            "package": "DIL18",
            "library": "microchip",
            "part": "IC1",
            "value": "16F84",
            "position": "(1100 700)",
        },
        {
            "orientation": "R180",
            "package": "1X20",
            "library": "PINHEAD",
            "part": "J1",
            "value": "",
            "position": "(1050 1400)",
        },
        {
            "orientation": "R0",
            "package": "QS",
            "library": "special",
            "part": "Q1",
            "value": "",
            "position": "(1550 250)",
        },
        {
            "orientation": "R0",
            "package": "0207/10",
            "library": "rcl",
            "part": "R1",
            "value": "2.2k",
            "position": "(900 350)",
        },
        {
            "orientation": "R270",
            "package": "TO92",
            "library": "linear",
            "part": "U1",
            "value": "78L05",
            "position": "(1950 650)",
        },
    ],
)
# -#


def test_parse():
    assert parse_partlist(RAW_PARTLIST_singlesided_sch) == PARTLIST_singlesided_sch

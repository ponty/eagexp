eagexp can export eagle_ partlist or image (2D/3D) of schematic or board.

Links:
 * home: https://github.com/ponty/eagexp
 * PYPI: https://pypi.python.org/pypi/eagexp

|Travis| |License|

Features:
 - written in python
 - it can be used as library or as a command line program
 - headless processing using Xvfb_ and pyvirtualdisplay_
 - timeout
 - 3D image export using Eagle3D and povray_
 - calculate airwires
 
Known problems:
 - slow: eagle is opened and closed for each export
 - high DPI does not work (memory problem?)
   
Basic usage
===========

    >>> from eagexp import image, partlist
    >>> brd='~/.eagle/projects/examples/singlesided/singlesided.brd'
    >>> image.export_image(brd, 'brd.png', resolution=600)
    >>> print partlist.raw_partlist(brd)


How it works
============

#. start Xvfb_ headless X server using pyvirtualdisplay_
#. redirect eagle display to Xvfb server by setting $DISPLAY variable.
#. start eagle_ with EXPORT and QUIT commands


Installation
============

General
-------

 * install eagle_
 * install povray_ (optional for 3D)
 * install PIL_
 * install pyvirtualdisplay_ , Xvfb_
 * install the program:

    python3 -m pip install eagexp


Ubuntu 14.04
------------
:

    sudo apt-get install eagle povray  python-pil xvfb xdotool
    python3 -m  pip install eagexp
    

Usage
=====


Export from python code
-----------------------

Example:

```py
# eagexp/examples/image_example.py

"""
Example for image export with various options
"""

from eagexp import image

brd = "/usr/share/eagle/projects/examples/tutorial/demo2.brd"

if __name__ == "__main__":
    # set resolution in DPI
    image.export_image(brd, "api_brd_50.png", resolution=50)
    image.export_image(brd, "api_brd_100.png", resolution=100)
    image.export_image(brd, "api_brd_150.png", resolution=150)

    # mirror image
    image.export_image(brd, "api_brd_mirror.png", mirror=True)

    # display only 2 layers
    image.export_image(brd, "api_brd_layer.png", layers=["dimension", "pads"])

    # display layer using eagle command
    image.export_image(brd, "api_brd_command.png", command="display none dimension")

```

<!-- embedme doc/gen/python3_-m_eagexp.examples.image_example.txt -->
Run it:
```console
$ python3 -m eagexp.examples.image_example

```

Result:

![](/doc/gen/api_brd_50.png)
![](/doc/gen/api_brd_100.png)
![](/doc/gen/api_brd_150.png)
![](/doc/gen/api_brd_mirror.png)
![](/doc/gen/api_brd_layer.png)
![](/doc/gen/api_brd_command.png)


Example for 3D:

```py
# eagexp/examples/image3d_example.py

"""
Example for 3D image export
"""
from eagexp import image3d

brd = "/usr/share/eagle/projects/examples/tutorial/demo2.brd"

if __name__ == "__main__":
    image3d.export_image3d(brd, "api_3d.png")

    # size
    image3d.export_image3d(brd, "api_3d_size1.png", size=(50, 50))
    image3d.export_image3d(brd, "api_3d_size2.png", size=(50, 100))
    image3d.export_image3d(brd, "api_3d_size3.png", size=(100, 50))

    # rotate
    image3d.export_image3d(
        brd, "api_3d_xrot.png", pcb_rotate=(180, 0, 0), size=(200, 150)
    )
    image3d.export_image3d(
        brd, "api_3d_yrot1.png", pcb_rotate=(0, 45, 0), size=(200, 150)
    )
    image3d.export_image3d(
        brd, "api_3d_yrot2.png", pcb_rotate=(0, 90, 0), size=(200, 150)
    )
    image3d.export_image3d(
        brd, "api_3d_yrot3.png", pcb_rotate=(0, 135, 0), size=(200, 150)
    )

```

Start the example program:
<!-- embedme doc/gen/python3_-m_eagexp.examples.image3d_example.txt -->
```console
$ python3 -m eagexp.examples.image3d_example
Traceback (most recent call last):
  File "/usr/lib/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/home/vagrant/.tox/eagexp/py3-doc/lib/python3.6/site-packages/eagexp/examples/image3d_example.py", line 18, in <module>
    brd, "api_3d_xrot.png", pcb_rotate=(180, 0, 0), size=(200, 150)
  File "/home/vagrant/.tox/eagexp/py3-doc/lib/python3.6/site-packages/eagexp/image3d.py", line 84, in export_image3d
    callback=render,
  File "/home/vagrant/.tox/eagexp/py3-doc/lib/python3.6/site-packages/eagexp/cmd.py", line 108, in command_eagle
    callback(tmp_dir, tmp_input)
  File "/home/vagrant/.tox/eagexp/py3-doc/lib/python3.6/site-packages/eagexp/image3d.py", line 60, in render
    s = s.replace(templ % ("x", 0), templ % ("x", pcb_rotate[0]))
TypeError: a bytes-like object is required, not 'str'
```

Result:

..  #-- sh('python -m eagexp.examples.image3d_example')--#
..  #-#

![](/doc/gen/api_3d.png)
![](/doc/gen/api_3d_xrot.png)
![](/doc/gen/api_3d_yrot1.png)
![](/doc/gen/api_3d_yrot2.png)
![](/doc/gen/api_3d_yrot3.png)
![](/doc/gen/api_3d_size1.png)
![](/doc/gen/api_3d_size2.png)
![](/doc/gen/api_3d_size3.png)

Example for partlist export:

```py
# eagexp/examples/partlist_example.py

from eagexp import partlist

sch = "/usr/share/eagle/projects/examples/singlesided/singlesided.sch"
brd = "/usr/share/eagle/projects/examples/singlesided/singlesided.brd"

if __name__ == "__main__":
    print("raw_partlist of " + sch)
    print("'''")
    print(partlist.raw_partlist(sch))
    print("'''")

    print()

    print("raw_partlist of " + brd)
    print("'''")
    print(partlist.raw_partlist(brd))
    print("'''")

    print()

    print("structured_partlist of " + sch)
    print(partlist.structured_partlist(sch))

    print()

    print("structured_partlist of " + brd)
    print(partlist.structured_partlist(brd))

```

Start the example program:
<!-- embedme doc/gen/python3_-m_eagexp.examples.partlist_example.txt -->
```console
$ python3 -m eagexp.examples.partlist_example
raw_partlist of /usr/share/eagle/projects/examples/singlesided/singlesided.sch
'''
Partlist

Exported from singlesided.sch at 31 May 2020 20:55:38

EAGLE Version 6.6.0 Copyright (c) 1988-2014 CadSoft

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

'''

raw_partlist of /usr/share/eagle/projects/examples/singlesided/singlesided.brd
'''
Partlist

Exported from singlesided.brd at 31 May 2020 20:55:40

EAGLE Version 6.6.0 Copyright (c) 1988-2014 CadSoft

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

'''

structured_partlist of /usr/share/eagle/projects/examples/singlesided/singlesided.sch
([], [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}])

structured_partlist of /usr/share/eagle/projects/examples/singlesided/singlesided.brd
([], [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}])
```

Export schematic from command-line
----------------------------------

Export image
++++++++++++

Start the eagexp module directly with python:

<!-- embedme doc/gen/python3_-m_eagexp.image__usr_share_eagle_projects_examples_singlesided_singlesided.sch_cli_sch.png.txt -->
```console
$ python3 -m eagexp.image /usr/share/eagle/projects/examples/singlesided/singlesided.sch cli_sch.png

```
  
<!-- ![](/doc/gen/cli_sch.png) -->
<img src="doc/gen/cli_sch.png" width="200">


Export partlist
+++++++++++++++

Start the eagexp module directly with python:

<!-- embedme doc/gen/python3_-m_eagexp.partlist__usr_share_eagle_projects_examples_singlesided_singlesided.sch.txt -->
```console
$ python3 -m eagexp.partlist /usr/share/eagle/projects/examples/singlesided/singlesided.sch
Partlist

Exported from singlesided.sch at 31 May 2020 20:56:06

EAGLE Version 6.6.0 Copyright (c) 1988-2014 CadSoft

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

```

Export board from command-line
------------------------------

Export image
++++++++++++

Start the eagexp module directly with python:

<!-- embedme doc/gen/python3_-m_eagexp.image__usr_share_eagle_projects_examples_singlesided_singlesided.brd_cli_brd.png.txt -->
```console
$ python3 -m eagexp.image /usr/share/eagle/projects/examples/singlesided/singlesided.brd cli_brd.png

```

![](/doc/gen/cli_brd.png)

Export 3D image
+++++++++++++++

Start the eagexp module directly with python:

<!-- embedme doc/gen/python3_-m_eagexp.image3d__usr_share_eagle_projects_examples_singlesided_singlesided.brd_cli_3d.png.txt -->
```console
$ python3 -m eagexp.image3d /usr/share/eagle/projects/examples/singlesided/singlesided.brd cli_3d.png

```

![](/doc/gen/cli_3d.png)

Export partlist
+++++++++++++++

Start the eagexp module directly with python:

<!-- embedme doc/gen/python3_-m_eagexp.partlist__usr_share_eagle_projects_examples_singlesided_singlesided.brd.txt -->
```console
$ python3 -m eagexp.partlist /usr/share/eagle/projects/examples/singlesided/singlesided.brd
Partlist

Exported from singlesided.brd at 31 May 2020 20:56:14

EAGLE Version 6.6.0 Copyright (c) 1988-2014 CadSoft

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

```

airwires
--------

```py
# eagexp/examples/airwires.py

from eagexp.airwires import airwires

brd1 = "/usr/share/eagle/projects/examples/singlesided/singlesided.brd"
brd2 = "/usr/share/eagle/projects/examples/tutorial/demo2.brd"

if __name__ == "__main__":
    print(airwires(brd1))
    print(airwires(brd2))

```

<!-- embedme doc/gen/python3_-m_eagexp.examples.airwires.txt -->
```console
$ python3 -m eagexp.examples.airwires
39
0
```    
    
Command-line help
=================


<!-- embedme doc/gen/python3_-m_eagexp.image_--help.txt -->
```console
$ python3 -m eagexp.image --help
usage: image.py [-h] [-t TIMEOUT] [-p PALETTE] [-r RESOLUTION] [-l LAYERS]
                [-c COMMAND] [-m] [-s] [--debug] [--version]
                input output

Exporting eagle .sch or .brd file into image file. If export is blocked
somehow (e.g. popup window is displayed) then after timeout operation is
canceled with exception. Problem can be investigated by setting 'showgui'
flag.

Exporting generates an image file with a format corresponding to the given
filename extension. The following image formats are available:

.bmp    Windows Bitmap Files

.png    Portable Network Graphics Files

.pbm    Portable Bitmap Files

.pgm    Portable Grayscale Bitmap Files

.ppm    Portable Pixelmap Files

.tif    TIFF Files

.xbm    X Bitmap Files

.xpm    X Pixmap Files

positional arguments:
  input                 eagle .sch or .brd file name
  output                image file name, existing file will be removed first!

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        operation is canceled after this timeout (sec)
  -p PALETTE, --palette PALETTE
                        background color [None,black,white,colored]
  -r RESOLUTION, --resolution RESOLUTION
                        image resolution in dpi (50..2400)
  -l LAYERS, --layers LAYERS
                        list, layers to be displayed ['top','pads']
  -c COMMAND, --command COMMAND
                        string, direct eagle command
  -m, --mirror          Bool
  -s, --showgui         eagle GUI is displayed
  --debug               set logging level to DEBUG
  --version             show program's version number and exit
```

<!-- embedme doc/gen/python3_-m_eagexp.image3d_--help.txt -->
```console
$ python3 -m eagexp.image3d --help
usage: image3d.py [-h] [-s SIZE] [-p PCB_ROTATE] [-t TIMEOUT] [--showgui]
                  [--debug] [--version]
                  input output

Exporting eagle .brd file into 3D image file using Eagle3D and povray. If
export is blocked somehow (e.g. popup window is displayed) then after timeout
operation is canceled with exception. Problem can be investigated by setting
'showgui' flag.

positional arguments:
  input                 eagle .brd file name
  output                image file name (.png)

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  tuple(width, size), image size
  -p PCB_ROTATE, --pcb-rotate PCB_ROTATE
  -t TIMEOUT, --timeout TIMEOUT
                        operation is canceled after this timeout (sec)
  --showgui             eagle GUI is displayed
  --debug               set logging level to DEBUG
  --version             show program's version number and exit
```

<!-- embedme doc/gen/python3_-m_eagexp.partlist_--help.txt -->
```console
$ python3 -m eagexp.partlist --help
usage: partlist.py [-h] [-t TIMEOUT] [-s] [--debug] [--version] input

print partlist text delivered by eagle

positional arguments:
  input                 .sch or .brd file name

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        int
  -s, --showgui         Bool, True -> do not hide eagle GUI
  --debug               set logging level to DEBUG
  --version             show program's version number and exit
```




.. _pip: https://pypi.python.org/pypi/pip
.. _Xvfb: http://en.wikipedia.org/wiki/Xvfb
.. _pyvirtualdisplay: https://github.com/ponty/PyVirtualDisplay
.. _eagle: http://www.cadsoftusa.com/
.. _povray: http://www.povray.org/
.. _PIL: http://www.pythonware.com/library/pil/


.. |Travis| image: https://travis-ci.org/ponty/eagexp.svg?branch=master
   :target: https://travis-ci.org/ponty/eagexp/
.. |License| image: https://img.shields.io/pypi/l/eagexp.svg
   :target: https://pypi.python.org/pypi/eagexp/
   

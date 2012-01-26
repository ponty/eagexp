eagexp can export eagle_ partlist or image (2D/3D) of schematic or board.

Links:
 * home: https://github.com/ponty/eagexp
 * documentation: http://ponty.github.com/eagexp


Features:
 - written in python
 - it can be used as library or as a command line program
 - background processing (only if Xephyr_, Xvfb_ and pyvirtualdisplay_ are installed)
 - timeout
 - 3D image export using Eagle3D_ and povray_
 - calculate airwires
 
Known problems:
 - slow: eagle is opened and closed for each export
 - high DPI does not work (memory problem?)
 - Python 3 is not supported
 - export can be blocked by eagle_ -> timeout
 - 3D image export has a lot of options which are not supported
   
Basic usage
============

    >>> from eagexp import image, partlist
    >>> brd='~/.eagle/projects/examples/singlesided/singlesided.brd'
    >>> image.export_image(brd, 'brd.png', resolution=600)
    >>> print partlist.raw_partlist(brd)


How it works
========================

#. start Xvfb_ headless X server using pyvirtualdisplay_
#. redirect eagle display to Xvfb server by setting $DISPLAY variable.
#. start eagle_ with EXPORT and QUIT commands


Installation
============

General
--------

 * install eagle_
 * install povray_ (optional for 3D)
 * install pip_
 * install pyvirtualdisplay_ , xvfb_ , xephyr_ (optional for background processing)
 * install the program::

    # as root
    pip install eagexp


Ubuntu
----------
::

    sudo apt-get install eagle
    sudo apt-get install povray
    sudo apt-get install python-pip

    # optional for background processing
    sudo apt-get install xvfb xserver-xephyr

    sudo pip install eagexp
    
Uninstall
----------
::

    # as root
    pip uninstall eagexp


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _Xvfb: http://en.wikipedia.org/wiki/Xvfb
.. _Xephyr: http://en.wikipedia.org/wiki/Xephyr
.. _pyvirtualdisplay: https://github.com/ponty/PyVirtualDisplay
.. _eagle: http://www.cadsoftusa.com/
.. _povray: http://www.povray.org/
.. _povray: http://www.povray.org/
.. _Eagle3D: http://www.matwei.de/doku.php?id=en:eagle3d:eagle3d

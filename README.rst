eagexp can export eagle_ partlist or image of schematic or board.

Links:
 * home: https://github.com/ponty/eagexp
 * html documentation: http://ponty.github.com/eagexp
 * pdf documentation: https://github.com/ponty/eagexp/raw/master/docs/_build/latex/eagexp.pdf


Features:
 - background processing (only if Xephyr_, Xvfb_ and PyVirtualDisplay_ are installed)
 - timeout
 
Known problems:
 - slow: eagle is opened and closed for each export
 - high DPI does not work (memory problem?)
 - Python 3 is not supported
 - export can be blocked by eagle_ -> timeout
  
Basic usage
============

    >>> from eagexp import image, partlist
    >>> brd='~/.eagle/projects/examples/singlesided/singlesided.brd'
    >>> image.export_image(brd, 'brd.png', resolution=600)
    >>> print partlist.raw_partlist(brd)


How it works
========================

#. start Xvfb_ headless X server using PyVirtualDisplay_
#. redirect eagle display to Xvfb server by setting $DISPLAY variable.
#. start eagle_ with EXPORT and QUIT commands


Installation
============

General
--------

 * install eagle_
 * install setuptools_
 * install PyVirtualDisplay_ , xvfb_ , xephyr_ (optional for background processing)
 * install the program::

    # as root
    easy_install https://github.com/ponty/eagexp/zipball/master


Ubuntu
----------
::

    sudo apt-get install eagle
    sudo apt-get install python-setuptools

    # optional for background processing
    sudo apt-get install xvfb xserver-xephyr

    sudo easy_install https://github.com/ponty/eagexp/zipball/master
    
Uninstall
----------
::

    # as root
    pip uninstall eagexp


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _Xvfb: http://en.wikipedia.org/wiki/Xvfb
.. _Xephyr: http://en.wikipedia.org/wiki/Xephyr
.. _PyVirtualDisplay: https://github.com/ponty/PyVirtualDisplay
.. _eagle: http://www.cadsoftusa.com/

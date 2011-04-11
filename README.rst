eag2img can convert eagle_ schematic and board to image.

 * home: https://github.com/ponty/eag2img
 * html documentation: http://ponty.github.com/eag2img
 * pdf documentation: https://github.com/ponty/eag2img/raw/master/docs/_build/latex/eag2img.pdf


Features:
 - background processing (only if Xephyr_, Xvfb_ and PyVirtualDisplay_ are installed)
 - crossplatform, development on linux
 
Known problems:
 - slow: eagle is opened and closed
  
Basic usage
============

    >>> from eag2img import export_eagle_image
    >>> in1='~/.eagle/projects/examples/singlesided/singlesided.sch'
    >>> out1='~/singlesided.png'
    >>> export_eagle_image(in1,out1)


Installation
============

General
--------

 * install setuptools_
 * install PyVirtualDisplay_ (optional for background processing)
 * install the program::

    # as root
    easy_install https://github.com/ponty/eag2img/zipball/master


Ubuntu
----------
::

    # optional for background processing
    sudo apt-get install xvfb xserver-xephyr
    sudo easy_install PyVirtualDisplay

    sudo apt-get install python-setuptools
    sudo easy_install https://github.com/ponty/eag2img/zipball/master
    
Uninstall
----------
::

    # as root
    pip uninstall eag2img


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _Xvfb: http://en.wikipedia.org/wiki/Xvfb
.. _Xephyr: http://en.wikipedia.org/wiki/Xephyr
.. _PyVirtualDisplay: https://github.com/ponty/PyVirtualDisplay
.. _eagle: http://www.cadsoftusa.com/

Usage
==================

..  [[[cog
..  import os
..  os.chdir('docs')
..  ]]]
..  [[[end]]]

..  [[[cog
..  import cog
..  import os
..  def call(f):
..   from easyprocess import Proc
..   Proc(f).call()
..   cog.outl()
..   cog.outl('::')
..   cog.outl()
..   cog.outl('    ' + f)
..   cog.outl()
..  ]]]
..  [[[end]]]


Export from python code
-------------------------------------------

Example:

.. literalinclude:: ../eagexp/examples/image_example.py

Start the example program:

..  [[[cog
..  f = 'python -m eagexp.examples.image_example'
..  call(f)
..  ]]]

::

    python -m eagexp.examples.image_example

..  [[[end]]]

Result:

.. image::  api_brd_50.png

.. image::  api_brd_100.png

.. image::  api_brd_150.png

.. image::  api_brd_mirror.png

.. image::  api_brd_layer.png

.. image::  api_brd_command.png

Example for 3D:

.. literalinclude:: ../eagexp/examples/image3d_example.py

Start the example program:

..  [[[cog
..  f = 'python -m eagexp.examples.image3d_example'
..  call(f)
..  ]]]

::

    python -m eagexp.examples.image3d_example

..  [[[end]]]

Result:

.. image::  api_3d.png
.. image::  api_3d_xrot.png
.. image::  api_3d_yrot1.png
.. image::  api_3d_yrot2.png
.. image::  api_3d_yrot3.png
.. image::  api_3d_size1.png
.. image::  api_3d_size2.png
.. image::  api_3d_size3.png

Example for partlist export:

.. literalinclude:: ../eagexp/examples/partlist_example.py

Start the example program:

.. program-output:: python -m eagexp.examples.partlist_example
    :prompt:

Export schematic from command-line
----------------------------------------------

Export image
+++++++++++++

Start the eagexp module directly with python:

..  [[[cog
..  f = 'cli_sch.png'
..  f = 'python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.sch ' + f
..  call(f)
..  ]]]

::

    python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.sch cli_sch.png

..  [[[end]]]

Result:

.. image::  cli_sch.png
    :scale: 20%

Export partlist
++++++++++++++++

Start the eagexp module directly with python:

.. program-output:: python -m eagexp.partlist ~/.eagle/projects/examples/singlesided/singlesided.sch
    :prompt:

Export board from command-line
-------------------------------------------

Export image
+++++++++++++

Start the eagexp module directly with python:

..  [[[cog
..  f = 'cli_brd.png'
..  f = 'python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.brd ' + f
..  call(f)
..  ]]]

::

    python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.brd cli_brd.png

..  [[[end]]]

Result:

.. image::  cli_brd.png

Export 3D image
++++++++++++++++

Start the eagexp module directly with python:

..  [[[cog
..  f = 'python -m eagexp.image3d ~/.eagle/projects/examples/singlesided/singlesided.brd cli_3d.png'
..  call(f)
..  ]]]

::

    python -m eagexp.image3d ~/.eagle/projects/examples/singlesided/singlesided.brd cli_3d.png

..  [[[end]]]

Result:

.. image::  cli_3d.png

Export partlist
++++++++++++++++

Start the eagexp module directly with python:

.. program-output:: python -m eagexp.partlist ~/.eagle/projects/examples/singlesided/singlesided.brd
    :prompt:


..  [[[cog
..  import os
..  os.chdir('..')
..  ]]]
..  [[[end]]]



airwires
----------

.. runblock:: pycon
    
    >>> from eagexp.airwires import airwires
    >>> print airwires('~/.eagle/projects/examples/singlesided/singlesided.brd')    
    >>> print airwires('~/.eagle/projects/examples/tutorial/demo2.brd')
    
    
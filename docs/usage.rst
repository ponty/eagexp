Usage
==================

..  [[[cog
..  def call(f):
..   import cog
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
..  f = 'python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.sch docs/' + f
..  call(f)
..  ]]]

::

    python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.sch docs/cli_sch.png

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
..  f = 'python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.brd docs/' + f
..  call(f)
..  ]]]

::

    python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.brd docs/cli_brd.png

..  [[[end]]]

Result:

.. image::  cli_brd.png

Export partlist
++++++++++++++++

Start the eagexp module directly with python:

.. program-output:: python -m eagexp.partlist ~/.eagle/projects/examples/singlesided/singlesided.brd
    :prompt:



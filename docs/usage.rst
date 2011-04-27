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

Example for image export with 3 different DPI setting:

.. literalinclude:: ../eagexp/examples/image_example.py

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


Example for partlist export:

.. literalinclude:: ../eagexp/examples/partlist_example.py

Output:

.. program-output:: python -m eagexp.examples.partlist_example
    :prompt:

Export schematic from command-line
----------------------------------------------

Image:

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

Partlist:

.. program-output:: python -m eagexp.partlist ~/.eagle/projects/examples/singlesided/singlesided.sch
    :prompt:

Export board from command-line
-------------------------------------------


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

Partlist:

.. program-output:: python -m eagexp.partlist ~/.eagle/projects/examples/singlesided/singlesided.brd
    :prompt:



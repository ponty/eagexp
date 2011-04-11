# -*- coding: utf-8 -*-

from path import path
import logging
import sphinx
import sys

project='eag2img'
author='ponty'
copyright = '2011, ponty'
PACKAGE = 'eag2img'

__version__ = None
py = path('..') / PACKAGE / '__init__.py'
for line in open(py).readlines():
    if '__version__' in line:
        exec line
        break
assert __version__    
release = __version__

#logging.basicConfig(level=logging.DEBUG)

# Extension
extensions = [
     # -*-Extensions: -*-
     #'sphinx.ext.autodoc',
     #'sphinxcontrib.programoutput',
     #'sphinxcontrib.programscreenshot',
     #'sphinx.ext.graphviz',
     #'sphinxcontrib.autorun',
     #'sphinx.ext.autosummary',
     #'sphinx.ext.intersphinx',
    ]
intersphinx_mapping = {'http://docs.python.org/': None}

# Source
master_doc = 'index'
templates_path = ['_templates']
source_suffix = '.rst'
exclude_trees = []
pygments_style = 'sphinx'

# html build settings
html_theme = 'default'
html_static_path = ['_static']

# htmlhelp settings
htmlhelp_basename = '%sdoc' % project

# latex build settings
latex_documents = [
    ('index', '%s.tex' % project, u'%s Documentation' % project,
    author, 'manual'),
]

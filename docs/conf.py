# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'Python Handbook'
copyright = '2025, Your Name'
author = 'Your Name'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# MyST options
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'sphinxsetup': 'hmargin=2.5cm, vmargin=3cm, marginpar=2cm',
}
latex_documents = [
    ('index', 'python_handbook.tex', 'Python Handbook', 'Your Name', 'manual'),
]
latex_show_urls = 'footnote'

# -- Doctest ---------------------------------------------------------------
doctest_global_setup = '''
import sys, os, json, pathlib, typing, collections, itertools, math, random
'''
doctest_test_doctest_blocks = True
# -*- coding: utf-8 -*-
#
# OpenMAF documentation build configuration file, created by
# sphinx-quickstart on Wed Mar 24 12:19:03 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, re

# Check Sphinx version
import sphinx
if sphinx.__version__ < "0.5":
    raise RuntimeError("Sphinx 0.5.dev or newer required")

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('sphinxext'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [  # 'rst2pdf.pdfbuilder',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              #'sphinx.ext.pngmath',
              'sphinx.ext.mathjax',
              'sphinx.ext.autodoc',
              'numpydoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode'
              ]

if sphinx.__version__ >= "0.7":
    extensions.append('sphinx.ext.autosummary')
else:
    extensions.append('autosummary')
    extensions.append('only_directives')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'OpenMAF'
copyright = u'2014, OpenMAF'
publisher = u'OpenMAF'
author = u''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None
default_role = "autolink"

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# include the TODO in the output
todo_include_todos = True


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'default'
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes/sphinx_rtd_theme", ]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = re.sub('\\\\&', '&', project) + "v" + version + " documentation" 

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = '_static/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
# htmlhelp_basename = ''
htmlhelp_basename = re.sub(' ', '', project.lower())

# Pngmath should try to align formulas properly
pngmath_use_preview = True

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
#  ('index', re.sub(' ', '', project.lower()) + '.tex', project,
   ('index', re.sub(' ', '_', project)+ ".tex", project,
	   author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None
latex_logo = '_static/logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = True

# Additional stuff for the LaTeX preamble.
latex_preamble = r'''
\usepackage{amsmath}
\DeclareUnicodeCharacter{00A0}{\nobreakspace}

% In the parameters section, place a newline after the Parameters
% header
\usepackage{expdlist}
\let\latexdescription=\description
\def\description{\latexdescription{}{} \breaklabel}

% Make Examples/etc section headers smaller and more compact
\makeatletter
\titleformat{\paragraph}{\normalsize\py@HeaderFamily}%
            {\py@TitleColor}{0em}{\py@TitleColor}{\py@NormalColor}
\titlespacing*{\paragraph}{0pt}{1ex}{0pt}
\makeatother

% Fix footer/header
\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{\thechapter.\ #1}}{}}
\renewcommand{\sectionmark}[1]{\markright{\MakeUppercase{\thesection.\ #1}}}
'''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
latex_use_modindex = True

# If false, no module index is generated.
latex_domain_indices = True


#-----------------------------------------------------------------------------
# Intersphinx configuration
#-----------------------------------------------------------------------------
# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

# -----------------------------------------------------------------------------
# Numpy extensions
# -----------------------------------------------------------------------------

# If we want to do a phantom import from an XML file for all autodocs
phantom_import_file = 'dump.xml'

# Make numpydoc to generate plots for example sections
numpydoc_use_plots = True

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

# if sphinx.__version__ >= "0.7":
#    import glob
#    autosummary_generate = glob.glob("reference/*.rst")

autoclass_content = 'both'

# -----------------------------------------------------------------------------
# Plots
# -----------------------------------------------------------------------------
#plot_pre_code = """
#import numpy as np
#np.random.seed(0)
#"""
#plot_include_source = True
#plot_formats = [('png', 100), 'pdf']
#
#import math
#phi = (math.sqrt(5) + 1) / 2
#
#import matplotlib
#matplotlib.rcParams.update({
#    'font.size': 8,
#    'axes.titlesize': 8,
#    'axes.labelsize': 8,
#    'xtick.labelsize': 8,
#    'ytick.labelsize': 8,
#    'legend.fontsize': 8,
#    'figure.figsize': (3 * phi, 3),
#    'figure.subplot.bottom': 0.2,
#    'figure.subplot.left': 0.2,
#    'figure.subplot.right': 0.9,
#    'figure.subplot.top': 0.85,
#    'figure.subplot.wspace': 0.4,
#    'text.usetex': False,
#})

# -- Options for PDF output --------------------------------------------------
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.
pdf_documents = [
    ('index', re.sub(' ', '', project.lower()), project , author),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx', 'kerning', 'a4']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
# pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
# Language to be used for hyphenation support
# pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
# pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
pdf_break_level = 1

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
# pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
# pdf_verbosity = 0

# If false, no index is generated.
pdf_use_index = True

# If false, no modindex is generated.
pdf_use_modindex = True

# If false, no coverpage is generated.
pdf_use_coverpage = True

# Documents to append as an appendix to all manuals.
# pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = False

# Set the default DPI for images
# pdf_default_dpi = 72

# Enable rst2pdf extension modules (default is empty list)
# you need vectorpdf for better sphinx's graphviz support
# pdf_extensions = ['vectorpdf']

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = publisher
epub_copyright = copyright

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

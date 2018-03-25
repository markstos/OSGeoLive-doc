# -*- coding: utf-8 -*-
#
# OSGeoLive documentation build configuration file, created by
# sphinx-quickstart on Wed Sep 22 19:00:58 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# Definitions of:
# iso_size = 4.0
# iso_mini_size = 4.0
# vm_7z_size = 3.4
# req_hd_size = 20


# for osgeolive-X.X.iso
iso_size = 3.7
# for osgeolive-mini-X.X.iso
iso_mini_size = 3.7
# for osgeo-vm-X.X.7z
vm_7z_size = 3.2
# required hard disk space
req_hd_size = 20

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

#fileIN = open("VERSION.txt", "r")
#extract = fileIN.readline()
#line = extract.split()
#version =  line[0] + " " + line[1]
#fileIN.close()

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'@OSGeoLiveDoc_NAME@'
copyright = u'2011, OSGeo'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = '4.5'
# The full version, including alpha/beta/rc tags.
version = '@OSGeoLiveDoc_VERSION@'
release = '@OSGeoLiveDoc_VERSION@'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build', 'doc/presentation']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'overview'
html_theme_path = ['_themes']

if os.environ.get('HTML_THEME_PATH'):
  html_theme_path.append(os.environ.get('HTML_THEME_PATH'))

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title ='|project| |release| documentation'
html_title='%(projectname)s %(projectversion)s Documentation' % { 'projectname':project,'projectversion': release }

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_static_path = ['@CMAKE_CURRENT_SOURCE_DIR@/_static']
html_favicon = '@CMAKE_CURRENT_SOURCE_DIR@/_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % project


# -- Options for locale output --------------------------------------------------
locale_dirs = ['../../locale/']   # path is example but recommended.
gettext_compact = False     # optional.
gettext_auto_build = True

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# remove blank pages
'classoptions': ',oneside',
'babel': '\\usepackage[english]{babel}'

# Additional stuff for the LaTeX preamble.
#'preamble': ''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'OSGeoLive.tex', u'OSGeoLive Documentation',
   u'OSGeo', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# Linkcheck configuration, see http://sphinx.pocoo.org/latest/config.html#options-for-the-linkcheck-builder

linkcheck_ignore = [ r'http://localhost:\d+/', r'http://localhost/', r'http://127.0.0.1:\d+/', r'http://download.osgeo.org/']
linkcheck_anchors = False

# If false, no module index is generated.
#latex_use_modindex = True

# TODO (fgdrf) read the values from flat text file
# global replacements that will be included at the end of every source file
# see http://sphinx.readthedocs.org/en/latest/config.html#confval-rst_epilog
#
# TODO export versions into an extra app-versions file
#
rst_epilog="""
.. |osgeolive-project| replace:: %(projectname)s
.. |osgeolive-version| replace:: %(projectname)s %(projectversion)s
.. |osgeolive-hdspace| replace:: %(required_hd_space)02d GB
.. |osgeolive-iso-size| replace:: %(iso_size).1f GB
.. |osgeolive-iso-mini-size| replace:: %(iso_mini_size).1f GB
.. |osgeolive-vm-7z-size| replace:: %(vm_7z_size).1f GB
.. |osgeolive-appmenupath-geoserver| replace:: :menuselection:`Geospatial --> Web Services --> GeoServer --> Start GeoServer`
.. |osgeolive-appmenupath-udig| replace:: :menuselection:`Geospatial --> Desktop GIS --> uDig`
.. |osgeolive-appmenupath-52nWPS| replace:: :menuselection:`Geospatial --> Web Services --> 52North --> Start 52North WPS`
.. |nologo| image:: /images/logos/nologo.png
                        :align: bottom
                        :height: 18
.. |osgeo_project| image:: /images/logos/OSGeo_compass.png
                        :alt: OSGeo Project
                        :align: bottom
                        :height: 18
                        :target: ../sponsors_osgeo.html
.. |osgeo_incubation| image:: /images/logos/OSGeo_compass.png
                        :alt: OSGeo Community
                        :align: middle
                        :height: 18
                        :target: ../sponsors_osgeo.html
.. |osgeo_community| image:: /images/logos/OSGeo_compass.png
                        :alt: OSGeo Community
                        :align: middle
                        :height: 18
                        :target: ../sponsors_osgeo.html

@OSGeoLiveDoc_PROJECTS_LOGOS@
@OSGeoLiveDoc_PROJECTS_VERSIONS@""" % {
  'projectname':project,
  'projectversion': version,
  'required_hd_space': req_hd_size,
  'iso_size': iso_size,
  'iso_mini_size': iso_mini_size,
  'vm_7z_size': vm_7z_size
}

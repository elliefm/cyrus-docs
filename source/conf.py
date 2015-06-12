# -*- coding: utf-8 -*-
#
# Cyrus IMAP documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  6 19:23:19 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('exts'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.coverage',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
]

extensions.append('sphinxlocal.builders.manpage')

mathjax_path = 'https://cdn.mathjax.org/mathjax/latest/MathJax.js'

todo_include_todos = True

locale_dirs = [ 'locale/' ]
gettext_compact = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Cyrus IMAP and SASL'
copyright = u'1993-2015, The Cyrus Team'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}


# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["themes"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = "themes/images/logo.gif"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Cyrusdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'Cyrus.tex', u'Cyrus Documentation',
   u'The Cyrus Team', 'manual'),
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

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
        (
            'imap/admin/commands/arbitron',
            'arbitron',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/chk_cyrus',
            'chk_cyrus',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/ctl_cyrusdb',
            'ctl_cyrusdb',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/ctl_deliver',
            'ctl_deliver',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/ctl_mboxlist',
            'ctl_mboxlist',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/ctl_zoneinfo',
            'ctl_zoneinfo',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cvt_cyrusdb',
            'cvt_cyrusdb',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyr_dbtool',
            'cyr_dbtool',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyr_df',
            'cyr_df',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyr_expire',
            'cyr_expire',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyr_info',
            'cyr_info',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyradm',
            'cyradm',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/ipurge',
            'ipurge',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/mbexamine',
            'mbexamine',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/mbpath',
            'mbpath',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/mbtool',
            'mbtool',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/mkimap',
            'mkimap',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/ptdump',
            'ptdump',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/ptexpire',
            'ptexpire',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/ptloader',
            'ptloader',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/quota',
            'quota',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/reconstruct',
            'reconstruct',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/tls_prune',
            'tls_prune',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)'
                ],
            8
    ),

        (
            'imap/admin/commands/unexpunge',
            'unexpunge',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/squatter',
            'squatter',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/ctl_conversationsdb',
            'ctl_conversationsdb',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/sync_client',
            'sync_client',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyr_synclog',
            'cyr_synclog',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/deliver',
            'deliver',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyr_deny',
            'cyr_deny',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyrus-master',
            'cyrus-master',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/mbexamine',
            'mbexamine',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/mbpath',
            'mbpath',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/mbtool',
            'mbtool',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/mkimap',
            'mkimap',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/quota',
            'quota',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Jeroen van Meeuwen (Kolab Systems)',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/reconstruct',
            'reconstruct',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/cyrfetchnews',
            'cyrfetchnews',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/fud',
            'fud',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),

        (
            'imap/admin/commands/httpd',
            'httpd',
            u'Cyrus IMAP Documentation',
            [
                    u'The Cyrus Team',
                    u'Nic Bernstein (Onlight)'
                ],
            8
    ),
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Cyrus', u'Cyrus Documentation',
   u'The Cyrus Team', 'Cyrus', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Cyrus'
epub_author = u'The Cyrus Team'
epub_publisher = u'The Cyrus Team'
epub_copyright = u'2014, The Cyrus Team'

# The basename for the epub file. It defaults to the project name.
epub_basename = u'Cyrus'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True

rst_prolog = """
.. |imap_last_stable_version| replace:: 2.4.17
.. |imap_last_stable_branch| replace:: `cyrus-imapd-2.4`
.. |imap_last_stable_next_version| replace:: 2.4.17 + patches
.. |imap_current_stable_version| replace:: 2.5.3
.. |imap_current_stable_next_version| replace:: 2.5.3 + patches
.. |imap_current_stable_branch| replace:: `cyrus-imapd-2.5`
.. |imap_latest_development_version| replace:: 3.0
.. |imap_latest_development_branch| replace:: master
.. |imap_tikanga_stock_version| replace:: 2.3.7
.. |imap_santiago_stock_version| replace:: 2.3.16
.. |imap_maipo_stock_version| replace:: 2.4.17
.. |imap_precise_stock_version| replace:: 2.4.12-2
.. |imap_trusty_stock_version| replace:: 2.4.17+caldav~beta9-3
.. |imap_utopic_stock_version| replace:: 2.4.17+caldav~beta10-5
.. |imap_vivid_stock_version| replace:: 2.4.17+caldav~beta10-17
.. |imap_wily_stock_version| replace:: 2.4.17+caldav~beta10-17
"""

rst_prolog += """
.. |git_cyrus_imapd_url| replace:: https://git.cyrus.foundation/diffusion/I/cyrus-imapd.git
"""

# The version in which compatibility support for RFC 2086 (the 'c' and
# 'd' rights) is dropped.
rst_prolog += """
.. |imap_version_rfc2086_dropped| replace:: 3.0
"""

# The version in which the altnamespace setting default changes (was
# off).
rst_prolog += """
.. |imap_version_altnamespace_default_on| replace:: 3.0
"""

# The version in which the unixhierarchysep setting default changes (was
# off).
rst_prolog += """
.. |imap_version_unixhierarchysep_default_on| replace:: 3.0
"""

# The version in which the master process was renamed to cyrus-master.
rst_prolog += """
.. |imap_version_master_renamed| replace:: 3.0
"""

# Bloilerplate configuration file texts.
rst_prolog += """
.. |default-conf-text| replace:: reads its configuration options out of the :manpage:`imapd.conf(5)` file unless specified otherwise by **-C**.
.. |cli-dash-c-text| replace:: Use the specified configuration file *config-file* rather than the default :manpage:`imapd.conf(5)`.
.. |def-confdir-text| replace:: The *configdirectory* option in :manpage:`imapd.conf(5)` is used to determine the default location of the
"""

# New feature version disclaimer for 3.0 (big changes)
rst_prolog += """
.. |v3-new-feature| replace:: This feature was introduced in version 3.0.
.. |v3-new-command| replace:: This command was introduced in version 3.0.
"""

rst_prolog += """
.. |AMS| replace:: :abbr:`AMS (Andrew Mail System)`
.. |CMU| replace:: :abbr:`CMU (Carnegie Mellon University)`
"""

# Uncomment this if you publish to, like, www.cyrusimap.org/~vanmeeuwen/
#rst_prolog += """
#.. WARNING::

    #You are looking at documentation that is maintained by interval.

    #Please see https://docs.cyrus.foundation/ for better maintained
    #documentation.
#"""

# Use this as :task:`18`
extlinks = {
        'rfc':('http://tools.ietf.org/html/rfc%s', 'RFC '),
        'task':('https://git.cyrus.foundation/T%s', 'Task #'),
    }

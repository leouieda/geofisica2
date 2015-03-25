# -*- coding: utf-8 -*-
import sys
import os
import datetime
import sphinx_bootstrap_theme

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.extlinks',
]

# Make sure versioneer is imported from here
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import versioneer

versioneer.VCS = 'git'
versioneer.tag_prefix = ''
versioneer.versionfile_source = 'version.py' # This line is useless
versioneer.parentdir_prefix = 'geofisica2-'
versions = versioneer.get_versions()
commit = versions['full']
version = versions['version']
if version == 'master':
    # When downloading a zip from Github, versioneer gets the version from the
    # directory name in the zip file. That would endup being 'master'. More
    # useful would be the commit hash. The pattern below will be replaced by
    # git when 'git archive' is called
    version = '$Format:%H$'

# General information about the project
year = datetime.date.today().year
project = u'Geofisica 2'
copyright = u'{:d}, Leonardo Uieda'.format(year)
version = year
# I'll use the release to place the commit hash at the footer of the site
release = commit.split('-')[0] # Get rid of -dirty

# Sphinx project configuration
templates_path = ['_templates']
exclude_patterns = ['_build']
source_suffix = '.rst'
#source_encoding = 'utf-8-sig'
master_doc = 'index'

# These enable substitutions using |variable| in the rst files
rst_epilog = """
.. |year| replace:: {year}
""".format(year=year)

html_last_updated_fmt = '%b %d, %Y'
html_title = u'Geofísica 2 - FGEL/UERJ'
html_short_title = u'Geofísica 2'
html_logo = ''
html_favicon = u'favicon.png'
html_static_path = ['_static']
html_extra_path = ['.nojekyll']
html_use_smartypants = True
pygments_style = 'sphinx'
#add_function_parentheses = False
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
html_show_sourcelink = True
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''
# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None
# Output file base name for HTML help builder.
htmlhelp_basename = 'geofisica2'

# Theme config
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    'bootswatch_theme': "flatly",
    'navbar_title': u'geofísica 2',
    'navbar_site_name': u"Práticas",
    'navbar_links': [
        ('Ementa', "ementa"),
        ('<i class="fa fa-envelope fa-fw" title="Lista de e-mails"></i>',
            "https://groups.google.com/d/forum/geofisica-uerj", True),
    ],
    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,
    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,
    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "This page",
    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,
    # Include hidden TOCs in Site navbar?
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "false",
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-default",
    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "false",
    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",
    'bootstrap_version': "3",
}

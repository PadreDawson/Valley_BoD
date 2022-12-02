# import sphinx_rtd_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Valley Lutheran BoD'
copyright = '2022'
# author = 'Board of Directors'
# release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'sphinx_rtd_theme',
    'rst2pdf.pdfbuilder',
]

pdf_documents = [
    ('index', u'rst2pdf', u'Sample rst2pdf doc', u'Your Name'),
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinx_material'
# html_static_path = ['_static']
# html_css_files = [
#     'custom.css',
# ]




# html_theme = 'sphinx_material'

# # Material theme options (see theme.conf for more information)
# html_theme_options = {

#     # Set the name of the project to appear in the navigation.
#     'nav_title': 'Documentation',

#     # Set you GA account ID to enable tracking
#     # 'google_analytics_account': 'UA-XXXXX',

#     # Specify a base_url used to generate sitemap.xml. If not
#     # specified, then no sitemap will be built.
#     'base_url': 'https://project.github.io/project',

#     # Set the color and the accent color
#     'color_primary': 'blue',
#     'color_accent': 'light-blue',

#     # Set the repo location to get a badge with stats
#     'repo_url': 'https://github.com/project/project/',
#     'repo_name': 'Project',

#     # Visible levels of the global TOC; -1 means unlimited
#     'globaltoc_depth': 2,
#     # If False, expand all TOC entries
#     'globaltoc_collapse': True,
#     # If True, show hidden TOC entries
#     'globaltoc_includehidden': False,
# }

# html_sidebars = {
#     "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
# }




html_theme = "pydata_sphinx_theme"

html_theme_options = {
"navbar_start": ["navbar-logo"],
"navbar_center": ["navbar-nav"],
"navbar_end": ["navbar-icon-links", "theme-switcher"],
"navbar_persistent": ["search-button"],
"show_toc_level": 2,
"announcement": "<p>Here's a <a href='https://pydata.org'>PyData Announcement!</a></p>",
"external_links": [
    {
        "url": "https://www.vlscrusaders.org/",
        "name": "Valley Lutheran School",
    },
],
"primary_sidebar_end": ["indices.html"],
}

# html_sidebars = {
#     "**": ["index.html"],
# }

html_context = {
   "default_mode": "light"
}
#:==========================================
# Sphinx Documentation Builder Configuration
#:==========================================

from datetime import datetime


#####################
# Project Information

project = 'bedrockpy'
copyright = f'{datetime.now().year}, Jonas da Silva'
author = 'Jonas da Silva'
release = '1.0.0a0.post1'


###############
# Configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',

    'myst_parser',
    'notfound.extension',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.video'
]


#######################
# autodoc Configuration

autodoc_default_options = {
    'members': True,
    'inherited-members': True,
    'undoc-members': True,
    'special-members': '__call__',
}
autodoc_typehints = 'both'
autoclass_content = 'both'


####################
# todo Configuration

todo_include_todos = True


####################
# MyST Configuration

myst_enable_extensions = [
    'linkify',
    'smartquotes',
    'substitution'
]

myst_linkify_fuzzy_links = False
myst_substitutions = {
    'release': release,
    'wip': '```{todo}\n\N{BUILDING CONSTRUCTION} Work In Progress\n```',
    'needs_research': '```{admonition} Research Required\n:class: warning\n\nThe section below requires research to be confirmed.\n```'
}
myst_fence_as_directive = ['mermaid']


###########################
# Intersphinx Configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}


############
# Find Files

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


###########################
# HTML Output Configuration

html_theme = 'furo'
html_title = 'bedrockpy'
html_static_path = ['_static']
html_css_files = ['style.css', 'mc.css']
html_favicon = '_static/bedrockpy_3d.ico'
html_logo = '../bedrockpy_3d.png'

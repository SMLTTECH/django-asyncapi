# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os, sys

html_logo = "assets/img/dj-asyncapi.png"
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'django-asyncapi'
copyright = '2024, s'
author = 's'

# -- General configuratƒion ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',  # to parse .md files
    'sphinx.ext.autodoc',  # to generate doc from docstrings
    "sphinx.ext.napoleon" , # to use google style docstrings
    "sphinxcontrib.autodoc_pydantic", # pydantic documentaion
    "sphinx_inline_tabs", # tabs
    "sphinx_copybutton", # copy button for code snippets
    # "attr_utils.autoattrs",
    # "sphinx_multiversion", # versioning
]

napoleon_google_docstring = True

templates_path = ['_templates']
exclude_patterns = []

sys.path.insert(0, "django_asyncapi")
sys.path.append(os.path.abspath('../'))

autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_show_json = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
        "sidebar/versions.html",
    ]
}
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Traceability'
copyright = '2020, Anas Nashif'
author = 'Anas Nashif'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'mlx.traceability',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
import os
import mlx.traceability

html_static_path = [
    os.path.join(os.path.dirname(mlx.traceability.__file__), 'assets'),
    '_static'
    ]

traceability_attributes = {
    'value': '^.*$',
    'asil': '^(QM|[ABCD])$',
}

traceability_relationship_to_string = {
    'value': 'Value',
    'asil': 'ASIL',
}


traceability_relationships = {
    'validates': 'validated_by',
    'ext_polarion_reference': ''
}

traceability_relationship_to_string = {
    'validates': 'Validates',
    'validated_by': 'Validated by',
    'ext_polarion_reference': 'Polarion reference'
}
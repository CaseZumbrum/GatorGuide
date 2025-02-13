# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "GatorGuide"
copyright = "2025, Case Zumbrum, Louis Li, Jack Kellen"
author = "Case Zumbrum, Louis Li, Jack Kellen"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import sys
import os

import os
import sys

sys.path.insert(
    0, os.path.abspath("../../src")
)  # Source code dir relative to this file

extensions = [
    "sphinx.ext.autodoc",  # Core library for html generation from docstrings
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",  # Create neat summary tables
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary
add_module_names = False
# Add any paths that contain templates here, relative to this directory.


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# ----------------------------------------------------------------------------
# --- MUST ADAPT THIS FILE FOR YOUR PROJECT ---
# --- Instructions below ---
#
# * Search and replace `jupyterhub-python-repo-template` with the name of your
#   repository
# ----------------------------------------------------------------------------


# Configuration file for Sphinx to build our documentation to HTML.
#
import datetime

# -- Project information -----------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
#
project = "jupyterhub-python-repo-template"
copyright = f"{datetime.date.today().year}, Project Jupyter Contributors"
author = "Project Jupyter Contributors"


# -- General Sphinx configuration ---------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#
extensions = [
    # jupyterhub_sphinx_theme activates the sphinx-copybutton and
    # sphinx-opengraph extensions as well.
    "jupyterhub_sphinx_theme",
    "autodoc_traits",
    "myst_parser",
    "sphinxext.rediraffe",
]
root_doc = "index"
source_suffix = [".md"]

# default_role is set for use with reStructuredText that we still need to use in
# docstrings in the autodoc_traits inspected Python module. It makes single
# backticks around text, like `my_function`, behave as in typical Markdown.
default_role = "literal"


# -- Options for HTML output -------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#
html_theme = "jupyterhub_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/jupyterhub/jupyterhub-python-repo-template/",
    "use_edit_page_button": True,
}
html_context = {
    "github_user": "jupyterhub",
    "github_repo": "jupyterhub-python-repo-template",
    "github_version": "main",
    "doc_path": "docs/source",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files, so
# a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# About html_logo and html_favicon configuration:
#
# jupyterhub_sphinx_theme provides a jupyterhub favicon (html_favicon) and logo
# by default, where the logo is provided for light/dark respectively not under
# html_logo but under html_theme_options.logo.[image_light|image_dark] which
# will take precedence over html_logo configuration.
#
# ref: https://github.com/pydata/pydata-sphinx-theme/blob/v0.12.0/docs/user_guide/branding.rst
# ref: https://github.com/choldgraf/jupyterhub-sphinx-theme/blob/f97104c11cae55869ddc8394eb83594bd5c7d075/src/jupyterhub_sphinx_theme/__init__.py#L17-L54
#


# -- Options for linkcheck builder -------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder
#
linkcheck_ignore = [
    r"(.*)github\.com(.*)#",  # javascript based anchors
    r"(.*)/#%21(.*)/(.*)",  # /#!forum/jupyter - encoded anchor edge case
    r"https://github.com/[^/]*$",  # too many github usernames / searches in changelog
    "https://github.com/jupyterhub/jupyterhub-python-repo-template/pull/",  # too many PRs in changelog
    "https://github.com/jupyterhub/jupyterhub-python-repo-template/compare/",  # too many comparisons in changelog
    r"https?://(localhost|127.0.0.1).*",  # ignore localhost references in auto-links
]
linkcheck_anchors_ignore = [
    "/#!",
    "/#%21",
]


# -- Options for the opengraph extension -------------------------------------
# ref: https://github.com/wpilibsuite/sphinxext-opengraph#options
#
# ogp_site_url is set automatically by jupyterhub-sphinx-theme
ogp_image = "_static/logo.png"
ogp_use_first_image = True


# -- Options for the rediraffe extension -------------------------------------
# ref: https://github.com/wpilibsuite/sphinxext-rediraffe#readme
#
# This extensions help us relocated content without breaking links. If a
# document is moved internally, a redirect like should be configured below to
# help us not break links.
#
rediraffe_branch = "main"
rediraffe_redirects = {
    # "old-file": "new-folder/new-file-name",
}

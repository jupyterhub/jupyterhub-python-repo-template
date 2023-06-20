# A file declaring commands for working with the Sphinx based documentation.
#
# Used on linux/mac computers from a terminal like
#
#   make <buildername>
#
# <buildername> should be recognized by "sphinx-build -M <buildername>" or via
# manually added commands in this file.
#
# ref: https://www.sphinx-doc.org/en/master/man/sphinx-build.html#options
#

# Variables that can be set from command line or via environment variables
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build

# We declare commands (aka. targets), but Makefile expects to only run them only
# if a file associated with them doesn't already exist. Declaring .PHONY is a
# trick to make them run anyhow.
.PHONY: Makefile

# Put it first so that "make" without argument is like "make help".
help: Makefile
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Manually added commands
# ----------------------------------------------------------------------------
#
# For local development:
# - builds and rebuilds html on changes to source
# - starts a livereload enabled webserver and opens up a browser
# 
devenv: Makefile
	sphinx-autobuild -b html --open-browser "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

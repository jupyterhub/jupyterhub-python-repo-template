# jupyterhub-python-repo-template

[![Documentation status](https://img.shields.io/readthedocs/jupyterhub-python-repo-template?logo=read-the-docs)](https://jupyterhub-python-repo-template.readthedocs.io/en/latest/?badge=latest)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jupyterhub/jupyterhub-python-repo-template/Test?logo=github)](https://github.com/jupyterhub/jupyterhub-python-repo-template/actions)
[![Code coverage](https://codecov.io/gh/jupyterhub/jupyterhub-python-repo-template/branch/main/graph/badge.svg)](https://codecov.io/gh/jupyterhub/jupyterhub-python-repo-template)
[![](https://img.shields.io/pypi/v/jupyterhub-python-repo-template.svg?logo=pypi)](https://pypi.python.org/pypi/jupyterhub-kubespawner)

This is a repository that contains a set of example files that, after tailoring, can be used to create GitHub repositories for new JupyterHub Python projects.

## How to use this repository



## Repository contents

This section describes the various files in this repository and how to modify them for your new project.

### Files that don't need changes

Some of the files in this repository can be used in a new project, just as they in this repository,
without needing to change anything.
The list of files in this category is the following:

1. `SECURITY.md`
2. `LICENSE`
3. `CODE-OF-CONDUCT.md`

### Files that need straightforward, minimal modifications:

The changes to following files should be pretty straighforward.
They should only require project specific additions or removals.

1. `docs/source/_static_/images/logo`
2. `pre-commit-config.yaml`
3. `MANIFEST.in`
4. `.readthedocs.yaml`

### Files needing more complex changes

#### Files in the root of the repository

1. `pyproject.toml`

Contains the [Hatch](https://hatch.pypa.io/latest/) build system requirements and information,
which will be used by pip to build the package.

There are detailed instructions just at the start of the file,
about how to proper adapt this file to your own project.
Please follow them.

#### Files in the docs directory


#### Files in the tests directory
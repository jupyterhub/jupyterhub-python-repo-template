# jupyterhub-python-repo-template

[![Documentation status](https://img.shields.io/readthedocs/jupyterhub-python-repo-template?logo=read-the-docs)](https://jupyterhub-python-repo-template.readthedocs.io/en/latest/?badge=latest)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jupyterhub/jupyterhub-python-repo-template/Test?logo=github)](https://github.com/jupyterhub/jupyterhub-python-repo-template/actions)
[![Code coverage](https://codecov.io/gh/jupyterhub/jupyterhub-python-repo-template/branch/main/graph/badge.svg)](https://codecov.io/gh/jupyterhub/jupyterhub-python-repo-template)
[![](https://img.shields.io/pypi/v/jupyterhub-python-repo-template.svg?logo=pypi)](https://pypi.python.org/pypi/jupyterhub-python-repo-template)

This is a repository that contains a set of example files that, after tailoring, can be used to create GitHub repositories for new JupyterHub Python projects.

*NOTE: The badges above 🔝 can and should also be configured for the new project you intend to create. This will make it be consistent with the rest of the respositories in the [jupyterhub organization](https://github.com/jupyterhub). Just replace any reference to this repository `jupyterhub-python-repo-template` with your project and the proper links the badges should point to.*

## How to use this repository

You can either:

- use the green button 🟩 that says `"Use this template"`.

  This will create a new repository, with the a name of your choice
  and with the exact contents of this repo.
  You can then follow the instructions in each on how to change them
  to match your project.

- directly copy just the content of the files you want and change them to match your project.

## 📚 Repository contents

This section describes the various files in this repository and how to modify them for your new project.

### Files that don't need changes

Some of the files in this repository can be used in a new project, just as they in this repository,
without needing to change anything.
The list of files in this category is the following:

- `SECURITY.md`
- `LICENSE`
- `CODE-OF-CONDUCT.md`

### Files that need straightforward, minimal modifications:

The changes to following files should be pretty straighforward.
They should only require project specific additions or removals.

- `docs/source/_static_/images/logo`
- `pre-commit-config.yaml`
- `MANIFEST.in`
- `.readthedocs.yaml`

### Files needing more complex changes

TODO

#### Files in the root of the repository

1. `pyproject.toml`

Contains the [Hatch](https://hatch.pypa.io/latest/) build system requirements and information,
which will be used by pip to build the package.

There are detailed instructions just at the start of the file,
about how to proper adapt this file to your own project.
Please follow them.

#### The docs directory
TODO

#### The tests directory
TODO
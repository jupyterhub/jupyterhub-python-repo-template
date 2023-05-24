# jupyterhub-python-repo-template

[![Latest PyPI version](https://img.shields.io/pypi/v/jupyterhub-python-repo-template?logo=pypi)](https://pypi.python.org/pypi/jupyterhub-python-repo-template)
[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/jupyterhub-python-repo-template?logo=conda-forge)](https://anaconda.org/conda-forge/jupyterhub-python-repo-template)
[![GitHub Workflow Status - Test](https://img.shields.io/github/actions/workflow/status/jupyterhub/jupyterhub-python-repo-template/test.yaml?logo=github&label=tests)](https://github.com/jupyterhub/jupyterhub-python-repo-template/actions)
[![Test coverage of code](https://codecov.io/gh/jupyterhub/jupyterhub-python-repo-template/branch/main/graph/badge.svg)](https://codecov.io/gh/jupyterhub/jupyterhub-python-repo-template)
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/jupyterhub-python-repo-template/issues)
[![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/jupyterhub)

This is a repository that contains a set of example files that, after tailoring, can be used to create GitHub repositories for new JupyterHub Python projects.

_NOTE: The badges above 🔝 can and should also be configured for the new project you intend to create. This will make it be consistent with the rest of the respositories in the [jupyterhub organization](https://github.com/jupyterhub). Just replace any reference to this repository `jupyterhub-python-repo-template` with your project and the proper links the badges should point to._

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

The files in this list can be used in a new project, just as they are, without changing their content.

- `SECURITY.md`
- `LICENSE`
- `CODE-OF-CONDUCT.md`

### Files that need to be adapted

The files in this section will need to be adapted to match your project's specifics.

#### Files that need straightforward, minimal modifications

The changes that need to be done to the following files should be pretty straighforward,
as, they should only require project specific additions or removals.

- `docs/source/_static_/images/logo`
- `pre-commit-config.yaml`
- `MANIFEST.in`
- `.readthedocs.yaml`

#### `pyproject.toml`

Contains the [Hatch](https://hatch.pypa.io/latest/) build system requirements and information,
which will be used by pip to build the package.

There are detailed instructions just at the start of the file,
about how to proper adapt this file to your own project.
Please follow them.

#### The docs directory

TODO

#### The tests directory

TODO

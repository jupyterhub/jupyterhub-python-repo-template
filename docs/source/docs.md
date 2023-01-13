(documentation)=

# Documentation

This section contains information about documentation practices and standards
that are usually used across JupyterHub project repositories.

## The recommended `docs` directory structure

The `docs` directory contains configuration files that are generally used across the `jupyterhub` organization projects.
The `docs` directory usually has the overall structure described below.

```
📦docs
 ┣ 📂source
 ┃ ┣ 📂_static
 ┃ ┃ ┗ 📂images
 ┃ ┃ ┃ ┗ 📂logo
 ┃ ┃ ┃ ┃ ┣ 📜favicon.ico
 ┃ ┃ ┃ ┃ ┗ 📜logo.png
 ┃ ┣ 📜changelog.md
 ┃ ┣ 📜conf.py
 ┃ ┗ 📜index.md
 ┣ 📂_build
 ┣ 📜Makefile
 ┣ 📜make.bat
 ┗ 📜requirements.txt
```

```{warning}
The following files, `conf.py`, `Makefile`, `make.bat` assume the structure above.
If you wish to change something to the overall structure, please consider changing the relevant fields
in these files.
```

## Hosting documentation

In general the JupyterHub team encourages the use of [ReadTheDocs](https://readthedocs.org/).
This is a service that hosts documentation stored in online repositories.

```{note}
Checkout the documentation in [team-compass](https://jupyterhub-team-compass.readthedocs.io/en/latest/resources/shared-infrastructure.html#documentation-and-readthedocs) for more information about this.
```

### The `.readthedocs.yaml` file

```{warning}
This file is located in the root of the repository and not in the `docs` directory.
```

This file contains configuration on how ReadTheDocs (RTD) will build the documentation. Checkout the RTD [docs](https://docs.readthedocs.io/en/stable/config-file/v2.html) about the config options in that file.

```{note}
The contents of this file usually won't need to be changed when used for a new repository.
However, consider changing it in the following cases:
- you want a different os version than `ubuntu-22.04` for the docs builder
- you want a different Python version than "3.10" for the docs builder
- you have a different `docs` directory structure (not recommended)
```

## How to adapt for a new repository

1. Change the `docs/source/conf.py` file according the instructions in that file

1. Add new Markdown files under the `docs/source` directory and group them using the [Diataxis framework](https://diataxis.fr/).

1. Based on the contents of the new files, consider adding more Sphinx extensions to `docs/source/conf.py` and `requirements.txt` according to what you want to achieve.

1. Update the `docs/source/changelog.md` file according to the instructions in that file and `RELEASE.md`

1. Add more static resources, like logos or images to `docs/source/_static`

1. Build the docs locally by running

   ```bash
   make html
   ```

1. Checkout the rendered html assets built by the `make` command in the newly generated `docs/_build` directory

   ```{note}
   Running make clean, will delete the `_build` directory.
   ```

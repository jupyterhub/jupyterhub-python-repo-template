(documentation)=

# Documentation

The `docs` directory contains configuration files that are generally used across the `jupyterhub` organization projects.

## The general, recommended directory structure

The `docs` directory usually has the overall structure described below.

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

```{warning}
The following files, `conf.py`, `Makefile`, `make.bat` assume the structure above.
If you wish to change something to the overall structure, please consider changing the relevant fields
in these files.
```
### 

## Hosting documentation

In general the JupyterHub team encourages the use of [ReadTheDocs](https://readthedocs.org/).
This is a service that hosts documentation stored in online repositories.

```{note}
Checkout the documentation in [team-compass](https://jupyterhub-team-compass.readthedocs.io/en/latest/resources/shared-infrastructure.html#documentation-and-readthedocs) for more information about this.
```

### The `.readthedocs.yaml` file

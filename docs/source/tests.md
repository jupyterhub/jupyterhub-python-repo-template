(tests)=

# Tests

This section contains information about testing practices and standards that are
usually used across JupyterHub project repositories.

## The recommended `tests` directory structure

TODO

## `pre-commit`, `.pre-commit-config.yaml`, and pre-commit.ci

[pre-commit] is a tool to perform a predefined set of tasks manually and/or
automatically before git commits are made.

We rely on the [pre-commit.ci] service to automatically run pre-commit as a test
when someone opens a PR, just like we rely on the GitHub Actions service to run
workflows defined in `.github/workflows`.

[pre-commit]: https://pre-commit.com/
[pre-commit.ci]: https://pre-commit.ci/

## How to adapt for a new repository

1. **Configure pre-commit.ci**

   As a jupyterhub admin, visit the jupyterhub GitHub organization's [Settings
   -> GitHub Apps] and click configure on `pre-commit ci`, then add this
   repository to the list of selected repositories the GitHub Application is
   activated for.

   [settings -> github apps]: https://github.com/organizations/jupyterhub/settings/installations

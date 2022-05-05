
# DF Cookiecutter

DF-cookiecutter simplifies creating add-ons for [Dialog Flow Framework](https://github.com/deepmipt/dialog_flow_engine), a minimalistic open-source bot engine.

The package uses [cookiecutter](https://github.com/cookiecutter/cookiecutter) to generate add-on templates that include all the necessary features, like makefile commands or automatized documentation. 

The derived packages are shipped with MIT license by default.

# Platforms

We suggest using a linux-based platform for development. 

While the template can be cloned on any device that can run python and cookiecutter, the makefile functionality will not be available.

# Usage

## Setting up a project

To use this package, you need to have [cookiecutter](https://github.com/cookiecutter/cookiecutter) installed into global scope.

```bash
pip install cookiecutter
```

When this is done, you can create your own add-on by simply calling cookiecutter from your CL interface and filling in the required values.

```bash
cookiecutter https://github.com/ruthenian8/df-cookiecutter.git
```

## Managing your workflow

After Cookiecutter clones the template for you, you can use a few make commands to get your development environment up and running.

The most essential part is setting up the virtual environment. The command also installs all the development dependencies.

```bash
make venv
# Do not forget to activate the environment, if you aim to install any other dependencies.
source venv/bin/activate
```

We also provide a simple hook that prevents you from commiting unlinted code. Note that this action will reinitialize the git repository inside the project directory, if you have already created one. To use it, run

```bash
make hooks
```

Assuming you use docstrings to annotate your modules and objects, you can easily build the Sphinx documentation for your module 
by ativating the virtual environment and then running

```bash
make build_doc
```

Use the command `help` to see more options:

```bash
make help
```

## Deployment

The template includes a handful of github workflows that allow you to lint and test your code as well as to deploy your newly made package straight to [PYPI](https://pypi.org/).

If you plan to use the latter feature, be sure to set the `PYPI_TOKEN` secret in your repository.

# Contributing to the {{cookiecutter.project_name}}

Please refer to [CONTRIBUTING.md]({{cookiecutter.url}}/blob/{{cookiecutter.default_git_branch}}/CONTRIBUTING.md).



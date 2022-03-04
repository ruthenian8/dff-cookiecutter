
# DFF Cookiecutter

DFF-cookiecutter simplifies creating add-ons for [Dialogflow Framework](https://github.com/deepmipt/dialog_flow_engine), a minimalistic open-source bot engine.

The package uses [cookiecutter](https://github.com/cookiecutter/cookiecutter) to generate add-on templates that include all the necessary features, like makefile commands or automatized documentation. 

The derived packages are shipped with MIT license by default.

# Usage

To use this package, you need to have [cookiecutter](https://github.com/cookiecutter/cookiecutter) installed into global scope.

```bash
pip install cookiecutter
```

When this is done, you can create your own add-on by simply calling cookiecutter from your CL interface.

```bash
cookiecutter https://github.com/ruthenian8/dff-cookiecutter.git
```

# Contributing to the Dialog Flow Framework

Please refer to [CONTRIBUTING.md](https://github.com/deepmipt/dialog_flow_engine/blob/dev/CONTRIBUTING.md).

# Dialog Flow Addon Template

**Dialog Flow Addon Template** provides template for add-on python modules for [Dialog Flow Framework](https://github.com/deepmipt/dialog_flow_framework), a minimalistic open-source bot engine.


Use [cookiecutter](https://github.com/cookiecutter/cookiecutter) to generate add-on repository from the template that include all the necessary features, like makefile commands, test, github actions and automatized documentation. 

The derived packages are shipped with [Apache-2.0](LICENSE) license by default.

# Platforms

We suggest using a linux-based platform for addon development. While the template can be cloned on any device that can run python and cookiecutter, the makefile functionality will not be available for Windows.

# Usage

## Setting up a project

To use this package, you need to have [cookiecutter](https://github.com/cookiecutter/cookiecutter) installed into your environment.

```bash
pip install cookiecutter
```

When this is done, you can create your own add-on by simply calling `cookiecutter` from your console interface and filling in the required values.

```bash
cookiecutter https://github.com/deepmipt/dialog_flow_addon_template.git
```
An example of filling:
```bash
addon_name [My Addon]: My first addon
addon_slug [dialog_flow_my_first_addon]: 
package_name [Dialog Flow My first addon]: Dialog Flow My First Addon
package_slug [df_my_first_addon]: 
version [0.0.1]: 
author [John Doe]: John
email [john@email.com]: john@gmail.com
git_repository_url [https://github.com/john/dialog_flow_my_first_addon]: 

```


## Workflow for you add-on
To start add-on developing your you can find more advices in [Add-on CONTRIBUTING.md]({{cookiecutter.addon_slug}}/CONTRIBUTING.md) of the add-on template.

# Contributing to the Dialog Flow Addon Template

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md).



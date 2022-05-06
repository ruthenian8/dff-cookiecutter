## Introduction
We will be glad to receive your pull requests and issues for adding new features if you are missing something.
We always look forward to your contributions to the {{cookiecutter.package_name}}. 

## Managing your workflow

After Cookiecutter creates the template for you, you can use a few make commands to get your development environment up and running.

### Virtual Environment
The most essential part is setting up the virtual environment. The command also installs all the development dependencies.

```bash
make venv
# Do not forget to activate the environment, if you aim to install any other dependencies.
source venv/bin/activate
```

### Pre-commit Hooks
We also provide a simple hook that prevents you from commiting unlinted code. Note that this action will reinitialize the git repository inside the project directory, if you have already created one. To use it, run

```bash
make hooks
```

### Documentation
Assuming you use docstrings to annotate your modules and objects, you can easily build the Sphinx documentation for your module 
by ativating the virtual environment and then running

```bash
make build_doc
```
after that `docs/build` dir was created and you can open index file by your browser:
```bash
$BROWSER docs/build/html/index.html
```
### Style
```bash
make format
```
### Test
```bash
make test_all
```
### Other provided features 
Use the command `help` to see more options:

```bash
make help
```

## Deployment

The template includes a handful of github workflows that allow you to lint and test your code as well as to deploy your newly made package straight to [PYPI](https://pypi.org/).

If you plan to use the latter feature, be sure to set the `PYPI_TOKEN` secret in your repository.

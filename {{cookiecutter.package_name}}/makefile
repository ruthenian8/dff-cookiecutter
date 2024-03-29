SHELL = /bin/bash

VENV_PATH = venv

help:
	@echo "Thanks for your interest in {{cookiecutter.project_name}}!"
	@echo
	@echo "make lint: Run linters"
	@echo "make test: Run basic tests (not testing most integrations)"
	@echo "make test-all: Run ALL tests (slow, closest to CI)"
	@echo "make format: Run code formatters (destructive)"
	@echo "make build_doc: Build Sphinx docs; activate your virtual environment before execution"
	@echo "make hooks: Register a git hook to lint the code on each commit"
	@echo "make bump_version_major: increment version major in metadata files 0.0.1 -> 1.0.1"
	@echo "make bump_version_minor: increment version minor in metadata files 0.1.1 -> 0.2.1"
	@echo "make bump_version_patch: increment patch number in metadata files 0.0.1 -> 0.0.2"
	@echo

venv:
	python3 -m venv $(VENV_PATH)
	$(VENV_PATH)/bin/pip install -e .
	$(VENV_PATH)/bin/pip install -r requirements_dev.txt
	$(VENV_PATH)/bin/pip install -r requirements_test.txt

format: venv
	@$(VENV_PATH)/bin/python -m black --exclude="setup\.py" --line-length=120 .
.PHONY: format

check: lint test
.PHONY: check

lint: venv
	$(VENV_PATH)/bin/python -m flake8 --config=setup.cfg {{cookiecutter.project_slug}}/
	@set -e && $(VENV_PATH)/bin/python -m black --exclude="setup\.py" --line-length=120 --check . || ( \
		echo "================================"; \
		echo "Bad formatting? Run: make format"; \
		echo "================================"; \
		false)

.PHONY: lint

test: venv
	@$(VENV_PATH)/bin/python -m pytest --cov-report html --cov-report term --cov={{cookiecutter.project_slug}} tests/
.PHONY: test

test_all: venv test lint
.PHONY: test_all

venv_activation_check:
if [ "`which python`" != "venv/bin/python" ]; then exit 1; fi 
.PHONY: venv_activation_check

build_doc:
	make venv_activation_check
	sphinx-apidoc -e -f -o docs/source/apiref {{cookiecutter.project_slug}}
	sphinx-build -M clean docs/source docs/build
	sphinx-build -M html docs/source docs/build
.PHONY: build_doc

hooks:
	@git init .
	-@git branch -m {{cookiecutter.default_git_branch}}
	@cp pre-commit.sh .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
.PHONY: hooks

bump_version_patch:
	@$(VENV_PATH)/bin/python -m bump2version patch
.PHONY: bump_version_patch

bump_version_minor:
	@$(VENV_PATH)/bin/python -m bump2version minor
.PHONY: bump_version_minor

bump_version_major:
	$(VENV_PATH)/bin/python -m bump2version major
.PHONY: bump_version_major

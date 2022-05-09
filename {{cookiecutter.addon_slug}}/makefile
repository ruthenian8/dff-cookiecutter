SHELL = /bin/bash

VENV_PATH = venv
VERSIONING_FILES =  setup.py makefile docs/source/conf.py {{cookiecutter.package_slug}}/__init__.py
CURRENT_VERSION = {{cookiecutter.version}} 

help:
	@echo "Thanks for your interest in Dialog Flow My Addon!"
	@echo
	@echo "make lint: Run linters"
	@echo "make test: Run basic tests (not testing most integrations)"
	@echo "make test-all: Run ALL tests (slow, closest to CI)"
	@echo "make format: Run code formatters (destructive)"
	@echo "make build_doc: Build Sphinx docs; activate your virtual environment before execution"
	@echo "make pre_commit: Register a git hook to lint the code on each commit"
	@echo "make bump_version_major: increment version major in metadata files 0.0.1 -> 1.0.0"
	@echo "make bump_version_minor: increment version minor in metadata files 0.1.1 -> 0.2.0"
	@echo "make bump_version_patch: increment patch number in metadata files 0.0.1 -> 0.0.2"
	@echo

venv:
	@if [ "`which python`" != "venv/bin/python" ] ; 	then \
		echo "Start creating virtual environment";\
		python3 -m venv $(VENV_PATH);\
	fi

	$(VENV_PATH)/bin/pip install -e . ;
	$(VENV_PATH)/bin/pip install -r requirements_dev.txt ;
	$(VENV_PATH)/bin/pip install -r requirements_test.txt ;
	

format: venv
	$(VENV_PATH)/bin/python -m black --exclude="setup\.py" --line-length=120 .
.PHONY: format

lint: venv
	$(VENV_PATH)/bin/python -m flake8 --config=setup.cfg {{cookiecutter.addon_slug}}/
	@set -e && $(VENV_PATH)/bin/python -m black --exclude="setup\.py" --line-length=120 --check . || ( \
		echo "================================"; \
		echo "Bad formatting? Run: make format"; \
		echo "================================"; \
		false)
	$(VENV_PATH)/bin/python -m mypy --config=setup.cfg {{cookiecutter.addon_slug}}/

.PHONY: lint

test: venv
	$(VENV_PATH)/bin/python -m pytest --cov-report html --cov-report term --cov={{cookiecutter.addon_slug}} tests/
.PHONY: test

test_all: venv test lint
.PHONY: test_all

build_doc:
	if [ "`which python`" != "venv/bin/python" ]; then exit 1; fi 
	sphinx-apidoc -e -f -o docs/source/apiref {{cookiecutter.addon_slug}}
	sphinx-build -M clean docs/source docs/build
	sphinx-build -M html docs/source docs/build
.PHONY: build_doc

pre_commit: venv
	echo -e "#!/bin/sh\n\nmake test_all" > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
.PHONY: pre_commit

bump_version_patch: venv
	bump2version --current-version $(CURRENT_VERSION) patch $(VERSIONING_FILES)
.PHONY: bump_version_patch

bump_version_minor: venv
	bump2version --current-version $(CURRENT_VERSION) minor $(VERSIONING_FILES)
.PHONY: bump_version_minor

bump_version_major: venv
	bump2version --current-version $(CURRENT_VERSION) major $(VERSIONING_FILES)
.PHONY: bump_version_major

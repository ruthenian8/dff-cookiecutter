import sys

import pytest

from {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}} import main

# uncomment the following line, if you want to run your examples during the test suite or import from them
# sys.path.insert(0, "../")


def test_main():
    assert main() is None

import pytest
import os
import re

from binaryornot.check import is_binary

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [os.path.join(dirpath, file_path) for dirpath, subdirs, files in os.walk(root_dir) for file_path in files]


def check_path(path):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    if is_binary(path):
        return True

    for line in open(path, "r"):
        match = RE_OBJ.search(line)
        if match:
            return False
    return True


def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_name": "Test Project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.context["package_name"] == "test-project"
    assert result.project_path.name == "test-project"
    assert os.path.isdir(result.project_path)
    assert result.context["project_slug"] == "test_project"
    slug_dir = os.path.join(result.project_path, result.context["project_slug"])
    assert os.path.isdir(slug_dir)
    paths = build_files_list(str(result.project_path))
    assert paths
    for path in paths:
        assert check_path(path)

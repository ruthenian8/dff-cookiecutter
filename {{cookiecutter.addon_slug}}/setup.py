#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip
import pathlib

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import find_packages


LOCATION = pathlib.Path(__file__).parent.resolve()


def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    lines = (line.strip() for line in (LOCATION / filename).open())
    return [line for line in lines if line and not line.startswith("#")]


# Get the long description from the README file
readme_file = LOCATION / "README.md"

readme_lines = [line.strip() for line in readme_file.open(encoding="utf-8").readlines()]
description = [line for line in readme_lines if line and not line.startswith("#")][0]
long_description = "\n".join(readme_lines)


requirements = parse_requirements("requirements.txt")

test_requirements = parse_requirements("requirements_test.txt")


setup(
    name="{{cookiecutter.package_slug}}",
    version="{{cookiecutter.version}}",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{{cookiecutter.git_repository_url}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    classifiers=[  # Optional
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["chatbots", "{{ cookiecutter.package_name }}"],  # Optional
    packages=find_packages(where="."),  # Required
    include_package_data=True,
    python_requires=">=3.6, <4",
    install_requires=requirements,
    test_suite="tests",
    tests_require=test_requirements,
)

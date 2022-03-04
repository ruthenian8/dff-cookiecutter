#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip
import pathlib
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import find_packages


LOCATION = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
readme_file = LOCATION / "README.md"

readme_lines = [line.strip() for line in readme_file.open(encoding="utf-8").readlines()]
description = [line for line in readme_lines if line and not line.startswith("#")][0]
long_description = "\n".join(readme_lines)


parsed_requirements = [
    str(item.req) for item in parse_requirements(
        'requirements.txt',
        session='workaround'
    )
]

test_requirements = [
    str(item.req) for item in parse_requirements(
        'requirements_test.txt',
        session='workaround'
    )
]


setup(
    name="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version}}",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{{cookiecutter.url}}",
    author="{{cookiecutter.full_name}}",
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
    keywords=["chatbots", '{{ cookiecutter.package_name }}'],  # Optional
    packages=find_packages(where="."),  # Required
    include_package_data=True,
    python_requires=">=3.6, <4",
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements
)

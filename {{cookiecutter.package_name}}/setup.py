from setuptools import setup, find_packages
import pathlib
from setuptools.command.install import install


LOCATION = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
readme_file = LOCATION / "README.md"

readme_lines = [line.strip() for line in readme_file.open(encoding="utf-8").readlines()]
description = [line for line in readme_lines if line and not line.startswith("#")][0]
long_description = "\n".join(readme_lines)


def read_requirements():
    """parses requirements from requirements.txt"""
    reqs_file = LOCATION / "requirements.txt"
    reqs = [line.strip() for line in reqs_file.open(encoding="utf8").readlines() if not line.strip().startswith("#")]

    names = []
    links = []
    for req in reqs:
        if "://" in req:
            links.append(req)
        else:
            names.append(req)
    return {"install_requires": names, "dependency_links": links}


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
    keywords="chatbots",  # Optional
    packages=find_packages(where="."),  # Required
    python_requires=">=3.6, <4"
)

"""
A collaboration in Python.
"""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path().resolve()
long_description = (here / 'README.rst').read_text(encoding='utf-8')

setup(
    name="storybook",
    version="0.0.0",
    description=("A collaboration in Python."),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/blakeNaccarato/storybook",
    author="Blake Naccarato",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=["PyYAML"]
)

"""
One possible solution to the Story of a Mage.
"""

from setuptools import find_packages, setup

setup(
    name="tome",
    version="0.0.0",
    description=("One possible solution to the Story of a Mage."),
    long_description_content_type="text/markdown",
    author="Blake Naccarato",
    package_dir={"": "src"},
    packages=find_packages(where=r"adventure\src"),
    python_requires=">=3.7",
)

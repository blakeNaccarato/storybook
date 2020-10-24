"""Configuration file for sphinx-build.

The main configuration file for building documentation with Sphinx.
Run [>Tasks: Run Build Task] (CTRL+SHIFT+B) in VSCode to build. Open the file
"./docs/_build/html/index.html" in Chrome to check. Variables appear in alphabetical
order unless one depends on another.

If you're getting build errors, you may need to manually create the ".docs/_build" and
".docs/_static" folders.
"""

# pylint: disable=invalid-name

import pathlib
import sys

# So we can write "package.module" instead of "../src/package.module"
sys.path.insert(0, str(pathlib.Path(r"..\src").resolve()))

author = "Blake Naccarato"
copyright = "2020, Blake Naccarato"  # pylint: disable=redefined-builtin

# A list of glob-style patterns that should be excluded when looking for source files
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Extensions to use in processing files
extensions = [
    # built-in
    "sphinx.ext.napoleon",  # Convert readable docstrings to RST #! List before autodoc
    "sphinx.ext.autodoc",  # Parse RST in docstrings
    # Must pip install before using
    "sphinx_rtd_theme",  # The theme we're using
]

html_theme = "sphinx_rtd_theme"  # It must also appear in our extensions

# A list of paths with custom static files (such as style sheets or script files).
html_static_path = ["_static"]

project = "storybook"  # The project name
source_suffix = ".rst"  # So we can do ".. include:: ../README.rst"

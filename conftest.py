"""Test documentation.

Finds text in code blocks.
"""

from sybil import Sybil
from sybil.parsers.codeblock import CodeBlockParser
from sybil.parsers.doctest import DocTestParser

pytest_collect_file = Sybil(
    parsers=[
        CodeBlockParser(),
        DocTestParser(),
    ],
    pattern="*.rst",
).pytest()

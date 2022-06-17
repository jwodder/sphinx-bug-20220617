"""
Demonstration of a Sphinx bug

Visit <https://github.com/jwodder/sphinx-bug-20220617> for more information.
"""

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "sphinx-bug-20220617@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/sphinx-bug-20220617"

from typing import AnyStr, Generic, TypeVar

T = TypeVar("T")


class Genericized(Generic[T]):
    """This inherits ``Generic[T]``, and Sphinx shows that."""


class AnyStrable(Generic[AnyStr]):
    """This inherits ``Generic[AnyStr]``, but Sphinx leaves off the `AnyStr`."""

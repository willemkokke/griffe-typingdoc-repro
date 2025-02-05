"""Module to test griffe-typingdoc."""

from typing import Annotated

from pydantic import StringConstraints
from typing_extensions import Doc


ChecksumString = Annotated[
    str, Doc("A sha256 checksum."), StringConstraints(pattern="^[a-fA-F0-9]{64}$")
]


ChecksumString2 = Annotated[str, StringConstraints(pattern="^[a-fA-F0-9]{64}$")]
"""Alternative checksum string."""

NormalString = Annotated[str, Doc("A normal string.")]


def hi(to: Annotated[str, Doc("Who to say hi to")]) -> None:
    """Say hi to someone."""
    print(f"Hi {to}!")


def hi_no_docstring(to: Annotated[str, Doc("Who to say hi to")]) -> None:
    print(f"Hi {to}!")

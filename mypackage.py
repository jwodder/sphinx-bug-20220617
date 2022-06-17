from typing import AnyStr, Generic, TypeVar

T = TypeVar("T")

class Genericized(Generic[T]):
    ...

class AnyStrable(Generic[AnyStr]):
    ...

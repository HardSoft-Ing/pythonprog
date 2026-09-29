# This module shows variable annotations, a syntax in python to 
# give show hints for the variable usage. 
#

# Basic types
name: str = "Alice"
age: int = 30
height: float = 5.9
is_active: bool = True
# No error since type annotation 'bool' is just a hint and gets ignored by the interpreter!
bad_bool: bool = "A bad bool"
print(f"bad_bool type: {type(bad_bool)}, value: {bad_bool}")
# Dunder attribute __class__ is same as type()
print(f"bad_bool type: {bad_bool.__class__})

# Without initialization (just the type hint)
count: int
message: str

# Collections
numbers: list[int] = [1, 2, 3]
mapping: dict[str, int] = {"a": 1, "b": 2}
items: tuple[str, ...] = ("x", "y", "z")

# From typing module
from typing import Optional, List
optional_value: Optional[str] = None
values: List[int] = [1, 2, 3]
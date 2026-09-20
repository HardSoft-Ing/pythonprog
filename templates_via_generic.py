from typing import Generic, TypeVar

T = TypeVar("T")

# C++-like generic template in Python syntax
class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    def get(self) -> T:
        return self._value

    def set(self, value: T) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"Box({self._value!r})"

# Different template specializations:
# Box[int], Box[str], Box[float], Box[bool]
box_int = Box[int](10)
box_str = Box[str]("hello")
box_float = Box[float](3.14)
box_bool = Box[bool](True)

box_nogen_int = Box(10)
box_nogen_str = Box("hello")
box_nogen_float = Box(3.14)
box_nogen_bool = Box(True)

print("--- Before updates:")
print("box_int =",   box_int)
print("box_str =",   box_str)
print("box_float =", box_float)
print("box_bool =",  box_bool)

print("box_nogen_int =",   box_nogen_int)
print("box_nogen_str =",   box_nogen_str)
print("box_nogen_float =", box_nogen_float)
print("box_nogen_bool =",  box_nogen_bool)





# Assign values through setter methods, like C++ style set()
box_int.set(42)
box_str.set("world")
box_float.set(2.71)
box_bool.set(False)

print("\n--- After updates:")
print("box_int.get() =", box_int.get())
print("box_str.get() =", box_str.get())
print("box_float.get() =", box_float.get())
print("box_bool.get() =", box_bool.get())

# Show values directly through the object state
print("\nDirect state access:")
print("box_int._value =", box_int._value)
print("box_str._value =", box_str._value)
print("box_float._value =", box_float._value)
print("box_bool._value =", box_bool._value)

# A list of Boxes of type int, similar to std::vector<Box<int>>
items: list[Box[int]] = [Box[int](1), Box[int](2), Box[int](3)]
print("\nitems =", items)
for item in items:
    print("item.get() =", item.get())

# Extra example: a generic function that accepts any Box[T]
def print_box_value(box: Box[T]) -> None:
    print("generic print:", box.get())

print("\nGeneric function calls:")
print_box_value(box_int)
print_box_value(box_str)

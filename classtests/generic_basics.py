from typing import Generic, TypeVar
###
# Small AI generated tutorial of how to define typed classes via Generic[].
# Note: 
# - The type-declarations are only useful for Python type-checking tools but are
#   currently ignored by <= Python 3.14 interpreters.
#   TODO::fschaitb: Check if we can execute Python by recognizing types too.
# - The list-op '[]' for classType[] not relates to a list! Its the Python way of how to add type info. 
#   Its equivalent to the tuple-op '()' which is used for inheritance like classType(SomeBaseCls).


# T is a placeholder for a type. It is replaced by a concrete type when
# a type checker sees an expression such as Box[int] or Box[str].
T = TypeVar("T")


class Box(Generic[T]):
    """A container whose stored value has type T."""

    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value

    def set(self, value: T) -> None:
        self.value = value


# Box[int] is generic type syntax, not a list. It means that this Box is
# intended to contain an int. The information is mainly used by type checkers.
box_int = Box[int](10)
box_str = Box[str]("hello")

print("box_int:", box_int.get())
print("box_str:", box_str.get())
print("The runtime class is still Box:", type(box_int) is Box)
print("The generic alias is:", Box[int])

# !ATTENTION! Misusing types works in Python as it ignores type-hints!
box_bad_int = Box[int]("SomeText")
box_bad_str = Box[str](55)
print(f"box_bad_int: '{box_bad_int.get()}', class-type is just: {type(box_bad_int)}")
print(f"box_bad_str: '{box_bad_str.get()}', class-type is just: {type(box_bad_str)}")
# Python gives a shit on even swapping value-types!
box_bad_int.set(55); box_bad_str.set("SomeText")
print(f"Swapped values box_bad_int: '{box_bad_int.get()}'")
print(f"Swapped values box_bad_str: '{box_bad_str.get()}'")


# Multiple comma-separated type arguments are possible when the generic
# class declares multiple TypeVars.
U = TypeVar("U")

class Pair(Generic[T, U]):
    """A container with two independently typed values."""

    def __init__(self, first: T, second: U) -> None:
        self.first = first
        self.second = second


# Here T is int and U is str.
pair = Pair[int, str](10, "ten")

print("pair.first:", pair.first)
print("pair.second:", pair.second)
print("The pair type is:", Pair[int, str])


# This class shows the mechanism behind subscription syntax such as Box[int].
# Python calls __class_getitem__ when a class is followed by square brackets.
class InspectSubscription:
    @classmethod
    def __class_getitem__(cls, item: object) -> str:
        return f"{cls.__name__} received {item!r}"


print(InspectSubscription[int])
print(InspectSubscription[int, str])


# The brackets do not create a list. This is a list literal:
types_as_a_list = [int, str]
print("A real list of types:", types_as_a_list)

# Functions named __func__() are called dunder or magic methods 
# (see https://www.geeksforgeeks.org/python/dunder-magic-methods-python)
# ---
# The following applies:
# - All basic python types (actually classes) like int, float, list etc. consists of those
#   __xxx__ functions: E.g. for int we can display them via "print(dir(int))"
# - The operators [], =, +, * etc. are based on magic functions.
# - Deriving a class from e.g. int inherits all its magics. 
# - We can support for our custom-classes all python-operators by implementing the underlying
#   magics. 


print(f"List 'int' magics:\n{dir(int)}")

# - Inherit all int magics and print them.
class inherint(int):
    # Print self-reflection from class method level.
    def print(self):
        print(f"# List class {type(self).__name__} magics:\n{dir(self)}")
    pass
# Print inherint magics via main-function and class method. 
print(f"## List class {inherint.__name__} magics:\n{dir(inherint)}")
obj=inherint()
obj.print()


# - Custom class supporting read/write for operator []
class MyIndexRead:
    def __init__(self, *args):
        # To obtain a list not a tuple we shall expand *args by '= [*args]'
        self.values = [*args]
    # Implements read-op []
    def __getitem__(self, index):
        return self.values[index]
    # Implements write-op []
    def __setitem__(self, index, value):
        self.values[index] = value

item = MyIndexRead(1,2,3)
print(f"Default item[1]: {item[1]}") 
item[1] = 55
print(f"New item[1]: {item[1]}") 
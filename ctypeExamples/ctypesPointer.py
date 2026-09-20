from ctypes import *
import ctypes

# Pointer "pi" on int value "i":
i = c_int(42)
pi = pointer(i)
# deference pi
print ("pi value:", pi[0])
# show pi content (type and value):
print ("pi.contents:", pi.contents)



class Bar(Structure):
    _fields_ = [("count", c_int), ("values", POINTER(c_int))]

bar = Bar()
# Create c_int Array-Types of fixed element-size (e.g. 3, 5):
# Note: c_int defines the operator-overloads:
# - (c_int * x): c_int.__mul__()
# - (x * c_int): c_int.__rmul__()
TypeArr3 = (c_int * 3)
TypeArr5 = (5 * c_int)
print(f"Types {TypeArr3.__name__}: {TypeArr3}, {TypeArr5.__name__}: {TypeArr5}") 

# - create array instance from TypeArr3 initialized by values.
intArr = TypeArr3(1, 2, 3);
print("intArr:", intArr);
# Convert intArr array to pointer just by assignment. 
bar.values = intArr;
print ("bar.values:", bar.values);
# Alternative short form of the above with intArr!
#bar.values = (c_int * 3)(1, 2, 3);
bar.count = 3

for i in range(bar.count):
    print (bar.values[i]);


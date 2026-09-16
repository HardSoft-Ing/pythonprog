from ctypes import *
import ctypes
# --- Load shared libc for Winodws or Linux
# Structs shall be derived from cytpes "Structure"

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("z", c_int)
                ]

print("POINT.x:", POINT.x); print("POINT.y:", POINT.y)
point = POINT(10, 20, 30)
print ("Points:", point.x, point.y, point.z)

# Bitfields.

class Int(Structure):
   # define 2 "int bit-fields" + 1 "int" 
    _fields_ = [("first_16", c_int, 10),
                ("second_16", c_int, 16),
                ("third_int", c_int)                 
              ]
print(Int.first_16); print(Int.second_16); print(Int.third_int)


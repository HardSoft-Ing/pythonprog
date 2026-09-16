from ctypes import *

# --- Load shared libc for Winodws or Linux
import sys
if sys.platform == "win32":
    # libc of Windows
    #libc = cdll.msvcrt 
    libc = CDLL('msvcrt.dll')
else:    
    # libc of Linux
    libc = CDLL('libc.so.6')
    
class Bottles(object):
       def __init__(self, number):
# ctypes requires a member named _as_parameter_ to convert any object into a number or string.
           self._as_parameter_ = number

bottles = Bottles(42)
libc.printf(b"%d bottles of beer\n", bottles)


# --- call strchr

# Define strchr()'s return type as "string" since "int" by default is assumed. 
libc.strchr.restype = c_char_p;
# Define strchr()'s argument types to avoid type conversion.
libc.strchr.argtypes = [c_char_p, c_char]

val = libc.strchr(b"abcdef", b"d");
print (val);

# --- call sscanf

i = c_int()
f = c_float()
# We can use either create_string_buffer() or c_char_p to create a ctypes string object.
#s = create_string_buffer(b'\000' * 32)
s = c_char_p(b"\000")
print (i.value, f.value, repr(s.value))

libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
            # use "ctypes.byref" to access a primitive variable by reference (like a pointer)  
            byref(i), byref(f), s)

print (i.value, f.value, s.value)

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("z", c_int)
                ]

point = POINT(10, 20, 30)
print ("Points:", point.x, point.y, point.z)

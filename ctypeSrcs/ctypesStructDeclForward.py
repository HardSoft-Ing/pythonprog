from ctypes import *
import ctypes

# --- Load shared libc for Winodws or Linux
#import sys
#if sys.platform == "win32":
#    # libc of Windows
#    libc = cdll.msvcrt 
#else:    
#    # libc of Linux
#    libc = CDLL('libc.so.6')
#
# --- Class with next-pointer on it self. This approach uses a foward declaration likewise C  
#     by defining class "cell" as incomplete class. 

# Incomplete class to be used for forwad declaration
class cell(Structure):
    pass
# Delayed adding of class members. 
cell._fields_ = [("name", c_wchar_p),
                 ("next", POINTER(cell))]

c1 = cell()
c1.name = "foo"
c2 = cell()
c2.name = "bar"
c1.next = pointer(c2)
c2.next = pointer(c1)
p = c1
for i in range(8):
    print(p.name, end=" ")
    p = p.next[0]

print("\n");
    
# --- Alternative approach without forward declaration but void-pointer with class-pointer-cast!

class cellx(Structure):
    _fields_ = [("namex", c_wchar_p),
               ("nextx", c_void_p)]

cx1 = cellx()
cx1.namex = "foox"
cx2 = cellx()
cx2.namex = "barx"
cx1.nextx = cast(pointer(cx2), c_void_p)
cx2.nextx = cast(pointer(cx1), c_void_p)
p = cx1
for i in range(8):
    print(p.namex, end=" ")
    p = (cast(p.nextx, POINTER(cellx)))[0]
    
print("\n");    
from ctypes import *
import ctypes
# --- Load shared libc for Winodws or Linux
import sys
if sys.platform == "win32":
    # libc of Windows
    libc = cdll.msvcrt 
else:    
    # libc of Linux
    libc = CDLL('libc.so.6')

# --- call sscanf --------------------------


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# TODO: sscanf fails with cytpe pointers. Use create_string_buffer()
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

i = c_int()
f = c_float()
# We must use create_string_buffer() to create a buffer to be filled by C function sscanf()
# Note: be sure that sscanf() would not exceed the length of s (here 100).
s = create_string_buffer(b'\000',  100)

print ("i.value:", i.value, ", f.value:", f.value, ", s.value:", s.value, ", s.value len:", len(s.value) ) ;

# --- call sscanf via byref()

libc.sscanf(b"1 3.14 Hello_World_and_all_the_gooda_people_of_the_world", b"%d %f %s",
            # use "ctypes.byref" to access a primitive variable by reference (like a pointer)  
            byref(i), byref(f), s)

print ("sscanf via byref():");
print ("i.value:", i.value, ", f.value:", f.value, ", s.value:", s.value, ", s.value len:", len(s.value) );
# Note: s is an instance of create_string_buffer() and thus will be interpreted always as char-string. 
# But we can print the int-values of each char via ord():
print("xxx ord(s[0]):", ord(s[0]));
input("press ENTER to continue after ord() ...")

# To parse a string-value via sscanf it seems that we can use 
# - a ctypes c_char array
# - a python string via c_char_p
sp = (c_char * 100)();     # Must be defined long enough
#sp = c_char_p(b'xxxBla'); # Seems to work too but shall no be used as c_char_p uses a constant-string as buffer!!!
print ("i.value:", i.value, ", f.value:", f.value, ", sp.value:", sp.value, ", sp.value len:", len(sp.value) );

# --- call sscanf via pointer()

libc.sscanf(b"233 6.28 Hello_all_the_gooda_people_of_the_world", b"%d %f %s",
            # use "ctypes.byref" to access a primitive variable by reference (like a pointer)  
            pointer(i), pointer(f), sp)

print ("sscanf via pointer():");
print ("i.value:", i.value, ", f.value:", f.value, ", sp.value:", sp.value, ", sp.value len:", len(sp.value) );





class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("z", c_int)
                ]

point = POINT(10, 20, 30)
print ("Points:", point.x, point.y, point.z)

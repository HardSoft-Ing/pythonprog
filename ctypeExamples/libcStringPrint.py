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
class Bottles(object):
       def __init__(self, number):
# if we create the member _as_parameter_ ctypes will used it as argument to any libc call. 
           self._as_parameter_ = number

bottles = Bottles(42)
# ctypes invokes bottles._as_parameter_ in the printf call!
libc.printf(b"%d bottles of beer\n", bottles)


# --- call strchr

# Define strchr()'s return type as "string" since "int" by default is assumed. 
libc.strchr.restype = c_char_p;

opt1 = 0;
if(opt1):
    # --- Option 1: Define strchr()'s c_types argument-types to a avoid creating intermediate c_type wrapper objects.
    libc.strchr.argtypes = [c_char_p, c_char]
    val = libc.strchr(b"abcdef", b"d");
else:    
    # --- Option 2: If we use strchr() without  c_type-argument definitions we must convert the arguments into the 
    #     the expecte ctypes first!
    val = libc.strchr(c_char_p(b"abcdef"), c_char(b"d"));

print ("strchr-val:", val);



# --- call sscanf --------------------------

i = c_int()
f = c_float()
# We must use create_string_buffer() to create a buffer being filled by C function sscanf()
# Note: be sure that sscanf() would not exceed the length of s (here 100).
s = create_string_buffer(b'\000',  100)
# It seems that using  c_char_p() pointer-type rather than create_string_buffer() works too
# but this seems quite dangerous since how could python know the space it must allocate for sscanf()???
#s = c_char_p(b'xxxTest');

print ("i.value:", i.value, ", f.value:", f.value, ", s.value:", s.value, ", s.value len:", len(s.value) ) ;

# --- call sscanf via byref()

libc.sscanf(b"1 3.14 Hello_World_and_all_the_gooda_people_of_the_world", b"%d %f %s",
            # use "ctypes.byref" to access a primitive variable by reference (like a pointer)  
            byref(i), byref(f), s)

print ("sscanf via byref():");
print ("i.value:", i.value, ", f.value:", f.value, ", s.value:", s.value, ", s.value len:", len(s.value) );

s = c_char_p(b'xxxBla');

print ("i.value:", i.value, ", f.value:", f.value, ", s.value:", s.value, ", s.value len:", len(s.value) );


# --- call sscanf via pointer()

libc.sscanf(b"233 6.28 Hello_all_the_gooda_people_of_the_world", b"%d %f %s",
            # use "ctypes.byref" to access a primitive variable by reference (like a pointer)  
            pointer(i), pointer(f), s)

print ("sscanf via pointer():");
print ("i.value:", i.value, ", f.value:", f.value, ", s.value:", s.value, ", s.value len:", len(s.value) );


print ("Points:", point.x, point.y, point.z)

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
    
# --- UVSock struct SSTR
class SSTR(Structure):
    _fields_ = [("nLen", c_int),
                ("szStr", c_char_p)]

# --- UVSock struct EXECCMD
class EXECCMD(Structure):
    _fields_ = [("bEcho", c_int, 1),
                ("_pad0_", c_int, 31),
                ("nRes", c_int, 7),
                ("sCmd", SSTR)]
                


    

# Note, don't use a pointer since it causes a memory violation.
if USE_POINTER:
  # Pointer don't works: It seems that it can't allocate an memory array.
  #pia = pointer(c_int());
  pia = (c_int * 1)();
  print("pia before resize:", pia);
  resize(pia, 8);
  print("pia after resize:", pia);
  cnt = 0;
  for val in (5, 1, 7, 5, 5, 7, 33, 99):
    pia[cnt] = c_int(val); 
    cnt +=1 ;
else:    
  # Define int x 8 array
  pia = (c_int *8)(5, 1, 7, 5, 5, 7, 33, 99);
  cnt = 8;
  # Alternative array definition: 
  ## 1. define array-type IntArray8
  #IntArray8 = c_int * 8;
  ## 2. define array-instance of IntArray8 initialized by values. 
  #ia = IntArray8(5, 1, 7, 5, 5, 7, 33, 99)


qsort = libc.qsort
qsort.restype = None

# Function pointer (int, int*, int*)
CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

# compare callback-function for qsort()
def py_cmp_func(a, b):
    print("py_cmp_func:", a[0], ">", b[0])
    return (a[0] > b[0]) - (a[0] < b[0])

#qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func))

qsort(pia, cnt, sizeof(c_int), CMPFUNC(py_cmp_func))
 
for icnt in range(cnt):
  print ("elem:", pia[icnt]);

  
print ("done")  

from ctypes import *

#import ctypes

# --- Load shared libc for Winodws or Linux
import sys
if sys.platform == "win32":
    # libc of Windows
    # Load libc short-form form Windows
    #libc = cdll.msvcrt 
    # Load libc as literal dll-file name (same as cdll.msvcrt) 
    libc = CDLL('msvcrt.dll')
else:    
    # libc of Linux
    libc = CDLL('libc.so.6')

qsort = libc.qsort
# Indicate to python that qsort() returns "void", see "GNU C library" documentation. .
qsort.restype = None


# Explicit ctypes array-type definitions for c_uint elements.
UintArr8_t = c_uint * 8
UintArr10_t = c_uint * 10
print (f"# Array-type-length UintArr8_t: {UintArr8_t._length_}, UintArr10_t: {UintArr10_t._length_}")
# Instantiate uint-arrays:
uint8Vals = UintArr8_t(18,28,38,48,58)
uint10Vals = UintArr10_t(11,22,33,44,55,66,7,88,99,100)
print (f"# Instance uint8Vals len: {len(uint8Vals)}, uint8Vals len: {len(uint10Vals)}")

# Make immediate c_int array-instance without explicit array-type definition: 
## 1. Implicit defines array-type IntArrayXX
#IntArrayXX = c_int * XX;
## 2. create array-instance of IntArrayXX initialized by values. 
#iarr = IntArrayXX(5, 1, 7, 5, 5, 7, 33, 99)
# Define c_int array with 10 elements, filled by 8 values. 
iarr = (c_int * 10)(5, 1, 7, 5, 5, 7, 33, 99)
# Get element count of iarr via len().
cnt_iarr =  len(iarr);

# Define string-pointer (c_wchar_p) array with 8 elements. 
# Note: we even can sort strings if we pass them as array of wchar-pointers. 
wsarr = (c_wchar_p * 10)("5c", "1b", "7b", "5b", "5b","7b", "3a", "9a");
# Use a C-style element count of wsarr! Note, we use "//" to get python 
# doing an int division rather than float!!!
cnt_wsarr =  sizeof(wsarr)//sizeof(c_wchar_p);




# Function pointer (int, int*, int*)
CMPFUNC_I = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
# Function pointer (int, wchar**, wchar**)
CMPFUNC_WS = CFUNCTYPE(c_int, POINTER(c_wchar_p), POINTER(c_wchar_p))

# compare callback-function for qsort()
# Note: 
def py_cmp_func(a, b):
    # Ignore "void" (== "None") elements!
    if (a[0] == None or b[0] == None): return 0; 
    # Calculate compare result, 1: a>b, 0: a==b, -1: a<b. 
    cmpres = (a[0] > b[0]) - (a[0] < b[0]);
    print("py_cmp_func, compare a[0]/b[0]:", a[0], ",", b[0], ":",cmpres);
    #print ("xxx type a/b:",a,b); # type a is c_int-array
    return cmpres;


qsort(iarr, cnt_iarr, sizeof(c_int), CMPFUNC_I(py_cmp_func));
for icnt in range(cnt_iarr):
  print ("int-elem:", iarr[icnt]);

qsort(wsarr, cnt_wsarr, sizeof(c_wchar_p), CMPFUNC_WS(py_cmp_func))
for icnt in range(cnt_wsarr):
  print ("string-elem:", wsarr[icnt]);

  
print ("done");  

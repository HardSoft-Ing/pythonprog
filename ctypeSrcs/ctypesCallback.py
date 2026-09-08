from ctypes import *

#import ctypes

# --- Load shared libc for Winodws or Linux
import sys
if sys.platform == "win32":
    # libc of Windows
    libc = cdll.msvcrt 
else:    
    # libc of Linux
    libc = CDLL('libc.so.6')

qsort = libc.qsort
# Indicate to python that qsort() returns "void", see "GNU C library" documentation. .
qsort.restype = None


# This is an explicit array-type definition for e.g. c_int: 
## 1. define array-type IntArray8
#IntArray8 = c_int * 8;
## 2. create array-instance of IntArray8 initialized by values. 
#iarr = IntArray8(5, 1, 7, 5, 5, 7, 33, 99)



# Define c_int array with 8 elements. 
iarr = (c_int * 10)(5, 1, 7, 5, 5, 7, 33, 99);
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

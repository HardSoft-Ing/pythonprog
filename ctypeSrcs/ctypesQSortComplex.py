from ctypes import *
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

# Note: since "critter" derives from ctype-class "Structure" we can create object
# arrays of type critter via expression "(critter * array-length)()"
class critter (Structure):
    _fields_ = [("name", c_wchar_p),
                ("species", c_wchar_p)
               ] 


# --- Generic way of creating a random-length critter-array ---

# - Step 1: Define random touple string array
muppetstrs = (
    ("Kermit", "frog"),
    ("Piggy", "pig"),
    ("Gonzo", "whatever"),
    ("Fozzie", "bear"),
    ("Sam", "eagle"),
    ("Robin", "frog"),
    ("Animal", "animal"),
    ("Camilla", "chicken"),
    ("Sweetums", "monster"),
    ("Dr. Strangepork", "pig"),
    ("Link Hogthrob", "pig"),
    ("Zoot", "human"),
    ("Dr. Bunsen Honeydew", "human"),
    ("Beaker", "human"),
    ("Swedish Chef", "human")
  )



# - Step 2: Create muppets[] critter-array:
#   > Create  critter-array muppets[] of size: "(critter * len(muppetstrs))"
#   > Initialize muppets[] with unpacked tuples as "(*muppetstrs)".
# Note: operator "*" on "muppetstrs" unpacks its tuples as a list of comma 
# separated tuples, see python docu "Unpacking Argument Lists".  
muppets = (critter * len(muppetstrs))(*muppetstrs)
# --- Optional discrete muppets-array creation:
# - define array-type MuppetArray_t of length "len(muppetstrs)"
MuppetArray_t = critter * len(muppetstrs)
# - create array instance from MuppetArray_t
muppets2 = MuppetArray_t(*muppetstrs)

# Just a test to see difference of python packed/unpacked lists via unpack-operator "*".
showUnpack = False;
if(showUnpack):
  print("xxx packed muppetstrs object:", muppetstrs)
  print("xxx unpacked muppetstrs touples:", *muppetstrs)


CMPFUNC_CRITTER = CFUNCTYPE(c_int, POINTER(critter), POINTER(critter))

# compare callback-function for qsort()
# Note: 
def critter_cmp_func(a, b):
    # Calculate compare result, 1: a>b, 0: a==b, -1: a<b. 
    cmpres = (a[0].name > b[0].name) - (a[0].name < b[0].name);
    #cmpres = (a[0] > b[0]) - (a[0] < b[0]);
    print("py_cmp_func, compare a/b:", a[0].name, ",", b[0].name, ":",cmpres);
    return cmpres;


qsort(muppets, len(muppets), sizeof(critter), CMPFUNC_CRITTER(critter_cmp_func))
for icnt in range(len(muppets)):
  print ("muppets-elem:", muppets[icnt].name, muppets[icnt].species);
# Do qsort for muppets2
input('Sort now optional array muppets2, press ENTER:')  
qsort(muppets2, len(muppets2), sizeof(critter), CMPFUNC_CRITTER(critter_cmp_func))
for icnt in range(len(muppets2)):
  print ("muppets2-elem:", muppets2[icnt].name, muppets2[icnt].species);
  

print("sizeof critter:", sizeof(critter));
print ("done");  

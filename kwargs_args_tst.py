#!/usr/bin/python3.4

def test_3args(arg1, arg2, arg3):
    print("value arg1:", arg1)
    print("value arg2:", arg2)
    print("value arg3:", arg3)

""" Is to be used for a random number of positional parameters,
    e.g. test_args("fasel", 5)".
"""
def test_args(*inargs):
    for inarg in inargs:
        print("inarg:", inarg);

""" Is to be used for a random number of "key = valu" pair parameters
    (non positional parameters), e.g. test_kwargs(bla = "fasel", blu = 5)".
"""
def test_kwargs(**inkwargs):
    for key,value  in inkwargs.items():
        print("inkwarg key: {0}, value: {1}".format(key, value));


""" Checks key in kwargs and prints the value if found. 
"""
def check_key_in_kwargs(key,**inkwargs):
    if key  in inkwargs:
        print(f"Found key in kwargs: {key}, value: {inkwargs[key]}")
    else:
        print(f"Key not found in kwargs: {key}")        

""" Prints the key-values of a kwwargs-dictionary, which MUST match the parameter names of the function.
    The dictionary can also be given inline as key-value pairs, e.g. fixed_kwargs_key_args(arg1=1, arg2=2, arg3=3).
    Note: Initialization with `None` allows to use kwargs-dictionaries with missing keys. And the function signature
     by this shows a dictionary is expected. 
"""
def fixed_kwargs_key_args(arg1=None, arg2=None, arg3=None):
    print(f"Predefined key-values of kwargs: arg1: {arg1}, arg2: {arg2}, arg3: {arg3}") 


""" Note: to pass args to test_3args() we must have exactly 3 arguments,
otherwise python3.5 fails. """
args = ("two", 4, 3)
print('--- Test with *args')
""" Expands args by '*' and all 3 arguments """
test_3args(*args)

# Note: to run test_3args(**kwargs) the key-names and param-count must match the parameter names
# and count of test_3args()!!!
tstkwargs = {"arg3": 3, "arg2": "two", "arg1": 5}

# Print the key-values of kwargs (3, "two", 5)
# Note: the key-names of kwargs must match the parameter names of test_3args(), otherwise
# Python fails.
print('--- Test with **kwargs')
test_3args(**tstkwargs)
# Print the key-names (arg1 - arg3) of kwargs
print('--- Test with *kwargs')
test_3args(*tstkwargs)

print('--- Test test_args()')
test_args('fruit', 'vegetable', 5)
print('--- Test test_args() with expanded *args')
test_args(*args)

print('--- Test test_kwargs()')
test_kwargs(apple = 'fruit', cabbage = 'vegetable', num = 5)
print('--- Test test_kwargs() with expanded tstkwargs')
test_kwargs(**tstkwargs)

check_key_in_kwargs("arg3", **tstkwargs)
check_key_in_kwargs("arg2", **tstkwargs)
check_key_in_kwargs("arg0", **tstkwargs)

# Key parameter order does not matter, but the key-names must match the parameter names of the function.
fixed_kwargs_key_args(arg3="arg-pos1", arg2="arg-pos2", arg1="arg-pos3")
# Key parameters can be even supplied by a dictionary which at least defines ALL key-names.
shorter_kwargs = {"arg3": 3, "arg2": "two"}
fixed_kwargs_key_args(**shorter_kwargs)
# Keys in a dict not defined in the function signature (key "arg0") will fail since they are all iterated into the function!
#to_long_kwargs = {"arg3": 3, "arg2": "two", "arg1": 5, "arg0": 0}
#fixed_kwargs_key_args(**to_long_kwargs)
arg3="arg-pos1" 
arg2="arg-pos2" 
fixed_kwargs_key_args(arg3, arg2)


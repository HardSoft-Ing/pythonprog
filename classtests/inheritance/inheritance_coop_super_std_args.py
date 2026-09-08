###
# Cooperative Multiple Inheritance with using MRO super() calls (runs Method Resolution Order)
# and *args positional parameters:
#
# Usage:
# ======
# Use this pattern for single/multi inheritance if you want to run with positional parameters
# not named parameters. 
# ----------------------------------------------------------------------------------------------
# - This pattern applies super.__init__() to call the initializers of the base classes in tree. 
#   Note: super().__init__() calls are executed for the base classes according to the MRO rules.
# - This pattern even supports base-classes with mixed arbitrary argument-lists via forwarding list-param *args.
# - This pattern requires a root-class which intercepts the __init__(...) calls to not pass them to object.__init__().
#   This is the major point here to make this pattern working!


# All classes we are deriving from shall derive from this root class!
# The class is needed to support  the super().__init__() MRO call-chain as follows:
# - Since all classes derive from RootX it becomes the last class calling __init__() in the MRO call-chain.
#   This prevents accidentally calling object.__init__() with parameters since __init__() not executes.
class RootX:
    # Must use list `*args` as argument when deriving classes which uses variable args in __init__()

    def __init__(self, *args):
        #print(f"debug-print: RootX.__init__() called with *args: {args}")
        pass

class BaseA(RootX):
    # @param msg_a: 1. Positional parameter to be printed. 
    # @param msg_b: 2. Positional parameter to be printed. 
    # @param *args: Passes potential remaining args to the next __init__() in MRO chain.
    def __init__(self, msg_a, msg_b, *args):
        print(f"BaseA: msg_a={msg_a}, msg_b={msg_b}")
        # Forward everything as list to next caller in the MRO chain.
        super().__init__(msg_a, msg_b, *args)

class BaseB(RootX):
    # @param msg: Positional parameter to be printed. 
    # @param *args: Passes potential remaining args to the next __init__() in MRO chain.
    def __init__(self, msg, *args):
        print(f"BaseB: msg={msg}")
        # Forward everything as list to next caller in the MRO chain.
        super().__init__(msg, *args)

# 1. Derives in order BaseA to B 
class Derived(BaseA, BaseB):
    def __init__(self, msg1, msg2):
        print(f"Derived: msg1={msg1}, msg2={msg2}")
        # Foward all args to the BaseX.__init__() methods in the MRO chain.
        super().__init__(msg1, msg2)

# 2. Derives in order BaseB to A to proof that super() MRO is working order independent. 
class Derived2(BaseB, BaseA):
    def __init__(self, msg1, msg2):
        print(f"\nDerived2: msg1={msg1}, msg2={msg2}")
        super().__init__(msg1, msg2)

# 3. Derive from BaseB which just requires 1 init-arg.  
class Derived3(BaseB):
    def __init__(self, msg1):
        print(f"\nDerived3: msg1={msg1}")
        super().__init__(msg1)

# 4. Just uses the BaseB.__init__() function since no override is done. 
class Derived4(BaseB):
    pass


# Testlauf für beide
d1 = Derived("Hallo Welt!", "Good Morning!")
d2 = Derived2("Hallo All!", "Good Evening!")
d3 = Derived3("Hello friends!")
d4 = Derived4("Hello simple")


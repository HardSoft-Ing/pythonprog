# Cooperative Multiple Inheritance with using MRO super() calls (runs Method Resolution Order)
# and *kwargs dictionary parameters:
#
# Usage:
# ======
# Use this pattern for single/multi inheritance if you want to run with named parameters rather 
# then positional parameters. 
# ----------------------------------------------------------------------------------------------
#
# - This pattern applies super.__init__() to call the initializers of the base classes in tree. 
#   Note: super().__init__() calls are executed for the base classes according to the MRO rules.
# - This pattern only supports base-classes using dictionary **kwargs style args.
# - This pattern requires a root-class which intercepts the __init__(...) calls to not pass them to object.__init__().
#   This is the major point here to make this pattern working!



# All classes we are deriving from shall derive from this root class!
# The class is needed to support  the super().__init__() MRO call-chain as follows:
# - Since all classes derive from it RootX becomes the class in the MRO chain.
# - The chainged super().__init__() calls will be terminated here and not reach object.__init__()
#   which does not accept arbitrary kwargs. 
# 
class RootX:
    def __init__(self, **kwargs):
        #print(f"debug-print: RootX.__init__() called with kwargs: {kwargs}")
        pass

class BaseA(RootX):
    # @param msg_a, msg_b: The key-name arguments forwarded by the super().__init__() MRO call-chain.
    # @param **kwargs: Pass the else dictionary entries beyond msg_a key to the next class in the MRO chain.
    def __init__(self, msg_a=None, msg_b=None, **kwargs):
        print(f"BaseA: {msg_a}, {msg_b}")
        # It is important for foward "msg_a= msg_a" as key-value pair since otherwise msg_a is confused
        # as positional parameter which cannot be handled by next calls __init__() which expects dictionary lists. 
        super().__init__(msg_a = msg_a, msg_b=msg_b, **kwargs)

class BaseB(RootX):
    def __init__(self, msg_b=None, **kwargs):
        print(f"BaseB: {msg_b}")
        super().__init__(msg_b=msg_b, **kwargs)

# 1. Derives in order BaseA to B 
class Derived(BaseA, BaseB):
    def __init__(self, msg1, msg2):
        print(f"Derived: {msg1}, {msg2}")
        # Runs MRO chainged initialization for all BaseX.__init__() methods.
        # The key-names  mgs_a, msg_b direct the values to the BaseX.__init__() where those key-names are expected.
        super().__init__(msg_a=msg1, msg_b=msg2)

# 2. Derives in order BaseB to A to proof that super() MRO is working order independent. 
class Derived2(BaseB, BaseA):
    def __init__(self, msg1, msg2):
        print(f"\nDerived2: {msg1}, {msg2}")
        super().__init__(msg_b=msg1, msg_a=msg2)


# 2. Derives in order BaseB to A to proof that super() MRO is working order independent. 
class Derived3(BaseB):
    def __init__(self, msg1):
        print(f"\nDerived2: {msg1}")
        super().__init__(msg_b=msg1)


d1 = Derived("Hallo Welt!", "Good Morning!")
d2 = Derived2("Hallo All!", "Good Evening!")
d3 = Derived3("Hello friends!")


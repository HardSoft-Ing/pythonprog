# Multiple inheritance example simply using C++ style class__init__() calls to base class initializers.
# Simplest approach (but not generic) for handling multiple inheritance with override of __init__().


class BaseA(object):
    def __init__(self, msg=None):
        print("call BaseA.__init__(), msg:", msg)

class BaseB(object):
    def __init__(self, msg=None):
        print("call BaseB.__init__(), msg:", msg)

class BaseC(object):
    def __init__(self, msg=None):
        print("call BaseC.__init__(), msg:", msg)



class Derive(BaseA, BaseB, BaseC):
    def __init__(self, msg):
        print("call AB_Inherit.__init__(), msg:", msg)

        # Calls  BaseA.__init__() which is the first __init__() in the MRO.
        BaseA.__init__(self, msg)
        # Calls BaseC.__init__() which is the next __init__() in the MRO following BaseB.
        BaseC.__init__(self, msg)
        # Calls BaseB.__init__() which is the next __init__() in the MRO following BaseA.
        BaseB.__init__(self, msg)


class Derive2(BaseC, BaseB, BaseA):
    def __init__(self, msg):
        print("call BA_Inherit.__init__(), msg:", msg)
        BaseC.__init__(self, msg)
        BaseB.__init__(self, msg)
        BaseA.__init__(self, msg)

    def prn1(self, msg):
        print("prn1-msg:", msg)

    def prn2(self, msg):
        print("prn2-msg:", msg)

class Derive3(BaseB):
    def __init__(self, msg):
        print("call BA_Inherit.__init__(), msg:", msg)
        BaseB.__init__(self, msg)

    def prn1(self, msg):
        print("prn1-msg:", msg)

    def prn2(self, msg):
        print("prn2-msg:", msg)



print("xxx Start")
abc_inherit = Derive("# Message from parent abc_inherit")
cba_inherit = Derive2("# Message from parent cba_inherit")
b_inherit = Derive3("# Message from parent b_inherit")
print("xxx Done")



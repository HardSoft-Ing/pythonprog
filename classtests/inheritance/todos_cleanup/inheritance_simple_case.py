import sys


class BaseA():
    # Called if not overriden by derived class.
    def __init__ (self, init_msg=None):
        self.init_msg = init_msg
        print (f"{BaseA.__name__} init_msg: {self.init_msg}")
    # Empty function! Can be used when deriving abstract classes to define
    # interfaces. 
    # Note: No warnings or errors occur when instantiating abstract classes!!! 
    # This is a kind of dangerous. 
    def fooIfSave(self,msg=None):
        raise NotImplementedError(self.fooIfSave.__name__+ "() is not implemented in derived class.")

    def fooIfDogy(self, msg=None):
        # Using pass for interface function is doggy since it can be called without any warnings or errors.
        pass


class DeriveNoInit(BaseA):
    def fooIfSave(self, msg=None):
        print (f"Call {self.fooIfSave.__name__} ({self.init_msg}), msg: {msg}")
    

drv = DeriveNoInit("Object-DeriveNoInit")
bs = BaseA("Base message")


drv.fooIfSave("Hello from derived class")

bs.fooIfSave   ()
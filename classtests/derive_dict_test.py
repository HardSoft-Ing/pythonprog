
class MyDict(dict):
    """My dictionary which derives from "dict"
    
    The class extending the default dict behave like a dict 
    object but can extend it by new member properties. 
    """
           
    def printme(self, str):
        print(self.__str__() + ", xxx msg: " + str)

        
        
mydict = MyDict()

mydict["bla"] = 1
mydict["fasel"] = 2
mydict.printme("test")
# Prints the class documentation embedded in  """ """
print(mydict.__doc__) 
print(repr(mydict.__doc__))






          
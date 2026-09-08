# Property test
# Here we define for class P a getter/setter property "x" via function property()
class P:
    def __init__(self,x):
        self.__x = x

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

 
    x = property(getX, setX)

pObj = P(10);
print(pObj.x);
pObj.x = 55;
print(pObj.x);

# Strange class for property and class definitions:
#
# Note: 
# - the instance "self" this-pointer can actually be named randomly for 
#   any instance method but must be the first argument of an instance method.
#   Since python natively don't supports static methods arg1 always is "this".
#   But always use "self" for the this-arg!!! Also note that many python editors 
#   indicate naming the this-arg other then "self" as error. 
# - property setter-, getter-function can be named randomly but must
#   passed to property() in the defined order for getter, setter, ... etc.
# - class members prefixed with "__" are private and can't be accessed by objects. 
class P_strange:
    # We can name the `self` this-pointer randomly (e.g. `myselfA`), but it must be the first argument of an instance method.
    def __init__(myselfA,x):
        myselfA.__myx = x
    # Name the `self` this-pointer name can be freely defined per class method.
    def blaGet(myselfB):
        return myselfB.__myx

    def blubSet(myselfC, x):
        myselfC.__myx = x
    
    x = property(blaGet, blubSet)

pSObj = P_strange(10);
print(pSObj.x);
# Don't works since __myx is private!
#print(pSObj.__myx);

pSObj.x = 55;
print(pSObj.x);



class Bottles(object):
  def __init__(self, number):
# ctypes requires a member named _as_parameter_ to convert any object into a number or string.
    self._as_parameter_ = number;
    print('Bottels ctor with number:', number);
           

# Derive class from Bottels
class MilkBottle(Bottles):
    # Note, this class inherits __init__() if we don't override it
    def showParam(self):
        print('Value of _as_parameter_:', self._as_parameter_);

    _fields_ = [("x", c_int),
                ("y", c_int),
                ("z", c_int)
               ];
  

bottles = Bottles(42)
milkBottle = MilkBottle(55);


for fieldVal in MilkBottle._fields_:
  # exec executes any dynamic python-code expression (it can alter code/data in memory) but doesn't return a result.
  # With fieldVal[0] is 'x' we get expression: x = fieldVal[1](3) => x = c_int(3), thus a variable x is defined!
  exec(fieldVal[0] + '= fieldVal[1](3)');
  # eval only returns the result of a dynamic expression but can't alter code or data, thus no "=" operator is accepted.
  # The literals of fieldVal[0] e.g. 'x' are defined via exec as real existing variables e.g. x. 
  # Thus with 'x' expression print(x) or print(eval('x')) print same defined variable x!    
  a = eval(fieldVal[0]);
  print("eval var",fieldVal[0],": ",a)

  
  

milkBottle.showParam();


class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("z", c_int)
                ]

point = POINT(10, 20, 30)
print ("Points:", point.x, point.y, point.z)

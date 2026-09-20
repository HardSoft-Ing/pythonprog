# Define getter/setter class-property via discrete 'class property' assignment
class PropByCls:
    def __init__(self,in_x):
        self._x = in_x
    def get_x(self):
        print(f"Getter x-property")
        return self._x
    def set_x(self, in_x):
        print(f"Setter x-property = {in_x}")
        self._x = in_x
    x = property(get_x, set_x)

# Define getter/setter class-property via recommend decorated-syntax for 'class property'
# Advantage with decorator: Only a property-name is required but no getter/setter function names.
class PropByDecor:
    def __init__(self,in_x):
        self._x = in_x
    # Use class property by decorator syntax        
    @property
    def x(self):
        print(f"Getter x-property")
        return self._x
    @x.setter
    def x(self, in_x):
        print(f"Setter x-property = {in_x}")
        self._x = in_x


propcls = PropByCls(10);
print(propcls.x);
propcls.x = 55;
print(propcls.x);

propdec = PropByDecor(11);
print(propdec.x);
propcls.x = 56;
print(propdec.x);


# Simulates decorator code-expansion of example `PropByDecor` without decorator-op '@'.
# Note: Just a deep-dive of how the '@property' stuff actually works.
class PropByDecorSim:
    def __init__(self,in_x):
        self._x = in_x
    # Getter 'x()'    
    def x(self):
        print(f"Getter x-property")
        return self._x
    # Get a property instance
    tmp_x = property(x)
   # Setter 'x()'
   # Note: Python overwrites now Getter 'x()' with Setter 'x()'! But this won't harm since Getter 'x()' 
   # is ALREADY captured by object tmp_x! This trick allows to use same func-name 2 times!
    def x(self, in_x):
        print(f"Setter x-property = {in_x}")
        self._x = in_x
    # property.setter() returns a new property() with the added Setter 'x()'.    
    x = tmp_x.setter(x)

propsim = PropByDecorSim(10);
print(propsim.x);
propsim.x = 55;
print(propsim.x);







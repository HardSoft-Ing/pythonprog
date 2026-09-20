class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


temp = Celsius(10);

print ("temp.get_temperature():", temp.get_temperature() );
print ("temp._temperature:", temp._temperature );
print ("temp._temperature by __dict__:", temp.__dict__['_temperature'] );



class Math(object):  
    def __init__(self):
        self._pi = 3.14

    @property
    def pi(self):
        print("In")
        return self._pi

    @pi.setter
    def pi(self, value):
        """ Do nothing when 'pi' is being assigned a new value """
        pass
        
        
        
a = Math();
print("a.pi", a.pi)
# No change on a.pi possible 
a.pi = 0
print("a.pi", a.pi)

          
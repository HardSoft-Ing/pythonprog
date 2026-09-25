from ctypes import *
import ctypes

# --- Define 'ctypes Structure' derived class with "native C" compatible int-fields. 

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int),
                ("z", c_int)
                ]

print("POINT.x:", POINT.x); print("POINT.y:", POINT.y)
point = POINT(10, 20, 30)
print ("Points:", point.x, point.y, point.z)


# --- Define 'ctypes Structure' derived class with "native C" compatible bit- and int-fields. 

class BitFlds(Structure):
    # 
    _fields_ = [
        # Define 3 bits at offset=0
        ("first_2", c_int, 3),
        # Define 8 bits at offset=3
        ("second_8", c_int, 8),
        # Define 16 bits at offset=3+8
        ("third_16", c_int, 16)                 
        ]
# Print bit-field types-info
print(BitFlds.first_2); print(BitFlds.second_8); print(BitFlds.third_16)

# The value-range of bit-field items is limited by their bit-size!
bitFldsMax = BitFlds(0x2, 0x7f, 0x7fff)
bitFldsNeg1 = BitFlds(0x7, 0xff, 0xffff)
bitFldsOvrLim = BitFlds(0x8, 0x100, 0x10000)

# Iterating over instance bit-fields only returns the fields type-info but not the 
# field value! The values are the generated attributes of the _fields_ owning instances!
for fld in bitFldsMax._fields_:
    print(f"fld: {fld}")

# Print bit-field values from instance
print(bitFldsMax.first_2); print(bitFldsMax.second_8); print(bitFldsMax.third_16)
print(bitFldsNeg1.first_2); print(bitFldsNeg1.second_8); print(bitFldsNeg1.third_16)
print(bitFldsOvrLim.first_2); print(bitFldsOvrLim.second_8); print(bitFldsOvrLim.third_16)








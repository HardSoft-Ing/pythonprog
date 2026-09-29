###
# Experimenting with simple function as 'yield' generator. 
#

# Simple add function turned into a generator once 'yield' as inserted!
# The count of 'yield' instructions is irrelevant. 
def addval(num: int) -> int:
    count_e = 0
    # Executed once but ignored for the next calls until yield-for-loop is done. 
    print (f"### - Enter {addval.__name__}()")
    yield 10 + num

    print (f"### - Run 2. yield {addval.__name__}()")
    yield 20 + num

    print (f"### - Exit {addval.__name__}()")
    return 10

# Get function generator-object initialized by 5.
genobj = addval(5)
print (f"# Got generator: {genobj}")            

# Run with 1. yield
value = next(genobj)
print (f"# Got value: {value}")            
# Run with 2. yield
value = next(genobj)
print (f"# Got value: {value}")            

try:
    # Raises exception since no yield instructions is left for next().
    value = next(genobj)
    assert(False) # Not to be reached!
    print (f"# Got value: {value}")            
except StopIteration as exec:
    print (f"# Function really returned, we got return-value: {exec.value}")            


# yield via for-in loop: it implicit gets and iterates the generator-object
# but CAN'T access the addval() return value!
for value in addval(5):
    print (f"# Got 'for-in' value: {value}")            

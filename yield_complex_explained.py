# Python3 code to demonstrate yield keyword 

# Use of yield inside a function turns the function into a generator.
# Inovking the 
# returns a generator object for each `yield` call. 
def printresult(String) : 
    count_e = 0
    # Executed once but ignored for the next calls until yield-for-loop is done. 
    print (f"### - Entering {printresult.__name__}() before for-in-yield loop")
    for i in String: 
        if i == "e": 
            
            print(f"### Before yield, count_e = {count_e}")
            # Pauses "for-in" loop by immediately returning to function-caller with value of 'i'.
            yield i 
            count_e += 1
            # Continues paused yield-context of "for-in" loop
            print(f"### Continue yield, count_e = {count_e}")
    # Executed once when yield-loop is done for the next call.             
    print (f"### - Returning from {printresult.__name__}()")     
    
    # The caller m
    # Due to this an implicit <generator object printresult xxxx> is returned only which 
    # then can be used via loop-iterations to get out the yield-values.
    return 'a'

# initializing string 
ans = 0
print ("# Run yield test #\n") 
String = "GeeksforGeeks" 
String = String.strip() 

# --- Call printresult() in for-loop which does:
#     - return the COMPLETE function body of printresult() as temporary generator-object.
#     - a for-in iteration over the returned generator-object only.
print (f"\n--- Example 1: 'for j in printresult()' ---\n")            
for j in printresult(String): 
    ans = ans + 1
    print(f"Current 'for-in' ans = {ans}, yield-result = {j}")
print (f"# - Final 'for-in'  ans value = {ans}")            


# --- Call printresult() via separated 'while-True / next()' loop which does:
#     - return the COMPLETE function body of printresult() as generator-object 'generatorobj'.
#     - run a 'next()' iteration-loop over 'generatorobj' which is the first time where the printresult() body is executed!

# Note: printresult() is NOT executed but instead the call returns its function-body wrapped in a generator-object.
#       (see also printresult() log-traces to assure the order of function-code execution). 

generatorobj = printresult(String)
print (f"\n--- Example 2: 'while next() on printresult() generator-object' = {generatorobj}\n")            

ans = 0
try:
    while True:
        # - 1'st next() is first time we enter function printresult().
        # - Subsequent next() calls enter and return from yield-context until yield is called. 
        # - Last next() (when internal yield execution is skipped) raises 'StopIteration exception'.
        value = next(generatorobj)
        ans = ans + 1
        print(f"Current 'next' ans = {ans}, yield-result = {j}")
# Catch type StopIteration: it always provides a function's return-value.
except StopIteration as exec:        
     print(f"# StopIteration.value contains printresult() return-value = {exec.value}")  # a

print (f"# - Final 'next'  ans value = {ans}")            



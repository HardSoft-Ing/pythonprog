# The following explains the python fundamentals used for the decorator implementation. 
# Check this out before progressing to the real decorator examples. 
# From: 
# https://www.datacamp.com/tutorial/decorators-python?utm_cid=23781701478&utm_aid=196565213035&utm_campaign=260417_1-ps-dscia%7Eamx-tofu%7Epython_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9042535-&utm_mtd=p-m&utm_kw=decorators+python&utm_source=google&utm_medium=paid_search&utm_content=ps-dscia%7Eemea-en%7Eamx%7Etofu%7Etutorial%7Epython&gad_source=1&gad_campaignid=23781701478&gbraid=0AAAAADQ9WsGmJYqXHvDxoBXmTLuK27FQx&gclid=Cj0KCQjw-frTBhCvARIsADv4XY7Fkg-KLHBg5qvLylE-Nn10jYaStxCvTvmCZ0xv11LSXElLAbas_5QaAl2WEALw_wcB&dc_referrer=https%3A%2F%2Fwww.google.com%2F


# - Defining functions inside other functions 
def plus_one(number):
    def add_one(number):
        return number + 1
    result = add_one(number)
    return result

print(plus_one(4))


# - Passing functions as arguments to other functions
def plus_one(number):
    return number + 1
def plus_two(number):
    return number + 2

def function_call(function):
    number_to_add = 4
    return function(number_to_add)

print(function_call(plus_one))
print(function_call(plus_two))


# - Functions returning other functions
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(hello())
# Do function as object assignment with immediate dereferencing via "()()"
pfunc_hello=hello_function
print("pfunc_hello()(): " + pfunc_hello()())


# - Inner Functions and Closures
def outer_function(message):
    def inner_function():
        # Note: The variable context of outer_function() (param. message) is accessible to
        # closure inner_function() and returned with it when invoked. 
        print(f"Message from closure: {message}")
    return inner_function
closure_function = outer_function("Hello, closures!")
# Closer function stores input-string in its return-context. 
closure_function()


# - Using a decorator pattern
def simple_decorator(func):
    def wrapper():
        print("- Before the function call")
        func()
        print("- After the function call")
    return wrapper

# Use decorator syntax
@simple_decorator
def greet():
    print("# Hello!")

greet()
# None decorator syntax with same result. 
def greetnew():
    print("# New Hello!")
# Reusing func-name greetnew() (just to be close the decorator syntax) overrides the first definition 
# of greetnew(): It seems the is done by the decorator pattern @xxxfunc().
greetnew=simple_decorator(greetnew)
greetnew()



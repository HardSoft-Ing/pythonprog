# Examples of various @decorator based impls.
# You may check out the decorator basics if not already done. 
# From: 
# https://www.datacamp.com/tutorial/decorators-python?utm_cid=23781701478&utm_aid=196565213035&utm_campaign=260417_1-ps-dscia%7Eamx-tofu%7Epython_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9042535-&utm_mtd=p-m&utm_kw=decorators+python&utm_source=google&utm_medium=paid_search&utm_content=ps-dscia%7Eemea-en%7Eamx%7Etofu%7Etutorial%7Epython&gad_source=1&gad_campaignid=23781701478&gbraid=0AAAAADQ9WsGmJYqXHvDxoBXmTLuK27FQx&gclid=Cj0KCQjw-frTBhCvARIsADv4XY7Fkg-KLHBg5qvLylE-Nn10jYaStxCvTvmCZ0xv11LSXElLAbas_5QaAl2WEALw_wcB&dc_referrer=https%3A%2F%2Fwww.google.com%2F


# - Creating Your First Decorator


def uppercase_decorator(function):
    def wrapper(msg):
        func = function(msg)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi(msg):
    return "Hi: " + msg
# Override say_hi() with new decorated say_hi().
say_hi = uppercase_decorator(say_hi)

print(say_hi("Frank"))


# - Using the @ syntax
@uppercase_decorator
def say_hi_new(msg):
    return "Hi: " + msg

print(say_hi_new("Peter"))


# - Stacking Multiple Decorators
import functools
def split_string(function):
    # The @functools.wraps(function) tag preserves the original metadata of 'function' e.g. the function-name etc.
    # Example when param function == say_hi_split:
    # - Using @functools.wraps(function):
    #   print(say_hi_split.__name__) == "say_hi_split"
    # - Without @functools.wraps(function) the returned wrapper() overrides metadata of say_hi_split:
    #   print(say_hi_split.__name__) == "wrapper"
    @functools.wraps(function)
    def wrapper(msg):
        func = function(msg)
        splitted_string = func.split()
        return splitted_string
    return wrapper 

@split_string
@uppercase_decorator
def say_hi_split(msg):
    return "Hi: " + msg

print(say_hi_split("Rudi"))


# - General-Purpose Decorators with *args and **kwargs
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_args():
    print("No arguments here.")
function_with_no_args()    
# It is allowed to input keyword arguments but not positional ones!
function_with_no_args(first_name="Bette", last_name="Davis")
# This would fails as positional args are not supported if not defined in signature!
#function_with_no_args("Bette", "Davis")


@a_decorator_passing_arbitrary_arguments
def function_with_args(val1, val2):
    print(f"Parameters val1: {val1}, val2: {val2}")

function_with_args("Level", 42)


# - Passing Arguments to Decorators
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")

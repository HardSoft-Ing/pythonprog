###
# The following explains by examples with simple to deep nested decorator func.-hierarchies 
# how the operator "@" of a decorator-expression "@decorator_func" works. 
# Note, that 
# - @decorator_func 
#   def somefunc(): 
#       ...code-body...  
# is ALWAYS expanded to the ivokation.
# - somefunc= decorator_func(somefunc)'
#
# In case of decorator_func(somearg) expects not arg. 'somefunc()' but has nested wrappers where at least one
# of them must accept 'somefunc()' we need to add "(...)" per nested function until we reach the nested 
# function expecting 'somefunc' as argument. 
# - @decorator_func(...)-(...)
#


g_pandas = "Pandas"

# ------------------------------------------------------------------------
print("\n# --- Simple decorator ---\n") 
# ------------------------------------------------------------------------
def decor_func_return(func):
    # The decorating function which adds functionality to func()
    def dec_wrapper(function_arg1, function_arg2):
        print(f"In func {dec_wrapper.__name__}()\n" 
            f"Calls func {func.__name__}() with args: {function_arg1}, {function_arg2}"
            )
        # Wrapped function
        return func(function_arg1, function_arg2)
    print(f"In func {decor_func_return.__name__}(), returning func {func.__name__}()")
    return dec_wrapper


# ---
print("# - Use decorator-syntax") 
# ---

# The "@" syntax WITHOUT "()" invokes decor_func_return(func) -> return dec_wrapper(...)
@decor_func_return
def decfunc_4decor_simple(function_arg1, function_arg2):
    print(f"This is the decorated function and it only knows about its arguments: {function_arg1}, {function_arg2}")
decfunc_4decor_simple("Hello", "World")

# ---
print("# - Use expanded inline-code") 
# ---
def stdfunc_4decor_simple(function_arg1, function_arg2):
    print(f"This is the decorated function and it only knows about its arguments: {function_arg1}, {function_arg2}")
stdfunc_4decor_simple = decor_func_return(stdfunc_4decor_simple)    
stdfunc_4decor_simple("Hello", "World")


# ------------------------------------------------------------------------
print("\n# --- Complex 2-level-nested decorator with Arguments\n") 
# ------------------------------------------------------------------------

def decor_factory_2nested_3args(decorator_arg1, decorator_arg2, decorator_arg3):
    def decor_func_return(func):
        def dec_wrapper(function_arg1, function_arg2, function_arg3) :
            print(f"In func {dec_wrapper.__name__}() with args: {decorator_arg1}, {decorator_arg2}, {decorator_arg3}\n" 
                f"Calls func {func.__name__}() with args: {function_arg1}, {function_arg2}, {function_arg3}"
                )
            return func(function_arg1, function_arg2,function_arg3)

        print(f"In func {decor_func_return.__name__}(), returning func {func.__name__}()")
        return dec_wrapper

    print(f"In func {decor_factory_2nested_3args.__name__}(), returning func {decor_func_return.__name__}()")
    return decor_func_return

# ---
print("# - Call complex decorator with decorator-syntax") 
# ---

# Extra operator "(...)" in "@" syntax invokes decor_factory_3args_2wraps(...) -> return decor_func_return(func):
@decor_factory_2nested_3args(g_pandas, "Numpy","Scikit-learn")
def decorated_with_arguments_lvl2(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl2(g_pandas, "Science", "Tools")


# ---
print("# - Call complex decorator without decorator-syntax") 
# ---

def decorated_with_arguments_lvl2_nodec(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

tmp_decorated_with_arguments_lvl2_nodec = decor_factory_2nested_3args(
    g_pandas, "Numpy", "Scikit-learn")

decorated_with_arguments_lvl2_nodec = tmp_decorated_with_arguments_lvl2_nodec(decorated_with_arguments_lvl2_nodec)

decorated_with_arguments_lvl2_nodec(g_pandas, "Science", "Tools")


# ---
print("# - Call complex decorator without decorator-syntax and NO temp-function") 
# ---
#   Note: We use a chained callable expression like "somefunc()()()" where the "()" operators MUST
#   follow the function-name in same line. A line-break can only occur within the argument-list, see below example.

def decorated_with_arguments_lvl2_notmp(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl2_notmp = decor_factory_2nested_3args(
    g_pandas, "Numpy", "Scikit-learn")(decorated_with_arguments_lvl2_notmp)

decorated_with_arguments_lvl2_notmp(g_pandas, "Science", "Tools")


# ------------------------------------------------------------------------
print("\n# --- Complex 3-level-nested decorator without nested Arguments\n") 
# ------------------------------------------------------------------------


def decor_factory_3nested_3args(decorator_arg1, decorator_arg2, decorator_arg3):
    def wrapper_deco_func_return():        
        def decor_func_return(func):
            def dec_wrapper(function_arg1, function_arg2, function_arg3) :
                print(f"In func {dec_wrapper.__name__}() with args: {decorator_arg1}, {decorator_arg2}, {decorator_arg3}\n" 
                    f"Calls func {func.__name__}() with args: {function_arg1}, {function_arg2}, {function_arg3}"
                    )
                return func(function_arg1, function_arg2,function_arg3)

            print(f"In func {decor_func_return.__name__}(), returning func {func.__name__}()")
            return dec_wrapper

        print(f"In func {wrapper_deco_func_return.__name__}(), returning func {decor_func_return.__name__}()")
        return decor_func_return
    
    print(f"In func {decor_factory_3nested_3args.__name__}(), returning func {wrapper_deco_func_return.__name__}()")
    return wrapper_deco_func_return


# ---
print("# - Call complex decorator with decorator-syntax") 
# ---

# We must call 2'st level wrapper_decorator() with empty arguments "(...)()".
@decor_factory_3nested_3args(g_pandas, "Numpy", "Scikit-learn")()
def decorated_with_arguments_lvl3(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl3(g_pandas, "Science", "Tools")


# ---
print("# - Call complex decorator without decorator-syntax") 
# ---

def decorated_with_arguments_lvl3_nodec(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

tmp_decorated_function_with_arguments = decor_factory_3nested_3args(
    g_pandas, "Numpy", "Scikit-learn"
)
tmp_decorated_function_with_arguments = tmp_decorated_function_with_arguments()
decorated_with_arguments_lvl3_nodec =  tmp_decorated_function_with_arguments(decorated_with_arguments_lvl3_nodec)

decorated_with_arguments_lvl3_nodec(g_pandas, "Science", "Tools")

# ---
print("# - Call complex decorator without decorator-syntax and NO temp-function") 
# ---
#   Note: We use a chained callable expression like "somefunc()()()" where the "()" operators MUST
#   follow the function-name in same line. A line-break can only occur within the argument-list, see below example.

def decorated_with_arguments_lvl3_notmp(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl3_notmp = decor_factory_3nested_3args(g_pandas, "Numpy", 
                                    "Scikit-learn")()(decorated_with_arguments_lvl3_notmp)

decorated_with_arguments_lvl3_notmp(g_pandas, "Science", "Tools")



# ------------------------------------------------------------------------
print("\n# --- Complex 3-level-nested decorator with nested Arguments\n") 
# ------------------------------------------------------------------------


def decorator_lvl3_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def wrapper_decorator(wrapper_arg1, wrapper_arg2):        
        def decorator(func):
            def wrapper(function_arg1, function_arg2, function_arg3) :
                print(f"In func {wrapper.__name__}() with args: {decorator_arg1}, {decorator_arg2}, {decorator_arg3}\n" 
                    f"Calls func {func.__name__}() with args: {function_arg1}, {function_arg2}, {function_arg3}"
                    )
                return func(function_arg1, function_arg2,function_arg3)

            print(f"In func {decorator.__name__}(), returning func {func.__name__}()")
            return wrapper

        print(f"In func {wrapper_decorator.__name__}({wrapper_arg1}, {wrapper_arg2}), returning func {decorator.__name__}()")
        return decorator
    
    print(f"In func {decorator_lvl3_maker_with_arguments.__name__}(), returning func {wrapper_decorator.__name__}()")
    return wrapper_decorator


# ---
print("# - Call complex decorator with decorator-syntax") 
# ---

# Requires calling with "(...)("Hello", "Frank")" to pass arguments to 2'nd level wrapper_decorator()!
@decorator_lvl3_maker_with_arguments(g_pandas, "Numpy","Scikit-learn")("Hello", "Frank")
def decorated_with_arguments_lvl3(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl3(g_pandas, "Science", "Tools")


# ---
print("# - Call complex decorator without decorator-syntax") 
# ---

def decorated_with_arguments_lvl3_nodec(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

tmp_decorated_function_with_arguments = decorator_lvl3_maker_with_arguments(
    g_pandas, "Numpy", "Scikit-learn"
)
tmp_decorated_function_with_arguments = tmp_decorated_function_with_arguments("Hello", "Frank")
decorated_with_arguments_lvl3_nodec =  tmp_decorated_function_with_arguments(decorated_with_arguments_lvl3_nodec)

decorated_with_arguments_lvl3_nodec(g_pandas, "Science", "Tools")

# ---
print("# - Call complex decorator without decorator-syntax and NO temp-function") 
# ---
#   Note: We use a chained callable expression like "somefunc()()()" where the "()" operators MUST
#   follow the function-name in same line. A line-break can only occur within the argument-list, see below example.

def decorated_with_arguments_lvl3_notmp(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl3_notmp = decorator_lvl3_maker_with_arguments (g_pandas, "Numpy", 
                                    "Scikit-learn")("Hello", "Frank")(decorated_with_arguments_lvl3_notmp)

decorated_with_arguments_lvl3_notmp(g_pandas, "Science", "Tools")

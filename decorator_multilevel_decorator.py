###
# Demonstrates multi-level-nested decorator calls:
# - Using the "@" decorator-syntax.
# - Using NO "@" decorator-syntax and temp-helper-functions
# - Using NO "@" decorator-syntax, NO temp-helper functions but with callable chaining like "()()...()"


g_pandas = "Pandas"


# ------------------------------------------------------------------------
print("\n# --- Complex 2-level-nested decorator with Arguments\n") 


def decorator_lvl2_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            print(f"In func {wrapper.__name__}() with args: {decorator_arg1}, {decorator_arg2}, {decorator_arg3}\n" 
                f"Calls func {func.__name__}() with args: {function_arg1}, {function_arg2}, {function_arg3}"
                )
            return func(function_arg1, function_arg2,function_arg3)

        print(f"In func {decorator.__name__}(), returning func {func.__name__}()")
        return wrapper

    print(f"In func {decorator_lvl2_maker_with_arguments.__name__}(), returning func {decorator.__name__}()")
    return decorator

# ---
print("# - Call complex decorator with decorator-syntax") 

@decorator_lvl2_maker_with_arguments(g_pandas, "Numpy","Scikit-learn")
def decorated_with_arguments_lvl2(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl2(g_pandas, "Science", "Tools")


# ---
print("# - Call complex decorator without decorator-syntax") 

def decorated_with_arguments_lvl2_nodec(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

tmp_decorated_with_arguments_lvl2_nodec = decorator_lvl2_maker_with_arguments(
    g_pandas, "Numpy", "Scikit-learn")

decorated_with_arguments_lvl2_nodec = tmp_decorated_with_arguments_lvl2_nodec(decorated_with_arguments_lvl2_nodec)

decorated_with_arguments_lvl2_nodec(g_pandas, "Science", "Tools")


# ---
print("# - Call complex decorator without decorator-syntax and NO temp-function") 
#   Note: We use a chained callable expression like "somefunc()()()" where the "()" operators MUST
#   follow the function-name in same line. A line-break can only occur within the argument-list, see below example.

def decorated_with_arguments_lvl2_notmp(function_arg1, function_arg2, function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl2_notmp = decorator_lvl2_maker_with_arguments(
    g_pandas, "Numpy", "Scikit-learn")(decorated_with_arguments_lvl2_notmp)

decorated_with_arguments_lvl2_notmp(g_pandas, "Science", "Tools")



# ------------------------------------------------------------------------
print("\n# --- Complex 3-level-nested decorator with Arguments\n") 


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

# Requires calling with "(...)("Hello", "Frank")" to pass arguments to 2'nd level wrapper_decorator()!
@decorator_lvl3_maker_with_arguments(g_pandas, "Numpy","Scikit-learn")("Hello", "Frank")
def decorated_with_arguments_lvl3(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl3(g_pandas, "Science", "Tools")


# ---
print("# - Call complex decorator without decorator-syntax") 

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
#   Note: We use a chained callable expression like "somefunc()()()" where the "()" operators MUST
#   follow the function-name in same line. A line-break can only occur within the argument-list, see below example.

def decorated_with_arguments_lvl3_notmp(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_with_arguments_lvl3_notmp = decorator_lvl3_maker_with_arguments (g_pandas, "Numpy", 
                                    "Scikit-learn")("Hello", "Frank")(decorated_with_arguments_lvl3_notmp)

decorated_with_arguments_lvl3_notmp(g_pandas, "Science", "Tools")

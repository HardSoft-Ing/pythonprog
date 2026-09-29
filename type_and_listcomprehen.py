type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    """
    Multiplies the each vector-element by given scalar.
    Args:
        scalar: Multiplication factor for the vector elements
        vector: Vector which elements gets scaled up by scalar.
    Returns:
        Scaled up vector.     
    """
    # Run for-in as 'list comprehension'
    return [scalar * num for num in vector]


def makesquares(num_start: int, num_end: int) -> Vector:
    """
    Returns squared numbers by the range from num_start until num_end (is included).
    Args:
        num_start: First number to be squared.
        num_end: Last number to be squared
    Returns:
        Vector with range of squared numbers. 
    """
    return [num**2 for num in range(num_start, num_end + 1)]


# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(f" new_vector: {new_vector}, size: {len(new_vector)}")

squares = makesquares(2, 8)
print(squares)

# Notes on range():

val_range = range(1, 10)
# Due to range() "lazy evaluation" the range-object was returned and is just printed.
print(f"Prints the val_range object: {val_range}") # 
# The 'lazy evaluation' for range() and others is a python concept to save memory. 
# Use an for-iteration or list() function to dynamically expand range-objects.
print(f"Prints the val_range list: {[val for val in val_range]}") 
# Same as above but quicker: List expansion via list(). 
print(f"Prints the val_range list: {list(val_range)}") 
# Experimental: The for-interator in a tuple '()' not expands to a list.
print(f"Prints the val_range function generator: {(val for val in val_range)}") 

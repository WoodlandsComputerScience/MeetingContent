def cool_function(x):
    """This function outputs the input plus 99, times 2, divided by the cube root of x."""
    return (2*(x + 99))/(x**1/3)


print(cool_function(int(input())))
print(cool_function.__doc__)
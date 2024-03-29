import re
def double(x):
    return x*2
def apply(f):
    return(f(1))

my_double=double
x=apply(my_double)
print(x)
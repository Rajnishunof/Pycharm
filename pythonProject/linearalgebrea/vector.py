import math
def add(v1,v2):
    return [i+j for i,j in zip(v1,v2)]

def sub(v1,v2):
    return [i-j for i,j in zip(v1,v2)]

def dot(v1,v2):
    return sum([i*j for i,j in zip(v1,v2)])

def sumsquare(v1,v2):
    return sum([(i+j)*(i+j) for i,j in zip(v1,v2)])
def mag(v1):
    return math.sqrt(sumsquare(v1,v1))

v1=[1,2,3,4]
v2=[11,12,13,14]
print(add(v1,v2))
print(sub(v1,v2))
print(dot(v1,v2))
print(sumsquare(v1,v2))
print(mag(v1))
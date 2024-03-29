def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def fibonacci(n):

    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
c=0
s=0
def reverse(n):
    global c
    k=n
    while(n>0):
        c+=1
        n=n//10


    return op(k)
def op(n):
    global s
    global c
    if c==0:
        return s
    p=n%10
    s=s*10+p
    c-=1
    return op(n//10)

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def printfibo(a,b,n):
    if n==0:
        return n
    else:
        print(a,end=" ")
        return printfibo(b,a+b,n-1)




# print(factorial(5))
# print(fibonacci(6))
# print(reverse(12345))
# print(gcd(41567887,3256789))
printfibo(0,1,2)
# lst = [1, 2, 3, 1, 2]
# print(lst.count(1))
# print(lst.count(2))
# print(lst.count(3))
# lst.pop(1)
# print(lst)
def sum1(a,b):
    return a+b

def sum2():
    a=int(input("Enter a no\n"))
    b=int(input("Enter a no\n"))
    return a+b

def sum3(a,b):
    print(a+b)

def sum4():
    a=int(input("Enter a no\n"))
    b=int(input("Enter a no\n"))
    print(a+b)

def cal():
    print("Enter 1 for with argument with return\nEnter 2 for without argument with return\nEnter 3 for with argument without return\nEnter 4 for without argument without return\n")
    n=int(input("Enter your choice"))
    functions:dict={1:sum1,2:sum2,3:sum3,4:sum4}
    print(dict[n])
#
# print("with argument with return\n")
# print(sum1(2,4))
#
# print("without argument with return\n")
# print(sum2())
#
# print("with argument without return\n")
# sum3(2,4)
#
# print("without argument without return\n")
# sum4()

print("Using menu driven")
cal()


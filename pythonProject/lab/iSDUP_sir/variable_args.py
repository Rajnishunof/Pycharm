def f(*args):
    print(*args)
    print(args)
    print(type(args))
    print(args[2])

f(10,20,30,40)

def fun(a,b):
    print(a+b)
# fun([1,2])
# fun(*[1,2])

import random
# random.seed(1)
print(random.random())

# random.seed(1)
print(random.random())
print(random.randrange(3,6,2)) #not  6
print(random.randint(3,6))
lst=[1,2,3,4,5,6]
random.shuffle(lst)
print(lst)
friend=['Ram','shyam','sita']
best_friend=random.choice(friend)
print(best_friend)
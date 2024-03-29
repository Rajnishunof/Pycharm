import copy


def dup(lst):
    newlst=[]
    for i in lst:
        if i not in newlst:
            newlst.append(i)
    return newlst

def cummulative(lst):
    newlst=[]
    sum=0
    for i in lst:
        sum=sum+i
        newlst.append(sum)
    return newlst
def freq(str):
    letf={}
    letg={}
    for ch in str:
            letf[ch]=letf.get(ch,0)+1
            letg[ch]=str.count(ch)
    print(letf)
    print(letg)


# lst=eval(input("enter the list "))
lst=[1,1,1,2,2,2,3,4,5,1,2,2,3,1]
print(dup(lst))
print(cummulative(lst))
freq("RajnishKumar is my name")
# l1=copy.copy(list1)simple copy not nested
# l1=copy.deepcopy(list1)simple copy  nested
print("USing Assignment to copy")
lst1=[1,2,3,4]
lst2=lst1
lst2[0]=10
print(lst1)
print(lst2)
print("\n")

print("USing copy.copy to copy")
lst1=[1,2,3,4]
lst2=copy.copy(lst1)
lst2[0]=10
print(lst1)
print(lst2)
print("\n")

print("USing copy.copy to copy")
lst1=[1,2,3,4,[1,2]]
lst2=copy.copy(lst1)
lst2[4][1]=10
print(lst1)
print(lst2)
print("\n")

print("USing copy.deepcopy to copy")
lst1=[1,2,3,4,[1,2]]
lst2=copy.deepcopy(lst1)
lst2[4][1]=10
print(lst1)
print(lst2)
print("\n")

# USING LAMBDA FUNCTION
sum=lambda x,y:x+y
print(sum(1,2))

mark=[10,20,30,40]
updated_marks=list(map(lambda x:x+5,mark))
print(updated_marks)

l=[-1,-2,-3,4,-5]
l_pos=list(map(abs,l))
print(l_pos)

l_filter=list(filter(lambda x:x%2==0,l))
print(l_filter)

s1=set()
s1.add("ITER")
print(s1)
s1.update({1,2,3})
print(s1)
s1.update((1,2,3,6))
print(s1)
print("Set METHODS")
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1 | s2)
print(s1.union(s2))

print(s1 & s2)
print(s1.intersection(s2))

print(s1.difference(s2))
print(s1-s2)

print(s1.symmetric_difference(s2))
print((s1-s2) | (s2-s1))
print((s1 | s2) -(s1 & s2) )

s3={"Rajnish","Kumar"}
print(set.union(s1,s2,s3))

s1={1,2}
s2={1,2}
print(s1>s2)
print(s1>=s2)

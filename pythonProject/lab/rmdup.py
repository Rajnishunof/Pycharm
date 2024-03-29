def rmd(lst):
    for i in lst:
        k=lst.count(i)
        if(k>=2):
            for j in range(0,k-1):
               lst.remove(i)
    print(lst)
x=[1,2,3,3,4,1]
rmd(x)

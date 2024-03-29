def matrix(v1):

    print("\nTHE MATRIX IS ")
    for i in v1:
        for j in i:
            print(j," ",end='')
        print()
    print("\n")

def shape(v1):
    print("The dimension of the matrix is ")
    return len(v1),len((v1[0]))

def rownelements(v1,i):
    print(f"{i}th row of matrix is")
    return v1[i]

def coloumnelements(v1,i):
    print(f"{i}th coloumn of matrix is")

    return [a[i] for a in v1]

def identitymat(n):
    lst=[]
    for i in range(n):
        l=[]
        for j in range(n):
            if i==j:
                l.append(1)
            else:
                l.append(0)
        lst.append(l)

    return lst


v1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matrix(v1)
print(shape(v1))
print(rownelements(v1,2))
print(coloumnelements(v1,2))
print(matrix(identitymat(4)))


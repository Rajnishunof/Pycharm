f=open('f4','w')
f.write('SOAITER')
f.close()
f=open('f4','r')
print(f.read(3))
print(f.tell())#It gives where the pointer of read function reached
print(f.read(1))


# seek function
print(f.seek(2))
print(f.read(2))
f.close()
#It moves the curson to that position
print("write lines")
#readlines function : convert the data which are separated by space into list
#writelines function : we can write any data in the form of list
f=open('f4','w')

f.writelines(['aos','fda'])
f=open('f4','r')
print(f.read())
f.close()


# r+ is used to use as read and write mode both


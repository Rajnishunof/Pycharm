x=input("ENTER YOUR NAME\n")
f=open("f1",'w')
f.write(x)
f.close()

f=open('f1','r')
print(f.read())
f.close()

f=open('f1','a')
f.write("\nappending some text")
f.close()

f=open('f2')#2nd argument default is read 'r
print(f.read())
f.close()

# we cannot leave the file unclosed
# write function returns no of character in that file

k="Raj"
p=open("f3",'w')
print(p.write(k))

# read function can have arguement any no till that character it will read
p=open("f3",'r')
print(p.read(2))

import pickle
def main():
    f=open("pickleFile","wb") #write binary
    pickle.dump({1: 'one', 2: 'two'}, f)
    pickle.dump(['hello','world'],f)
    
    f=open('pickleFile','rb') #read binary
    value1=pickle.load(f)
    value2=pickle.load(f)
    print(value1,value2)
    f.close()
main()
import matplotlib.pyplot as plt
import numpy as np
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.9, 10289.7, 14958.3]
# plt.plot(years, gdp, color='red',marker='s',linestyle='--')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# movies=['a','b','c','e','f']
# award=[7,2,7,2,7]
# plt.bar(movies,award,color='green',edgecolor='black',width=0.9)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.yticks(range(-4,11))
# plt.show()

grades=[83,95,91,87,70,0,85,83,100,67,73,77,0]
lst=[min(grade//10*10,90) for grade in grades]
print(lst)
print(lst*2)




from collections import Counter as ct
# h=ct(lst)
# print(h)
# plt.bar([x+5 for x in h.keys()],h.values(),width=9)
# plt.bar(h.keys()+5,h.values(),width=9)
# plt.hist(lst,bins=100)
# plt.xticks([10*i for i in range(11)])
# plt.show()

variance=[1,2,4,8,16,32,64,128,256]
biassquare=[256,128,64,32,16,8,4,2,1]
totalError=[x+y for x,y in zip(variance,biassquare)]
website=[1,2,3,4,5,6,7,8,9]

xs=[i for i,_ in enumerate(variance)]

# plt.plot(xs,variance,'g-',label='variance')
# plt.plot(xs,biassquare,'r-.',label='bias')
# plt.plot(xs,totalError,'b:',label='totalerror')
plt.scatter(variance,biassquare)
plt.scatter([11,21,31,41,51,61,71,81],[101,91,81,71,61,51,41,31])

for label,friend,min in zip(website,variance,biassquare):
    plt.annotate(label,xy=(friend,min),xytext=(5,-5),textcoords='offset points')
# plt.xticks([])
plt.show()

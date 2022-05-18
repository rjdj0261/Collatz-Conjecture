import random as rd
#import matplotlib.pyplot as plt
a=rd.randint(0,100)
b=a
c=0
d=[]
while b!=1:
    d.append(b)
    c+=1
    if c<100000:
      if b%2==0:
        b//=2
      else:
        b=(b*1+1)//2
    else:
      break
print("Original No. =",a)
print("Hailstone Nos. =",d)
print("No. of Repetitions =",c)

#y=d
#x=range(len(y))
#plt.plot(x,y)

#plt.show()
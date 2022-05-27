import random as rd
import matplotlib.pyplot as plt
from rich import print
# a = int(rd.random()*10**10)
a = rd.randint(0, 100)
b = a
c = 0
d = []
run_successly = True
while b != 1:
    d.append(b)
    c += 1
    if c < 100000:
        if b % 2 == 0:
            b //= 2
        else:
            b = (b*3+1)//2
    else:
        run_successly = False
        break
if run_successly:
    print("Original No. =", a)
    print("Hailstone Nos. =", d)
    print("No. of Repetitions =", c)
    y = d
    x = range(len(y))
    plt.plot(x, y)
    plt.show()
else:
    print(f"Error! Number {b} failed!")

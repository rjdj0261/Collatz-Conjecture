import random as rd
from rich import print

# a = int(rd.random() * 10**100)
# a = rd.randint(0, 100)
a = 0

while a < 10**100:
    a+=1
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
                b = (b * 3 + 1) // 2
        else:
            run_successly = False
            break
    if run_successly:
        file_object = open('proof.txt', 'a')
        file_object.write("Original No. = " + str(a) + '\n')  
        file_object.write("Hailstone Nos. = " + str(d) + '\n')
        file_object.write("No. of Repetitions = " + str(c) + '\n')
    else:
        file_object.write(f"Error! Number {str(b)} failed!" + '\n')

file_object.close()
print("Done!")
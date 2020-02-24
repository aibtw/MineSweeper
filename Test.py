# make while loop
# while the nubber of elements in certain list x < 10 then get a two random int, if the two exist in x, continue
# else, add them to list x

import random


##value = random.random()
##print (value)
##
##value - random.uniform(1, 10)
##print (value)



##integer = random.randint(1,6)
##print (integer)


x = []
while len(x) < 10 :
    i = random.randint(0,7)
    j = random.randint(0,7)

    temp = [i, j]
    if x:
        if temp not in x:
            x.append(temp)
        else:
            continue
    else:
        x.append(temp)

print (x)



x = [[1,2,3],[5,6,7]]
print (x[1][1])

import random
x = 0
count = 0
y = False

while y == False:
    x = random.randrange(10000, 100000)
    print(x)
    count = count + 1
    if x == 69420:
        y = True
        print('It took ' + str(count) + ' attempts to get to 69420')


    

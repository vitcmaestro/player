import math
num = int(input(""))
if(num%2 == 0):
    print("yes")
else:
    for i in range(3,int(math.sqrt(num))+1):
        if(num%i == 0):
            print("yes")
            break
    else:
        print("no")

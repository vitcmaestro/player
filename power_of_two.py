num = int(input(""))
i = 1
n =2
while(n<=num):
    n = 2**i
    if(n == num):
        print("yes")
        break
    i+=1
else:
    print("no")

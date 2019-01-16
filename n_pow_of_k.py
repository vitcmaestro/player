import math
n,k = map(int,input().split())
num = k
i = 0
while(num<=n):
    if(num == n):
        print("yes")
        break
    num = k**i
    i+=1
else:
    print("no")

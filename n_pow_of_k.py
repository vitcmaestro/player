import math
n,k = map(int,input().split())
num = n
while(num>=k):
    if(num == k):
        print("yes")
        break
    num = int(math.sqrt(num))
else:
    print("no")

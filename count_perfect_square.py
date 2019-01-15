import math
def isperfect(num):
    temp = math.floor(math.sqrt(num))
    if(temp**2 == num ):
        return True
    else:
        return False
c =0
l,r = map(int,input().split())
for i in range(l,r+1):
    if(isperfect(i)):
        c+=1
print(c)

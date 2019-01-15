import math
num = int(input(""))
def isprime(n):
    if(n == 2):
        return True
    else:
        for j in range(3,n):
            if(n%j == 0):
                return False
        else:
            return True
c=0
for i in range(2,num+1):
    if(num%i == 0 and isprime(i)):
        if(c == 0):
            c+=1
            print(i,end="")
        else:
            print(" ",i,end = " ")

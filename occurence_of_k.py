n,k = map(int,input().split())
c =0
while(n>0):
    rem = n%10
    if(rem == k):
        c+=1
    n = n//10
print(c)

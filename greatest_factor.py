m,n = map(int,input().split())
temp = min(m,n)
for i in range(temp,0,-1):
    if(m%i == 0 and n%i == 0):
        print(i)
        break

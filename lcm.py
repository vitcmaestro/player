l,r = map(int,input().split())
maxer = l*r
temp = maxer
a = min(l,r)
b = max(l,r)
if(b%a ==0):
    print(b)
else:
    for i in range(temp,0,-1):
        if(temp %l == 0 and temp %r == 0):
            maxer = temp
        temp-=1
    print(maxer)

n,k = map(int,input().split())
lis = list(map(int,input().split()))
l = lis.index(k)
if k in lis:
    print("Yes")
else:
    print("No")

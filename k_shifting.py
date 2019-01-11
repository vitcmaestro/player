n,k = map(int,input().split())
lis = list(map(int,input().split()))
if(n<k):
    print(lis)
else:
    x= n-k
    for i in range(x,n):
        print(lis[i],end = " ")
    for i in range(0,x):
        if(i==x-1):
            print(lis[i],end="")
        else:
            print(lis[i],end = " ")

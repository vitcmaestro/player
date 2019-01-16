n = int(input())
lis = list(map(int,input().split()))
for i in range(n-1):
    if(lis[i]>lis[i+1]):
        print("no")
        break
else:
    print("yes")

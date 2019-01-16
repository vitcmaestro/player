n = int(input(""))
lis = []
for i in range(n):
    temp = list(map(int,input().split()))
    lis.append(temp)
lis.sort(key = lambda x: x[0])
c =0
for i in range(len(lis)-1):
    if(lis[i][0] < lis[i+1][0]):
        c+=1
print(c)

n = int(input(""))
lis = []
for i in range(n):
    temp = list(map(int,input().split()))
    lis.append(temp)
lis.sort(key = lambda x: x[0])
c =0
for i in range(len(lis)):
    if(lis[0][i] > lis[0][i+1]):
        c+=1
print(c)

l,r  = map(int,input().split())
lis = [i for i in range(2,r+1,1)]
lis2 = []
while(len(lis)>0):
    num = lis[0]
    lis.remove(lis[0])
    if(num>=l):
        lis2.append(num)
    i = 0
    while(i<len(lis)):
        if(lis[i]%num == 0):
            lis.remove(lis[i])
        i+=1
print(len(lis2))

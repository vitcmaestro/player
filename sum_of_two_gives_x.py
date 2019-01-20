n,x = map(int,input().split())
lis = list(map(int,input().split()))
j=0
while(j<len(lis)):
    for i in range(j+1,len(lis)):
        if(lis[j]+lis[i] == x):
            print("yes")
            exit()
    j+=1
else:
    print("no")

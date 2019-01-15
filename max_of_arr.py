n,k = map(int,input().split())
nlis = list(map(int,input().split()))
klis = list(map(int,input().split()))
c = 0
for i in klis:
    nlis.append(i)
    if(c == 0):
        print(max(nlis),end = "")
        c+=1
    else:
        print(" ",max(nlis),end = "")

P,A = map(int,input().split())
tot = P//2
d=False
for i in range(tot,0,-1):
    for j in range(1,tot):
        if(i+j == tot and i*j == A):
            print("yes")
            exit(0)
else:
    print("no")

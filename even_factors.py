num = int(input(""))
c = 0
for i in range(2,num+1,2):
    if(num%i == 0):
        if(c==0):
            c+=1
            print(i,end ="")
        else:
            print("",i,end ="")

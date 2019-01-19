num = int(input(""))
c =0
for i in range(1,num+1,2):
    if(num%i == 0):
        if(c==0):
            print(i,end = "")
            c +=1
        else:
            print("",i,end = "")

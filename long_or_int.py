x= input("")
num = int(x.replace(",",""))
if(num>= -2147483648 and num<= 2147483647):
    print("INT")
else:
    print("LONG")

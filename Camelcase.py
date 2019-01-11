str1 = input("")
str2 =""
for i in range(len(str1)):
    if(i==0):
        str2 +=str1[i].upper()
    elif(str1[i-1].isspace()):
        str2 +=str1[i].upper()
    else:
        str2 +=str1[i]
print(str2)

dic = {}
lis =[]
d= "yes"
str1,str2 = map(str,input("").split())
if(len(str1)!=len(str2)):
    d ="no"
else:
    for i in range(len(str1)):
        if str1[i] in lis:
            temp = dic[str1[i]]
            if(temp == str2[i]):
                d = "yes"
            else:
                d = "no"
        else:
            lis.append(str1[i])
            dic[str1[i]] = str2[i]
print(d)

str1,str2 = map(str,input().split())
if(len(str1) != len(str2)):
    d ="no"
else:
    count = 0
    for i in range(len(str1)):
        if(str1[i] != str2[i]):
            count+=1
            
    if(count == 1):
        d="yes"
    else:
        d ="no"
print(d)

str1 = input("")
str2 = ""
for i in range(0,len(str1)-1,2):
    str2 +=str1[i+1]
    str2+=str1[i]
print(str2)

s = input("")
s1 = ""
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        s1 = s1+i.lower()
    elif(ord(i)>=97 and ord(i)<=122):
        s1 = s1 + i.upper()
    else:
        s1 = s1+i
        
print(s1)

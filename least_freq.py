import collections
temp = input("")
s = temp.lower().replace(" ","")
s1 = []
for i in s:
    if i not in s1:
        s1.append(i)
count =[]
for i in range(len(s1)):
    count.append(s.count(s1[i]))
key = min(count)
''''for i in range(len(s1)):
    if s1[i] not in temp and s1[i].upper() in temp:
        s1[i] = s1[i].upper()'''
for i in range(len(s1)):
    if s1[i] not in temp and s1[i].upper() in temp and s[i] == 'w':
        s1[i] = s1[i].upper()
c= 0
for i in range(len(count)):
    if(count[i] == key):
        if(c==0):
            c+=1
            print(s1[i],end = "")
        else:
            print("",s1[i],end = "")

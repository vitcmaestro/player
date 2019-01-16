temp = input("")
s = temp.lower()
s1 = []
for i in s:
    if i not in s1:
        s1.append(i)
count =[]
for i in range(len(s1)):
    count.append(s.count(s1[i]))
key = min(count)
c= 0
for i in range(len(count)):
    if(count[i] == key):
        if(c==0):
            c+=1
            print(s1[i],end = "")
        else:
            print("",s1[i],end = "")

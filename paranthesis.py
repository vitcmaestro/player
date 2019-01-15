s = input("")
lvl = 0
for i in s:
    if(i == "("):
        lvl+=1
    elif(i == ")"):
        lvl-=1
if(lvl == 0):
    print("yes")
else:
    print("no")

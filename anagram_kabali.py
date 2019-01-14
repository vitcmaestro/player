
def isanagram():
    s1 = input("")
    s2 = s1.lower()
    if(len(s1) != 6):
        return False
    else:
        if(s2.count('a') == 2 and s2.count('k') == 1 and s2.count('b') == 1 and s2.count('l') and s2.count('i')):
            return True
        else:
            return False

n=int(input(""))
count = 0
for i in range(n):
    if(isanagram()):
        count+=1
print(count)

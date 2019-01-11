s =input("")
s2 = ""
l =['a','e','i','o','u','A','E','I','O','U']
for i in reversed(s):
    if i not in l:
        s2+=i
print(s2)

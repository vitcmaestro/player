import re
s = input("")
s1 = s.strip()
print(re.sub(' +', ' ',s1))

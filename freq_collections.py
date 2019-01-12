import collections

s =input("")
freq = collections.Counter(s)
maxer = 0
for key,value in freq.items():
    if(value > maxer):
        temp = key
        maxer = value
print(temp)

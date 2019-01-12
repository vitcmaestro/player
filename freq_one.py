import collections
n= int(input(""))
lis = list(map(str,input().split()))
freq = collections.Counter(lis)
for key,value in freq.items():
    if(value == 1):
        temp = key
print(temp)

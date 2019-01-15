import operator
from collections import OrderedDict
n = int(input(""))
listemp = list(map(str,input().split()))
lentemp = []
for i in listemp:
    lentemp.append(len(i))
d = OrderedDict(zip(listemp, lentemp))
out = sorted(d.items(), key=operator.itemgetter(1), reverse=False)
c = 0
for i,k in out:
    if(c==0):
        print(i,end = "")
        c+=1
    else:
        print("",i,end ="")

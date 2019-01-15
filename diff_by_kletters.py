s1,s2,s3 = map(str,input().split())
k = int(s3)
if(len(s1) != len(s2)):
    print("no")
else:
    c =0
    for i in range(len(s1)):
        if(s1[i] != s2[i]):
            c+=1
    if(c == k):
        print('yes')
    else:
        print('no')

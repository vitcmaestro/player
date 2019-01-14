val = input("")
ans=""
for i in val:
    d=ord(i)+3
    if(d>90):
        d = d-26
    ans = ans + chr(d)
print(ans)

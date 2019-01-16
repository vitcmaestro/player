s1,subs = map(str,input().split())
num = int(subs)
ans =s1
n = len(s1)
for i in range(num):
    ans = ans[-1:]+ans[:n-1]
print(ans)

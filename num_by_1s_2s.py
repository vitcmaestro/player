num = int(input(""))
count = 0
for i in range(num+1):
    for j in range(num+1):
        ans = (1*i)+(2*j)
        if(ans == num):
            count+=1
print(count)

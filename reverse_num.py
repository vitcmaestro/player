num = int(input(""))
rev = 0
while(num>=1):
    rem = num%10
    rev = (rev*10)+rem
    num = num//10
print(rev)

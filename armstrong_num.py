n=int(input("enter a number: "))
num=n
total=0
str_num = len(str(num))
while num>0:
    d=num%10
    total=total+(d**str_num)
    num=num//10
if n==total:
        print(n,"is armstrong")
else:
        print(n,"is not armstrong")
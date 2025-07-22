n= 1234
num=n
result=0
while num>0:
    d=num%10
    result=(result*10)+d
    num=num//10
if n==result:   
    print(n, "is palimdrome")
else:
    print(n, "is not palimdrome")
n= int(input("enter a number"))

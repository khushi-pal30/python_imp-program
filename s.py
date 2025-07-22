amount=int(input("enter a amount"))
if amount>=10000:
   print(amount+1000)

sal=int(input("enter a salary"))
if sal>=10000 and sal<20000:
    b=sal*10/100+sal
    print(b)
elif sal>=20000 and sal<30000:
    c=sal*8/100+sal
    print(c)
elif sal>=30000 and sal<40000:
    d=sal*9/100+sal
    print(d)
elif sal>=40000 and sal<50000:
    e=sal*10/100+sal
    print(e)

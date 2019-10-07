n1=int(input("enter the first number to compare : "))
n2=int(input("enter the second number to compare : "))
n3=int(input("enter the third number to compare : "))
if n1<n2 and n1<n3 :
    print(n1)
elif n2<n3 :
    print(n2)
else:
    print(n3)
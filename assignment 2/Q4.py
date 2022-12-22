a=int(input("Enter value of a = "))
b=int(input("Enter value of b = "))
c=int(input("Enter value of c = "))

if(a>b & a>c):
    print("a is greater than both b and c")

elif(b>a and b>c):
    print("b is greater than both a and c")

else:
    print("c is greater than both a and b")
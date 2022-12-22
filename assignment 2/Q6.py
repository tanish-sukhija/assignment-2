a=int(input("Enter the length of side 1 : "))
b=int(input("Enter the length of side 2 : "))
c=int(input("Enter the length of side 3 : "))

if(a+b>c and a+c>b and b+c>a):
    print("The triangle can be formed")

else:
    print("The triangle cannot be formed")
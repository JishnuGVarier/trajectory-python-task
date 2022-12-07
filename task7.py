a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=1
while(c==1):
    d=(input("Enter any one of these operators( + , - , * , / , % ): "))
    if d=='+':
        print("Addition of numbers= ",(a+b))
    elif d=='-':
        print("Subtraction of numbers= ",(a-b))
    elif d=='*':
        print("Multiplication of numbers= ",(a*b))
    elif d=='/':
        print("Division of numbers= ",(a/b))
    elif d=='%':
        print("Remainder after division of numbers= ",(a%b))
    else:
        print("Invalid operator")
    p=input("Do you want to continue the operations? say 'y' or 'n'...")
    if p=='y':
        c=1
    else:
        c=0
        print("Exited...")
print("Simple Calculator")
print("Enter Operation~")
print("1.For sum a + b")
print("2.For subtraction a - b")
print("3.For multiplication a * b")
print("4.For division a / b")

while(True):
   
    choice = int(input("Enter Choice:~"))
    if(choice > 4):
        print("Enter Valid Choice")

    print("Enter numbers =>")

    try:
        a = float(input("Enter a:"))
        b = float(input("Enter b:"))
    except:
        print("Invalid Input. Lets Start again.....")
        continue

    
    if(choice == 1):
        print("summation" ,a, "and" , b, "is", a+b )
    elif(choice == 2):
        print("subtraction" ,a, "and" , b, "is", a-b )
    elif(choice == 3):
        print("multiplication" ,a, "and" , b, "is", a*b )
    elif(choice == 4):
        print("Division" ,a, "and" , b, "is", a/b )

    print("Do you want to use calculator!!! 1/0")
    if(input() == 0):
        break;

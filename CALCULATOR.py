print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
operation=input()
if operation =="1":
    #code for add
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    print("The Sum is "+str(int(num1)+int(num2)))
elif operation =="2":
    #code for subtract
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    print("The Difference is "+str(int(num1)-int(num2)))
elif operation =="3":
    #code for multiply
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    print("The Product is "+str(int(num1)*int(num2)))
elif operation =="4":
    #code for divide
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    print("The Divisor is "+str(int(num1)/int(num2)))
else:
    print("INVALID ENTRY")
    

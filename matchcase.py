#calculator:
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

operator = input("enter operator: ")

match operator:
    case "+":
        print("Sum is",num1 + num2)
    case "-":
        print("Sum is",num1 - num2) 
    case "*":
        print("Sum is",num1 * num2) 
    case "/":
        print("Sum is",num1 / num2)
    case _ :
        print("Enter a valid operator")
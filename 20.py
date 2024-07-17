#making calculator 

a = int(input("enter number a"))
b = int(input("enter number b"))

operator = input("enter operator")

match operator:
    case "+": 
        print("sum is ",a+b) 
    case "-": 
        print("subtract is ",a-b)
    case "*": 
        print("multi is ",a*b)
    case "/": 
        print("div ",a/b)
    case "**": 
        print("exponetial is ",a**b)
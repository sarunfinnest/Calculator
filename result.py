from addition import addition
from division import division
from substracion import substraction
from reminder import reminder
from multiplication import multiplication


while True:
    i=int(input("Choose an option :\n1.Continue\n2.Exit\n"))
    if i==1:
        pass
    elif i==2:
        break
    else:
        print("Invalid input. Please enter a valid input.") 
    n1 = int(input("Enter first number"))
    n2 = int((input("Enter the second number")))
    ops =input("select a operation : +,-,/,*,%")

    if ops=='+':
        print(addition(n1,n2))
    elif(ops=='-'):
        print(substraction(n1,n2))
    elif(ops=='*'):
        print(multiplication(n1,n2))
    elif(ops=='/'):
        print(division(n1,n2))
    elif(ops=='%'):
        print(reminder(n1,n2))
    # elif(ops=="exit"):
    #     break
    else:
        print("invalid input")








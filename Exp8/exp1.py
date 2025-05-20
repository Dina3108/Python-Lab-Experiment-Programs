try:
    num1=int(input("Enter Number 1 :"))
    num2=int(input("Enter Number 2 :"))
    print(f'Addition : {num1+num2}')
    print(f'Subtraction : {num1-num2}')
    print(f'Multiplication : {num1*num2}')
    print(f'Division : {num1/num2}')
    
except ZeroDivisionError:
    print('Cannot divide by Zero!')
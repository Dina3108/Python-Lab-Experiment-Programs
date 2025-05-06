import standard.std_cal as std
import scientific.sci_cal as sci
import programmer.pro_cal as pro

def standard_mode():
    print("\nStandard Calculator")
    print("Available operations:")
    print("1. Add  2. Subtract  3. Multiply  4. Divide")
    print("5. Modulus  6. Square  7. Square Root  8. Reciprocal")

    choice = input("Enter operation number: ")

    if choice in ['1', '2', '3', '4', '5']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", std.add(x, y))
        elif choice == '2':
            print("Result:", std.sub(x, y))
        elif choice == '3':
            print("Result:", std.mul(x, y))
        elif choice == '4':
            print("Result:", std.div(x, y))
        elif choice == '5':
            print("Result:", std.mod(x, y))
    elif choice == '6':
        x = float(input("Enter number: "))
        print("Square:", std.sq(x))
    elif choice == '7':
        x = float(input("Enter number: "))
        print("Square Root:", std.sqr(x))
    elif choice == '8':
        x = float(input("Enter number: "))
        print("Reciprocal:", std.reci(x))
    else:
        print("Invalid choice.")

def scientific_mode():
    print("\nScientific Calculator")
    print("1. Power  2. Square Root  3. Factorial  4. Logarithm")
    print("5. Exponential  6. Trigonometry  7. Inverse Trigonometry")
    print("8. Hypotenuse  9. Constants")

    choice = input("Enter operation number: ")

    if choice == '1':
        x = float(input("Enter base: "))
        y = float(input("Enter exponent: "))
        print("Result:", sci.pow(x, y))
    elif choice == '2':
        x = float(input("Enter number: "))
        print("Square Root:", sci.sqrt(x))
    elif choice == '3':
        x = int(input("Enter number: "))
        print("Factorial:", sci.fact(x))
    elif choice == '4':
        x = float(input("Enter number: "))
        print("Logarithm:", sci.log(x))
    elif choice == '5':
        x = float(input("Enter number: "))
        print("Exponential:", sci.exp(x))
    elif choice == '6':
        angle = float(input("Enter angle in degrees: "))
        print("sin:", sci.sin(angle))
        print("cos:", sci.cos(angle))
        print("tan:", sci.tan(angle))
        print("cosec:", sci.cosec(angle))
        print("sec:", sci.sec(angle))
        print("cot:", sci.cot(angle))
    elif choice == '7':
        x = float(input("Enter value between -1 and 1 for inverse sin/cos, any real number for tan: "))
        print("asin:", sci.isin(x))
        print("acos:", sci.icos(x))
        print("atan:", sci.itan(x))
        print("acosec:", sci.icosec(x))
        print("asec:", sci.isec(x))
        print("acot:", sci.icot(x))
    elif choice == '8':
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        print("Hypotenuse:", sci.hypo(a, b))
    elif choice == '9':
        print("Pi:", sci.pi(0))
        print("Euler's Number:", sci.euler(0))
    else:
        print("Invalid choice.")

def programmer_mode():
    print("\nProgrammer Calculator")
    print("1. AND  2. OR  3. XOR  4. NOT  5. Left Shift  6. Right Shift")
    print("7. Binary  8. Octal  9. Hexadecimal")
    print("10. Binary to Decimal  11. Octal to Decimal  12. Hex to Decimal")

    choice = input("Enter operation number: ")

    if choice in ['1', '2', '3']:
        x = int(input("Enter first integer: "))
        y = int(input("Enter second integer: "))
        if choice == '1':
            print("Result:", pro.band(x, y))
        elif choice == '2':
            print("Result:", pro.bor(x, y))
        elif choice == '3':
            print("Result:", pro.bxor(x, y))
    elif choice == '4':
        x = int(input("Enter integer: "))
        print("NOT:", pro.bnot(x))
    elif choice == '5':
        x = int(input("Enter integer: "))
        print("Left Shift (by 2):", pro.lshift(x))
    elif choice == '6':
        x = int(input("Enter integer: "))
        print("Right Shift (by 2):", pro.rshift(x))
    elif choice == '7':
        x = int(input("Enter number: "))
        print("Binary:", pro.binary(x))
    elif choice == '8':
        x = int(input("Enter number: "))
        print("Octal:", pro.octal(x))
    elif choice == '9':
        x = int(input("Enter number: "))
        print("Hexadecimal:", pro.hexadecimal(x))
    elif choice == '10':
        x = input("Enter binary string: ")
        print("Decimal:", pro.btodecimal(x))
    elif choice == '11':
        x = input("Enter octal string: ")
        print("Decimal:", pro.otodecimal(x))
    elif choice == '12':
        x = input("Enter hexadecimal string: ")
        print("Decimal:", pro.htodecimal(x))
    else:
        print("Invalid choice.")

while True:
    print("\n--- Welcome to the Python Calculator ---")
    print("Select calculator mode:")
    print("1. Standard")
    print("2. Scientific")
    print("3. Programmer")
    print("4. Exit")

    mode = input("Enter your choice: ")

    if mode == '1':
        standard_mode()
    elif mode == '2':
        scientific_mode()
    elif mode == '3':
        programmer_mode()
    elif mode == '4':
        print("Thank you for using the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please choose between 1 to 4.")
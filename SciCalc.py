### Python Scientific Calculator

## Importing Modules
import math, cmath, statistics, time, os, random

## User Defined Functions
def clearscreen():
    if os.name == 'nt': # Windows only
        os.system('cls')
    else: # other OSs
        os.system('clear')
def endfunc():
    input("Press Enter to return to main menu.")
    clearscreen()
def integerinput(prompt, minimum = None, maximum = None, notallowed = None):
    while True:
        try:
            variable = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        if minimum is not None and variable < minimum:
            print(f"Invalid input. Please enter an integer more than or equal to {minimum}.")
            continue
        if maximum is not None and variable > maximum:
            print(f"Invalid input. Please enter an integer less than or equal to {maximum}.")
            continue
        if notallowed is not None and variable == notallowed:
            print(f"Invalid input. Please enter an integer that is not {notallowed}.")
            continue
        return variable
def floatinput(prompt, minimum = None, maximum = None, notallowed = None):
    while True:
        try:
            variable = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if minimum is not None and variable < minimum:
            print(f"Invalid input. Please enter a number more than or equal to {minimum}.")
            continue
        if maximum is not None and variable > maximum:
            print(f"Invalid input. Please enter a number less than or equal to {maximum}.")
            continue
        if notallowed is not None and variable == notallowed:
            print(f"Invalid input. Please enter a number that is not {notallowed}.")
            continue
        return variable
## Splash Screen
print("Scientific Calculator for Python 3.6+ v1.0.1")
time.sleep(1.5)
clearscreen()

## Main Program
while True:
    mainmode = input("╭──┬───────────────────────╮\n│ 1│Basic Arithmetic       │\n│ 2│Scientific Calculations│\n│ 3│Equation Solver        │\n│ 4│Trigonometry           │\n│ 5│Base Converter         │\n│ 6│Word Problems          │\n│ 7│Statistics             │\n│ 8│Random Number Generator│\n├──┼───────────────────────┤\n│ f│Formulae               │\n│ q│Quit                   │\n╰──┴───────────────────────╯\n")
    if mainmode == '1':
        submode = input("\n1│Addition\n2│Subtraction\n3│Multiplication\n4│Division\n5│Sum\n ├────────────────\n6│Back to Main Menu\n")
        if submode == '1':
            a = floatinput("Enter first number: ")
            b = floatinput("Enter second number: ")
            result = a + b
            print(f"Result: {result}")
            endfunc()
        elif submode == '2':
            a = floatinput("Enter first number: ")
            b = floatinput("Enter second number: ")
            result = a - b
            print(f"Result: {result}")
            endfunc()
        elif submode == '3':
            a = floatinput("Enter first number: ")
            b = floatinput("Enter multiplier: ")
            result = a * b
            print(f"Result: {result}")
            endfunc()
        elif submode == '4':
            a = floatinput("Enter number: ")
            b = floatinput("Enter divisor: ", notallowed=0)
            result = a / b
            print(f"Result: {result}")
            endfunc()
        elif submode == '5':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            result = sum(data)
            print(f"Sum: {result}")
            endfunc()
        elif submode == '6':
            clearscreen()
            continue
        else:
            print("Error: not valid function")
    elif mainmode == '2':
        submode = input("\n 1│Exponent\n 2│Logarithm\n 3│Natural log\n 4│nth root\n 5│Pythagoras\' Theorem\n 6│Radians to Degrees\n 7│Degrees to Radians\n 8│Factorial\n 9│nCr\n10│nPr\n  ├────────────────\n11│Back to Main Menu\n")
        if submode == '1':
            a = floatinput("Enter number: ")
            b = floatinput("Enter exponent: ")
            result = a ** b
            print(f"Result: {result}")
            endfunc()
        elif submode == '2':
            a = floatinput("Enter number: ", 0, notallowed=0)
            b = floatinput("Enter base of logarithm: ", 0, notallowed=1)
            result = math.log(a, b)
            print(f"Result: {result}")
            endfunc()
        elif submode == '3':
            a = floatinput("Enter number: ", 0, notallowed=0)
            result = math.log(a)
            print(f"Result: {result}")
            endfunc()
        elif submode == '4':
            a = floatinput("Enter number: ")
            b = floatinput("Enter root: ", notallowed=0)
            result = a ** (1/b)
            print(f"Result: {result}")
            endfunc()
        elif submode == '5':
            a = floatinput("Enter horizontal change: ")
            b = floatinput("Enter vertical change: ")
            result = math.sqrt((a ** 2) + (b ** 2))
            print("Diagonal length:", result)
            endfunc()
        elif submode == '6':
            a = floatinput("Enter angle in radians")
            result = math.degrees(a)
            print(f"Result: {result:.5f}°")
            endfunc()
        elif submode == '7':
            a = floatinput("Enter angle in degrees: ")
            result = math.radians(a)
            print(f"Result: {result} radians")
            endfunc()
        elif submode == '8':
            a = integerinput("Enter number: ", 0)
            result = math.factorial(a)
            print(f"Result: {result}")
            endfunc()
        elif submode == '9':
            a = integerinput("Enter number of items: ", 0)
            b = integerinput("Enter number of items chosen: ", 0, a)
            result = math.comb(a, b)
            print("result:", int(result))
            endfunc()
        elif submode == '10':
            a = integerinput("Enter number of items: ", 0)
            b = integerinput("Enter number of items chosen: ", 0 , a)
            result = math.perm(a, b)
            print("result:", int(result))
            endfunc()
        elif submode == '11':
            clearscreen()
            continue
        else:
            print("Error: not valid function")
    elif mainmode == '3':
        submode = input("\n1│Linear Equation Solver\n2│Quadratic Equation Solver\n3│Discriminant\n ├────────────────\n4│Back to Main Menu\n")
        if submode == '1':
            a = floatinput("Enter x term: ", notallowed=0)
            b = floatinput("Enter constant: ")
            result = (b * -1) / a
            print(f"Result: {result}")
            endfunc()
        elif submode == '2':
            a = floatinput("Enter x² term: ", notallowed=0)
            b = floatinput("Enter x term: ")
            d = floatinput("Enter constant: ")
            discriminant = (b ** 2) - (4 * a * d)
            result1 = ((b * -1) + cmath.sqrt(discriminant)) / (a * 2)
            result2 = ((b * -1) - cmath.sqrt(discriminant)) / (a * 2)
            print(f"result: {result1}, {result2}")
            endfunc()
        elif submode == '3':
            a = floatinput("Enter x² term: ")
            b = floatinput("Enter x term: ")
            d = floatinput("enter constant: ")
            result = (b ** 2) - (4 * a * d)
            print(f"Result: {result}")
            endfunc()
        elif submode == '4':
            clearscreen()
            continue
    elif mainmode == '4':
        submode = input("\n 1│Sine\n 2│Cosine\n 3│Tangent\n 4│Inverse Sine\n 5│Inverse Cosine\n 6│Inverse Tangent\n  ├────────────────\n 7│Hyperbolic Sine\n 8│Hyperbolic Cosine\n 9│Hyperbolic Tangent\n10│Hyperbolic Inverse Sine\n11│Hyperbolic Inverse Cosine\n12│Hyperbolic Inverse Tangent\n  ├────────────────\n13│Back to Main Menu\n")
        if submode == '1':
            a = floatinput("Enter angle in degrees: ")
            if a == 30:
                result = 0.5
            elif a == 45:
                result = "1/√2"
            elif a == 60:
                result = "√3/2"
            else:
                a = math.radians(a)
                result = round(math.sin(a), 5)
            print(f"Result: {result}")
            endfunc()
        elif submode == '2':
            a = floatinput("Enter angle in degrees: ")
            if a == 30:
                result = "√3/2"
            elif a == 45:
                result = "1/√2"
            elif a == 60:
                result = 0.5
            else:
                a = math.radians(a)
                result = round(math.cos(a), 5)
            print(f"Result: {result}")
            endfunc()
        elif submode == '3':
            a = floatinput("Enter angle in degrees: ", notallowed=90)
            if a == 30:
                result = "1/√3"
            elif a == 45:
                result = 1
            elif a == 60:
                result = "√3"
            else:
                a = math.radians(a)
                result = round(math.tan(a), 5)
            print(f"Result: {result}")
            endfunc()
        elif submode == '4':
            a = floatinput("Enter number: ", -1, 1)
            if a == 0.5:
                result = 30
            else:
                a = math.asin(a)
                result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '5':
            a = floatinput("Enter number: ", -1, 1)
            if a == 0.5:
                result = 60
            else:
                a = math.acos(a)
                result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '6':
            a = floatinput("Enter number: ")
            if a == 1:
                result = 45
            else:
                a = math.atan(a)
                result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '7':
            a = floatinput("Enter angle in degrees: ")
            a = math.radians(a)
            result = round(math.sinh(a), 5)
            print(f"Result: {result}")
            endfunc()
        elif submode == '8':
            a = floatinput("Enter angle in degrees: ")
            a = math.radians(a)
            result = round(math.cosh(a), 5)
            print(f"Result: {result}")
            endfunc()
        elif submode == '9':
            a = floatinput("Enter angle in degrees: ")
            a = math.radians(a)
            result = round(math.tanh(a), 5)
            print(f"Result: {result}")
            endfunc()
        elif submode == '10':
            a = floatinput("Enter number: ")
            a = math.asinh(a)
            result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '11':
            a = floatinput("Enter number: ", 1)
            a = math.acosh(a)
            result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '12':
            a = floatinput("Enter number: ", -1, 1)
            a = math.atanh(a)
            result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '13':
            clearscreen()
            continue 
        else:
            print("Error: not valid function")
    elif mainmode == '5':
        submode = input("\n1│Denary to Binary\n2│Denary to Hex\n3│Binary to Denary\n4│Binary to Hex\n5│Hex to Denary\n6│Hex to Binary\n ├────────────────\n7│Back to Main Menu\n")
        if submode == '1':
            a = integerinput("Enter number to be converted: ")
            result = bin(a)[2:]
            print(f"Result: {result}")
            endfunc()
        elif submode == '2':
            a = integerinput("Enter number to be converted: ")
            result = hex(a)[2:]
            print(f"Result: {result}")
            endfunc()
        elif submode == '3':
            a = input("Enter number to be converted: ")
            result = int(a, 2)
            print(f"Result: {result}")
            endfunc()
        elif submode == '4':
            a = input("Enter number to be converted: ")
            a = int(a, 2)
            result = hex(a)[2:]
            print(f"Result: {result}")
            endfunc()
        elif submode == '5':
            a = input("Enter number to be converted: ")
            result = int(a ,16)
            print(f"Result: {result}")
            endfunc()
        elif submode == '6':
            a = input("Enter number to be converted: ")
            a = int(a ,16)
            result = bin(a)[2:]
            print(f"Result: {result}")
            endfunc()
        elif submode == '7':
            clearscreen()
            continue
    elif mainmode == '6':
        submode = input("\n1│Compound Interest - Total Amount\n2│Compound Interest - Interest\n3│Area of Triangle\n4│Area of Circle\n ├────────────────\n5│Back to Main Menu\n")
        if submode == '1':
            a = floatinput("Enter original amount: ")
            b = floatinput("Enter interest rate: ")
            c = integerinput("Enter number of terms used: ")
            result = a * ((1 + (b / 100)) ** c)
            print("total amount: $" + str(round(result, 2)))
            endfunc()
        elif submode == '2':
            a = floatinput("Enter original amount: ")
            b = floatinput("Enter interest rate: ")
            c = integerinput("Enter number of terms used: ")
            result = (a * ((1 + (b / 100)) ** c)) - a
            print("interest: $" + str(round(result, 2)))
            endfunc()
        elif submode == '3':
            a = floatinput("Enter side 1: ", 0)
            b = floatinput("Enter side 2: ", 0)
            c = floatinput("Enter angle between sides in degrees: ", 0, 180)
            c = math.radians(c)
            result = (a * b * math.sin(c))/ 2
            print("Area: ", round(result, 5))
            endfunc()
        elif submode == '4':
            a = floatinput("Enter radius: ", 0)
            result = math.pi * (a ** 2)
            print("Area: ", round(result, 5))
            endfunc()
        elif submode == '5':
            clearscreen()
            continue 
        else:
            print("Error: not valid function")
    elif mainmode == '7':
        submode = input("\n1│Mean\n2│Median\n3│Mode\n4│Standard Deviation\n5│Variance\n ├────────────────\n6│Back to Main Menu\n")
        if submode == '1':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            result = statistics.mean(data)
            print(f"Mean: {result}")
            endfunc()
        elif submode == '2':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            result = statistics.median(data)
            print(f"Median: {result}")
            endfunc()
        elif submode == '3':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            result = statistics.multimode(data)
            if result == []:
                print("There is no mode.")
            else:
                print(f"Mode: {result}")
            endfunc()
        elif submode == '4':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            try:
                result = statistics.pstdev(data)
                print(f"Standard Deviation: {result}")
            except statistics.StatisticsError:
                result = 0
                print("There is no standard deviation.")
            endfunc()
        elif submode == '5':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            try:
                result = statistics.pvariance(data)
                print(f"Variance: {result}")
            except statistics.StatisticsError:
                result = 0
                print("There is no variance.")
            endfunc()
        elif submode == '6':
            clearscreen()
            continue 
        else:
            print("Error: not valid function")
    elif mainmode == '8':
        submode = input("\n1│Random Floating Point\n2│Random Integers\n ├────────────────\n3│Back to Main Menu\n")
        if submode == '1':
            c = integerinput("Enter number of numbers needed: ", 0)
            a = floatinput("Enter minimum: ")
            b = floatinput("Enter maximum: ", a)
            for i in range(c):
                result = random.uniform(a, b)
                print(str(i+1) + "|" + str(result))
            endfunc()
        elif submode == '2':
            c = integerinput("Enter number of numbers needed: ", 0)
            a = integerinput("Enter minimum: ")
            b = integerinput("Enter maximum: ", a)
            for i in range(c):
                result = random.randint(a, b)
                print(str(i+1) + "|" + str(result))
            endfunc()
        elif submode == '3':
            clearscreen()
            continue 
        else:
            print("Error: not valid function")
    elif mainmode == 'f':
        submode = input("\n1│Quadratic Equation\n2│Compound Interest\n3│3D Mensuration\n4│Circle Mensuration\n5│E Math Trigonometry\n6│A Math Trigonometry\n ├────────────────\n7│Back to Main Menu\n")
        if submode == '1':
            print("x = -b±√(b²-4ac) / 2a")
            endfunc()
        elif submode == '2':
            print("Total Amount = P(1+ r/100)ⁿ\nInterest = P(1+ r/100)ⁿ - P")
            endfunc()
        elif submode == '3':
            print("Curved surface area of cone = πrl\nSurface area of sphere = 4πr²\nVolume of a cone = 1/3 πr²h\nVolume of sphere = 4/3 πr³")
            endfunc()
        elif submode == '4':
            print("when θ is in radians,\nArc length = rθ\nSector area = 1/2 r²θ")
            endfunc()
        elif submode == '5':
            print("Area of triangle ABC = 1/2 ab sin C\nSine law : a/sin A = b/sin B = c/sin C\nCosine law: a²=b²+c²-2bc cos A")
            endfunc()
        elif submode == '6':
            print("sin²A + cos²A = 1\n\nsec²A = 1 + tan²A\ncosec²A = 1 + cot²A\n\nsin(A±B) = sinA cosB ± cosA sinB\ncos(A±B) = cosA cosB ∓ sinA sinB\ntan(A±B) = tanA±tanB/1∓tanA tanB\n\nsin2A = 2 sinA cosA\ncos2A = cos²A - sin²A = 2cos²A - 1 - 2sin²A\ntan2A = 2tanA / 1 - tan²A")
            endfunc()
        elif submode == '7':
            endfunc()
            continue 
        else:
            print("Invalid option, please enter an existing one.")
    elif mainmode == 'q':
        print("Goodbye")
        time.sleep(1)
        break
    else:
        clearscreen()
        continue

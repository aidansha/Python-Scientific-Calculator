### Python Scientific Calculator

## Variables
# a, b, c
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

## Splash Screen
print("Scientific Calculator for Python 3.13")
time.sleep(1.5)
clearscreen()

## Main Program
while True:
    mainmode = input("╭──┬───────────────────────╮\n│ 1│Basic Arithmetic       │\n│ 2│Scientific Calculations│\n│ 3│Equation Solver        │\n│ 4│Trigonometry           │\n│ 5│Base Converter         │\n│ 6│Word Problems          │\n│ 7│Statistics             │\n│ 8│Random Number Generator│\n├──┼───────────────────────┤\n│ f│Formulae               │\n│ q│Quit                   │\n╰──┴───────────────────────╯\n")
    if mainmode == '1':
        submode = input("\n1│Addition\n2│Subtraction\n3│Multiplication\n4│Division\n5│Sum\n ├────────────────\n6│Back to Main Menu\n")
        if submode == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a + b
            print("Result:", result)
            endfunc()
        elif submode == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a - b
            print("Result:", result)
            endfunc()
        elif submode == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter multiplier: "))
            result = a * b
            print("Result:", result)
            endfunc()
        elif submode == '4':
            a = float(input("Enter number: "))
            while True:
                b = float(input("Enter divisor: "))
                if b == 0:
                    print("Divisor cannot be 0. Enter another number.")
                else:
                    break
            result = a / b
            print("Result:", result)
            endfunc()
        elif submode == '5':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            result = sum(data)
            print("sum:", result)
            endfunc()
        elif submode == '6':
            clearscreen()
            continue
        else:
            print("Error: not valid function")
    elif mainmode == '2':
        submode = input("\n 1│Exponent\n 2│Logarithm\n 3│Natural log\n 4│nth root\n 5│Pythagoras\' Theorem\n 6│Radians to Degrees\n 7│Degrees to Radians\n 8│Factorial\n 9│nCr\n10│nPr\n  ├────────────────\n11│Back to Main Menu\n")
        if submode == '1':
            a = float(input("Enter number: "))
            b = float(input("Enter exponent: "))
            result = a ** b
            print("Result:", result)
            endfunc()
        elif submode == '2':
            a = float(input("Enter number: "))
            b = float(input("Enter base of logarithm: "))
            result = math.log(a, b)
            print("Result:", result)
            endfunc()
        elif submode == '3':
            a = float(input("Enter number: "))
            result = math.log(a)
            print("Result:", result)
            endfunc()
        elif submode == '4':
            a = float(input("Enter number: "))
            b = float(input("Enter nth root"))
            result = a ** (1/b)
            print("Result:", result)
            endfunc()
        elif submode == '5':
            a = float(input("Enter horizontal change: "))
            b = float(input("Enter vertical change: "))
            result = math.sqrt((a ** 2) + (b ** 2))
            print("Diagonal length:", result)
            endfunc()
        elif submode == '6':
            a = float(input("Enter angle in radians"))
            result = math.degrees(a)
            print(f"result: {result:.5f}°")
            endfunc()
        elif submode == '7':
            a = float(input("Enter angle in degrees: "))
            result = math.radians(a)
            print(f"result: {result} radians")
            endfunc()
        elif submode == '8':
            while True:
                a = input("Enter number: ")
                if not a.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    a = int(a)
                    if a <= 0:
                        print("Invalid input. Number must be more than 0.")
                    else:
                        break
            result = math.factorial(a)
            print("result:", result)
            endfunc()
        elif submode == '9':
            while True:
                a = input("Enter number of items: ")
                if not a.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    a = int(a)
                    break
            while True:
                b = input("Enter number of items chosen: ")
                if not b.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    b = int(b)
                    break
            result = math.comb(a, b)
            print("result:", int(result))
            endfunc()
        elif submode == '10':
            while True:
                a = input("Enter number of items: ")
                if not a.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    a = int(a)
                    break
            while True:
                b = input("Enter number of items chosen: ")
                if not b.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    b = int(b)
                    break
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
            while True:
                a = input("Enter x term: ")
                if a == "0":
                    print("Invalid input. x term cannot be 0.")
                else:
                    a = float(a)
                    break
            b = float(input("Enter constant: "))
            result = (b * -1) / a
            print("result:", result)
            endfunc()
        elif submode == '2':
            a = float(input("Enter x² term: "))
            b = float(input("Enter x term: "))
            d = float(input("Enter constant: "))
            discriminant = (b ** 2) - (4 * a * d)
            result1 = ((b * -1) + cmath.sqrt(discriminant)) / (a * 2)
            result2 = ((b * -1) - cmath.sqrt(discriminant)) / (a * 2)
            print(f"result: {result1}, {result2}")
            endfunc()
        elif submode == '3':
            a = float(input("Enter x² term: "))
            b = float(input("Enter x term: "))
            d = float(input("enter constant: "))
            result = (b ** 2) - (4 * a * d)
            print("result:", result)
            endfunc()
        elif submode == '4':
            clearscreen()
            continue
    elif mainmode == '4':
        submode = input("\n 1│Sine\n 2│Cosine\n 3│Tangent\n 4│Inverse Sine\n 5│Inverse Cosine\n 6│Inverse Tangent\n  ├────────────────\n 7│Hyperbolic Sine\n 8│Hyperbolic Cosine\n 9│Hyperbolic Tangent\n10│Hyperbolic Inverse Sine\n11│Hyperbolic Inverse Cosine\n12│Hyperbolic Inverse Tangent\n  ├────────────────\n13│Back to Main Menu\n")
        if submode == '1':
            a = float(input("Enter angle in degrees: "))
            if a == 30:
                result = 0.5
            elif a == 45:
                result = "1/√2"
            elif a == 60:
                result = "√3/2"
            else:
                a = math.radians(a)
                result = round(math.sin(a), 5)
            print("result:", result)
            endfunc()
        elif submode == '2':
            a = float(input("Enter angle in degrees: "))
            if a == 30:
                result = "√3/2"
            elif a == 45:
                result = "1/√2"
            elif a == 60:
                result = 0.5
            else:
                a = math.radians(a)
                result = round(math.cos(a), 5)
            print("result:", result)
            endfunc()
        elif submode == '3':
            a = float(input("Enter angle in degrees: "))
            if a == 30:
                result = "1/√3"
            elif a == 45:
                result = 1
            elif a == 60:
                result = "√3"
            else:
                a = math.radians(a)
                result = round(math.tan(a), 5)
            print("result:", result)
            endfunc()
        elif submode == '4':
            a = float(input("Enter number: "))
            if a == 0.5:
                result = 30
            else:
                a = math.asin(a)
                result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '5':
            a = float(input("Enter number: "))
            if a == 0.5:
                result = 60
            else:
                a = math.acos(a)
                result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '6':
            a = float(input("Enter number: "))
            if a == 1:
                result = 45
            else:
                a = math.atan(a)
                result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '7':
            a = float(input("Enter angle in degrees: "))
            a = math.radians(a)
            result = round(math.sinh(a), 5)
            print("result:", result)
            endfunc()
        elif submode == '8':
            a = float(input("Enter angle in degrees: "))
            a = math.radians(a)
            result = round(math.cosh(a), 5)
            print("result:", result)
            endfunc()
        elif submode == '9':
            a = float(input("Enter angle in degrees: "))
            a = math.radians(a)
            result = round(math.tanh(a), 5)
            print("result:", result)
            endfunc()
        elif submode == '10':
            a = float(input("Enter number: "))
            a = math.asinh(a)
            result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')
            endfunc()
        elif submode == '11':
            a = float(input("Enter number: "))
            a = math.acosh(a)
            result = round(math.degrees(a), 2)
            print("Angle:", str(result) + '°')

            endfunc()
        elif submode == '12':
            a = float(input("Enter number: "))
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
            while True:
                a = input("Enter number of items: ")
                if not a.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    a = int(a)
                    break
            result = bin(a)[2:]
            print("result:", result)
            endfunc()
        elif submode == '2':
            while True:
                a = input("Enter number of items: ")
                if not a.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    a = int(a)
                    break
            result = hex(a)[2:]
            print("result:", result)
            endfunc()
        elif submode == '3':
            a = input("Enter number to be converted: ")
            result = int(a, 2)
            print("result:", result)
            endfunc()
        elif submode == '4':
            a = input("Enter number to be converted: ")
            a = int(a, 2)
            result = hex(a)[2:]
            print("result:", result)
            endfunc()
        elif submode == '5':
            a = input("Enter number to be converted: ")
            result = int(a ,16)
            print("result:", result)
            endfunc()
        elif submode == '6':
            a = input("Enter number to be converted: ")
            a = int(a ,16)
            result = bin(a)[2:]
            print("result:", result)
            endfunc()
        elif submode == '7':
            clearscreen()
            continue
    elif mainmode == '6':
        submode = input("\n1│Compound Interest - Total Amount\n2│Compound Interest - Interest\n3│Area of Triangle\n4│Area of Circle\n ├────────────────\n5│Back to Main Menu\n")
        if submode == '1':
            a = float(input("Enter original amount: "))
            b = float(input("Enter interest rate: "))
            c = float(input("Enter number of terms used: "))
            result = a * ((1 + (b / 100)) ** c)
            print("total amount: $" + str(round(result, 2)))
            endfunc()
        elif submode == '2':
            a = float(input("Enter original amount: "))
            b = float(input("Enter interest rate: "))
            c = float(input("Enter number of terms used: "))
            result = (a * ((1 + (b / 100)) ** c)) - a
            print("interest: $" + str(round(result, 2)))
            endfunc()
        elif submode == '3':
            a = float(input("Enter side 1: "))
            b = float(input("Enter side 2: "))
            c = float(input("Enter angle between sides in degrees: "))
            c = math.radians(c)
            result = (a * b * math.sin(c))/ 2
            print("Area: ", round(result, 5))
            endfunc()
        elif submode == '4':
            a = float(input("Enter radius: "))
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
            print("Mean:", result)
            endfunc()
        elif submode == '2':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            result = statistics.median(data)
            print("Median:", result)
            endfunc()
        elif submode == '3':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            try:
                result = statistics.mode(data)
                print("Mode:", result)
            except statistics.StatisticsError:
                result = 0
                print("There is no mode.")
            endfunc()
        elif submode == '4':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            a = input("Is this a sample or the entire population?\n1│Sample\n2│Population\n")
            if "sample" in a.lower() or a == "1":
                try:
                    result = statistics.stdev(data)
                    print("Standard Deviation:", result)
                except statistics.StatisticsError:
                    result = 0
                    print("There is no Standard Deviation")
            elif "population" in a.lower() or a == '2':
                try:
                    result = statistics.pstdev(data)
                    print("Standard Deviation:", result)
                except statistics.StatisticsError:
                    result = 0
                    print("There is no Standard Deviation.")
            else:
                print("Error: not valid function")
            endfunc()
        elif submode == '5':
            data = list(map(float, input("Enter numbers separated by spaces: ").split()))
            a = input("Is this a sample or the entire population?\n1│Sample\n2│Population\n")
            if "sample" in a.lower() or a == '1':
                try:
                    result = statistics.variance(data)
                    print("Variance:", result)
                except statistics.StatisticsError:
                    result = 0
                    print("There is no Variance.")
            elif "population" in a.lower() or a == '2':
                try:
                    result = statistics.pvariance(data)
                    print("Variance:", result)
                except statistics.StatisticsError:
                    result = 0
                    print("There is no Variance.")
            else:
                print("Error: not valid function")
            endfunc()
        elif submode == '6':
            clearscreen()
            continue 
        else:
            print("Error: not valid function")
    elif mainmode == '8':
        submode = input("\n1│Random Floating Point\n2│Random Integers\n ├────────────────\n3│Back to Main Menu\n")
        if submode == '1':
            while True:
                c = input("Enter number of numbers needed: ")
                if not c.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    c = int(c)
                    break
            while True:
                a = input("Enter minimum: ")
                if not a.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    a = int(a)
                    break
            while True:
                b = input("Enter maximum: ")
                if not b.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    b = int(b)
                    break
            for i in range(c):
                result = random.uniform(a, b)
                print(str(i+1) + "|" + str(result))
            endfunc()
        elif submode == '2':
            while True:
                c = input("Enter number of numbers needed: ")
                if not c.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    c = int(c)
                    break
            while True:
                a = input("Enter minimum: ")
                if not a.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    a = int(a)
                    break
            while True:
                b = input("Enter maximum: ")
                if not b.isdecimal():
                    print("Invalid input. Number must be an integer.")
                else:
                    b = int(b)
                    break
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

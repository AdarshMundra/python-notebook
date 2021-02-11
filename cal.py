'''
Try to calculatr
'''
FIRST = int(input("Enter first number"))
SECOND = int(input("Enter second number"))
OP = input("Enter symbol")
if OP == '+':
    TOTAL = FIRST + SECOND
    print("The Sum is")
elif OP == '-':
    TOTAL = FIRST - SECOND
    print("The Difference is")
elif OP == '*':
    TOTAL = FIRST * SECOND
    print("The Multiplication is")
elif OP == '/':
    try:
        TOTAL = FIRST / SECOND
        print("The Division is")
    except TypeError:
        print("The denominator is zero")
print(TOTAL)

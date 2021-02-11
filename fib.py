'''
Enter a number to find the fibonnaci u to the number
'''

TOTAL = int(input("Enter a number to find fiboonaci"))
FIRST = 0 #first number

SECOND = 1 #Second number
'''
The generated series
'''
print("fibonacci series")
print(FIRST, ",", SECOND, end=", ")
for i in range(2, TOTAL):
    Next = FIRST + SECOND #the next number
    print(Next, end=", ")
    FIRST = SECOND
    SECOND = Next

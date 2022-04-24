print('CALCULATOR IN THE PYTHON')
# ===================================================== THIS IS MY Calculator
numOne = int(input('Enter Any Number '))
numTwo = int(input('Enter 2nd number '))
# print(numTwo+numOne)
opt = input('Arithmetic operator ')

if opt == "+":
    result = str(numTwo + numOne)
    print('Sum of Two Numbers (1 and 2) ' + result)
elif opt == '-':
    print('Subtracted ' + str(numOne - numTwo))
elif opt == '*':
    print('Multiplication ' + str(numOne * numTwo))
elif opt == '/':
    print('Division ' + str(numOne / numTwo))
elif opt == '%':
    print('Remainder ' + str(numOne % numTwo))
else:
    print('Invalid Input')

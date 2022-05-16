print('SIMPLE CALCULATOR USING THE PYTHON')
numOne = int(input('Enter Any Number '))
numTwo = int(input('Enter 2nd number '))
opt = input('Arithmetic operator ')

if opt == "+":
    result = str(numTwo + numOne)
    print('Sum is  ' + result)
elif opt == '-':
    print('Subtracted  ' + str(numOne - numTwo))
elif opt == '*':
    print('Multiplication  ' + str(numOne * numTwo))
elif opt == '/':
    print('Division  ' + str(numOne / numTwo))
elif opt == '%':
    print('Remainder  ' + str(numOne % numTwo))
else:
    print('Invalid Input')

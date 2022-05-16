print('Day TWO Challenge!!!')
welcome = 'Welcome to the Tip Calculator'
welcome = welcome.upper()
print(welcome)
bill = float(input('What is the Total Bill? $ '))
people = int(input('How many people to Split the Bill? '))
tip = int(input('What Percentage should you pay ?10, 12 or 15? '))
billWithTip: float = (tip / 100 * bill) + bill
billPerPerson: float = billWithTip / people
finalAmount = round(billPerPerson, 2)
final_amount = "{:.2f}".format(billPerPerson)  # this is how we can use round of function to get exact format
tip = tip / 100 * bill
print(f'This is the Tip ${tip}')
print(f'Actual Total Bill is ${bill}')
print(f'Total Bill with Tip is ${billWithTip}')
print(f"Each person Should Pay ${final_amount}")

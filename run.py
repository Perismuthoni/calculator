from calculator import Calculator

choice = input('What oparation do want to run : \n 1 for Add, \n 2 for substract:  \n 3 for multiply: \n 4 for division: \n Enter here:  ')

num_one = input('Enter 1st number:   ')
num_two = input('Enter 2nd number:   ')

oparation = Calculator(num_one, num_two)

if choice == '1':
    res = oparation.add()
elif choice == '2':
    res = oparation.sub()
elif choice == '3':
    res = oparation.mul()
elif choice == '4':
    res = oparation.div() 
else:
    res = None
    print('invalid choice') 
print(f'The answer is: {res}')


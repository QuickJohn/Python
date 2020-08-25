# Author: John Quick
# Recursion demonstration

def main():
    
    print()
    print('RECURSION WITH PYTHON')
    print('Choose option:')
    print('[1] Find factorial')
    print('[2] Convert to binary')
    print('[3] Fibonacci')
    print()

    # get choice from user
    option = int(input('Pick option: \n'))
    # get number from user
    n = int(input('\nEnter a number: '))

    # determine choice
    if option < 0 | option > 3:
        print('Choose an option 1 - 3!')
    else: 
        if option == 1:
            print(factorial(n))
        elif option == 2:
            print(n,'in binary is')
            decimalToBinary(n)
        elif option == 3:
            print('Fibonacci sequence: ')
            for i in range(n):
                print(fibonacci(i))
        
        #print(fibonacci(n))

# calculate factorial function
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1) 

# convert to binary function
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
        print(num % 2, end='')

# Fibinocci function
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# call main function
main()

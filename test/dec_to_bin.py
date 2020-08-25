def binary_to_decimal(num):
    if not num:
        return 0
    return binary_to_decimal(num[:-1]) * 2 + int(num[-1])

# Test
number = int(input("Enter a number: "))

for i in range(number):
    b = format(i, '05b')
    n = binary_to_decimal(b)
    print('{:2} {:4} -> {}'.format(i, b, n)) 

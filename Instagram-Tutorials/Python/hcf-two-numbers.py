# Highest Common Factor of Two Numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def hcf(num1 , num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1

    for i in range(1 , smaller + 1):
        if((num1 % i == 0) and (num2 % i == 0)):
            factor = i
    return factor

print(f'The HCF of {num1} and {num2} is {hcf(num1 , num2)}')
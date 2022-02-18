# Finding Lowest Common Multiple of Two Numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def lcm(num1 , num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True: 
        if(greater % num1 == 0) and (greater % num2 == 0):
            break
        greater == 1
    return greater

print(f'The LCM of {num1} and {num2} is {lcm(num1, num2)}')
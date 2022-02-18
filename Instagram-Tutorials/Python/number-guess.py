import random

print("Welcome to the number guessing game!")

def guess_number():
    number = random.randint(1 , 100)
    chances = 0
    times = int(input("How many chances do you want to guess the number?: "))
    print("Guess the number between 1 and 100.")

    while chances < times:
        guess = int(input("Guess the number: "))

        if guess == number:
            print("You guessed the correct number!")
            break
        elif guess < number:
            print("Your guess is too low.")
            chances += 1
        else:
            print("Your guess is too high.")
            chances += 1

    if not chances < times:
        print("You have used all your chances.")
        print("The number was" , number)

guess_number()
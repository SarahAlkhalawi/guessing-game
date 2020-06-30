import random

number = random.randint(1, 20)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 20: "))

    if (guess < number):
        print("The number is greater than your number. Try again")
    elif (guess > number):
        print("The number is smaller than your number. Try again")
    else:
        print("This is the number!")
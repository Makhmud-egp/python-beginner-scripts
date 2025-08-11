import random

number = random.randint(1, 10)

attempts = 0 # to track the total attempts

while True:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print(''.join(["*" for _ in range(30)]))
        print("Correct!")
        print(f"Your total attempts: {attempts}.")
        break

    elif number > guess:
        if number - guess < 3:
            print("Close! But it`s a bit higher.")
        else:
            print("Too low!")
    else:
        if guess - number < 3:
            print("Close! But it`s a bit lower.")
        else:
            print("Too high!")


print("Thank you for partisparting!")
print("*" * 30)

# math_quiz.py
import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
ans = int(input(f"What is {num1} + {num2}? "))

if ans == num1 + num2:
    print("Correct!")
else:
    print("Oops! Try again.")

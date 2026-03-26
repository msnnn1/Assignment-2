import random

dice = random.randint(1, 6)
guess = int(input("Guess the dice (1-6): "))

print("Dice value:", dice)

if guess == dice:
    print("😊")
elif abs(guess - dice) == 1:
    print("😐")
else:
    print("😢")
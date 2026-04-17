import random

dice = random.randint(1, 6)
guess = int(input("Guess the dice (1-6): "))

if guess < 1 or guess > 6:
    print("Please guess between 1 and 6 next time!")

print("Dice value:", dice)

if guess == dice:
    print("😊")
elif abs(guess - dice) == 1:
    print("😐")
else:
    print("😢")
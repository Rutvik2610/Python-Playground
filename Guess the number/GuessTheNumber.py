import random
from Art import logo

print(logo)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 to 100.\nGuess what it is.")
choice = input("Choose the difficulty. Type 'easy or 'hard: ").lower()
if choice == 'easy':
    lives = 10
else:
    lives = 5

random_number = random.randint(1, 100)

while lives != 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess:"))

    if user_guess == random_number:
        print(f"You got it! The answer was {user_guess}.")
        break
    elif user_guess < random_number:
        lives -= 1
        print("Too low.")
    elif user_guess > random_number:
        lives -= 1
        print("Too high.")
    if lives == 0:
        print("You have run out of guesses. You lose")
    elif user_guess != random_number and lives != 0:
        print("Guess again")


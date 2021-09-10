import random
from Art import stages, logo
from WordList import word_list

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

lives = 6
end_of_game = False
status = "You Lose!"
print(logo)

#Use this for testing
#print(f'Pssst, the solution is {chosen_word}.')

while not end_of_game:
    user_input = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if user_input == display[i]:
            print("You have already guessed this letter.")
            break
        elif user_input == chosen_word[i]:
            display[i] = user_input
    if user_input not in chosen_word:
        print(f"You guessed {user_input}, it is not in the word. You lose a life.")
        # print(stages[lives])
        lives -= 1

    # if user_input in display:                                   There is a bug. This code doesn't work
    #     print("You have already guessed this letter.")           if there are multiple same letters in the word
    # elif user_input in chosen_word:
    #     display[chosen_word.find(user_input)] = user_input
    # elif user_input not in chosen_word:
    #     print(f"You guessed {user_input}, it is not in the word. You lose a life.")
    #     print(stages[lives - 1])
    #     lives -= 1
    if lives < 6:
        print(stages[lives+1])
    print(f"{' '.join(display)}")
    if lives == 0:
        end_of_game = True
    elif display.count("_") == 0:
        status = "You Win!"
        end_of_game = True

print(status)


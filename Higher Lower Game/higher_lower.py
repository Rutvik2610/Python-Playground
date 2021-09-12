import random
from art import logo, vs
from game_data import data


def pick_entity():
    """Picks a random item from the list of dictionary"""
    return random.choice(data)


def check_answer(first_entity, second_entity, choice):
    """Checks the user's answer. Returns True if correct else returns False"""
    if first_entity["follower_count"] > second_entity["follower_count"] and choice == "A":
        return True
    elif first_entity["follower_count"] < second_entity["follower_count"] and choice == "B":
        return True
    else:
        return False


def play_game():
    """The higher lower game. Guess who has more followers on Instagram"""
    is_guess = True
    score = 0
    print(logo)
    entity1 = pick_entity()
    entity2 = pick_entity()
    while entity1 == entity2:
        entity2 = pick_entity()

    while is_guess:
        print(f"Compare A: {entity1['name']}, a {entity1['description']}, from {entity1['country']}")
        print(vs)
        print(f"Against B: {entity2['name']}, a {entity2['description']}, from {entity2['country']}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if check_answer(entity1, entity2, user_choice):
            score += 1
            print(f"You are right! Current Score: {score}")
            entity1 = entity2
            entity2 = pick_entity()
        else:
            print(f"Sorry you are wrong! Final Score: {score}")
            is_guess = False


play_game()

import random
from Art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
player_cards = []


def deal_cards(deal_player, num_of_cards):
    for i in range(num_of_cards):
        if deal_player:
            player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))


def calculate_score(card_list):
    score = sum(card_list)
    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return score


def compare_score(player_socre, dealer_score):
    if player_socre == dealer_score:
        return "Draw"
    elif dealer_score == 21:
        return "Opponent has a Blackjack. You Lose!"
    elif player_socre == 21:
        return "You won with a Blackjack"
    elif player_socre > 21:
        return "You went over. You Lose!"
    elif dealer_score > 21:
        return "Dealer went over. You Win!"
    elif player_socre > dealer_score:
        return "You Win!"
    else:
        return "You Lose!"


def play_game():
    print(logo)
    deal_cards(True, 2)
    print(f'Your cards are: {player_cards}. The current score is: {calculate_score(player_cards)}')
    print(f'Dealer\'s first card is: {dealer_cards[0]}')
    while calculate_score(player_cards) < 21 and calculate_score(dealer_cards) < 21:
        continue_dealing = input("Type 'y' to Hit or 'n' to Stand: ").lower()
        if continue_dealing == 'y':
            deal_cards(True, 1)
        else:
            while calculate_score(dealer_cards) < 17:
                deal_cards(deal_player=False, num_of_cards=1)
            break

    print(f"Your final hand: {player_cards}, Your final score: {calculate_score(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, Dealer's final score: {calculate_score(dealer_cards)}")
    print(compare_score(calculate_score(player_cards), calculate_score(dealer_cards)))

    
play_game()

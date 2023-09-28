import random
import os
import time


cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}

def deal_cards(user_hand:list):

    for i in range(0, 2):
        card= random.choice(list(cards.keys()))
        user_hand.append(card)


def calculate_total(user_hand:list, user_total:int, computer_hand:list):

    user_total = 0

    for card in user_hand:
        user_total += cards[card]
        

    if "A" in user_hand:
        if user_total > 21:
            user_total = (user_total - 11) + 1
            
    if user_hand == computer_hand:
        print(f"Computer's Hand: {' '.join(user_hand)} - Total: {user_total}")
    else:
        print(f"Player's Hand: {' '.join(user_hand)} - Total: {user_total}")

    return user_total

def has_busted(user_total:int):
    if user_total > 21:
        return True

    return False

def display_dealer_first_hand(user_hand:list, user_total:int):

    user_total = cards[user_hand[0]]

    print(f"Computer's Hand: {user_hand[0]} ? - Total: {user_total}")

    return user_total


def place_bet(cash:int):

    is_valid_bet = False

    while not is_valid_bet:
        amount = int(input("Place your bet: $ "))
        if amount > cash:
            print("You do not have enough cash")
        else:
            is_valid_bet = True

    return amount


def is_player_turn(user_hand:list, user_total:int):

    if has_busted(user_total):
        return False

    player_input = input("What would you like to do? Type 'H' for Hit, Type 'S' for Stand: ").lower()

    if player_input == "h":
        card= random.choice(list(cards.keys()))
        user_hand.append(card)
        return True
    
    return False


def computer_ai(user_hand:list, user_total:int):

    if has_busted(user_total):
        return False

    if user_total >= 17:
        return False
    
    card= random.choice(list(cards.keys()))
    time.sleep(3)
    user_hand.append(card)

    return True


def pay_out(player_total:int, computer_total:int, winnings:int):

    if has_busted(player_total) and has_busted(computer_total):
        print(f"Push: ${winnings}")
        return winnings
    
    if has_busted(player_total):
        print(f"You lost {winnings}")
        return -winnings

    if player_total == computer_total:
        print(f"Push: ${winnings}")
        return winnings

    if player_total < computer_total and has_busted(computer_total):
        print(f"You Won! {winnings}")
        return winnings

    if player_total > computer_total:
        print(f"You Won! {winnings}")
        return winnings
    
    print(f"You lost {winnings}")
    return -winnings


def game():

    is_playing = True
    cash = 100

    while is_playing:

        computer_hand = []
        player_hand = []
        player_total = 0
        computer_total = 0

        os.system('cls')
        print(f"${cash}")
        potential_winnings = place_bet(cash)

        os.system('cls')
        print(f"${cash - potential_winnings}")

        deal_cards(player_hand)
        deal_cards(computer_hand)

        player_total = calculate_total(player_hand, player_total, computer_hand)
        computer_total = display_dealer_first_hand(computer_hand, computer_total)
        
        while is_player_turn(player_hand, player_total):
            player_total = calculate_total(player_hand, player_total, computer_hand)
            os.system('cls')
            print(f"${cash - potential_winnings}")
            calculate_total(player_hand,player_total, computer_hand)
            display_dealer_first_hand(computer_hand, computer_total)
        
        os.system('cls')
        print(f"${cash - potential_winnings}")
        calculate_total(player_hand, player_total, computer_hand)
        computer_total = calculate_total(computer_hand, player_total, computer_hand)
        
        while computer_ai(computer_hand, computer_total):
            os.system('cls')
            print(f"${cash - potential_winnings}")
            calculate_total(player_hand, player_total, computer_hand)
            computer_total = calculate_total(computer_hand, computer_total, computer_hand)
        time.sleep(1)
        cash += pay_out(player_total, computer_total, potential_winnings)
        time.sleep(1)
        
        
game()

import random

def rand_card():
    suits = ["hearts", "diamonds", "clubs", "spades"]
    cards = ["ace", "2", "3", "4", "5", "6", "7", "8",
             "9", "10", "jack", "queen", "king"]
    fcards = [card + " of " + suit for card in cards for suit in suits]

    return random.choice(fcards)

def card_to_num(card):
    num = card.split(" ")[0]
    if not num.isdigit():
        if num == "jack":
            num = 11
        elif num == "queen":
            num = 12
        elif num == "king":
            num = 13
        elif num == "ace":
            num = 14
    return int(num)

while True:
    card = rand_card()
    num = card_to_num(card)
    guess = input("Current card is " + card + ".\nWill the next be higher or lower?\n")
    next_card = rand_card()
    next_num = card_to_num(next_card)
    if ((guess == "higher") and (next_num > num)) or ((guess == "lower") and (next_num < num)):
        print("You win, the next card was " + next_card)
    else:
        print("Incorrect, the next card was " + next_card)
        break

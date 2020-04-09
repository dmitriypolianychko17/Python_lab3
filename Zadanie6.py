import random
def deck():
    range = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    color = ['c', 'd', 'h', 's']
    deck = []
    for a in range:
        for b in color:
            deck.append((a,b))
    return deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return tuple(deck)

def deal(deck,n):
    list = []
    for i in range(0, 5 * n, 5):
        list.append(deck[i:i + 5])
    return list
print(deck())
print(shuffle_deck(deck()))
print(deal(deck(), 3))

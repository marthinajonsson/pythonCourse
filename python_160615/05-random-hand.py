import random

suits = ["clubs", "diamonds", "hearts", "spades"]

ranks = [
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    "jack", "queen", "king", "ace"
]

deck = ["{0} of {1}".format(r, s) for s in suits for r in ranks]
random.shuffle(deck)

hand = random.sample(deck, 5)

print(hand)
from random import randint

cards = list(range(1,33))
print(cards)

for i in range(-1, 0, -1):
    rand = randint(0,i)
    cards[i], cards[rand] = cards[rand], cards[i]
    print(cards)
from random import randint

cards = list(range(1,33))
shuffled = []
print(cards)

randint(0,len(cards)-1)
while cards:
    shuffled.append(cards.pop(range(0,len(cards)))-1)
print(cards)
print(shuffled)
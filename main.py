import random

class card:
    def __init__(self,rank,color):
        self.rank = rank
        self.color = color
    def __str__(self):
        return f"{self.rank} {self.color}"

rank = ['2','3','4','5','6','7','8','9','10', 'jack','queen', 'king', 'ace']
colors = ['BlackHeart','RedClub','BlackDiamond','RedSpade']
cards = []
for i in rank:
    for j in colors:
        cards.append(card(i,j))
print(cards[0]) #calling __str__ only of object of the class card and only when printing or converting on text
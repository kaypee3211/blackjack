import random

#do with money

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
#print(cards[0]) #calling __str__ only of object of the class card and only when printing or converting on text
count_ace = 0
def count_points(cards,points):
    points = 0
    for i in range(len(cards)):
        x = str(cards[i])
        x = x.split(' ')
        if x[0] in ('jack', 'queen', 'king'):
            points += 10
        elif x[0] != 'ace':
            points += int(x[0])
        elif x[0] == 'ace':
            continue
    return points

def how_many_aces(cards,count_ace):
    for i in range(len(cards)):
        x = str(cards[i])
        x = x.split(' ')
        if x[0] == 'ace':
            count_ace = count_ace + 1
        return count_ace

move = ''
while move != 'stand':
        player_score = 0
        casino_score = 0

        player_cards = []
        number = random.randint(0, 51)
        player_cards.append(cards[number])
        number = random.randint(0, 51)
        player_cards.append(cards[number])
        print('This is your cards:')
        print(player_cards[0])
        print(player_cards[1])

        casino_cards = []
        number = random.randint(0, 51)
        casino_cards.append(cards[number])
        number = random.randint(0, 51)
        casino_cards.append(cards[number])
        print('------------------------')
        print("First card reveal:")
        print(casino_cards[0])
        print('------------------------')
        choice = ''
        print('Whats your choice?')
        move = str(input())

        if move == 'stand':
            move = 'stand'
            #player_score = count_points(player_cards, player_score)

        elif move == 'hit':
            while move == 'hit' and count_points(player_cards,player_score) <= 21:
                number = random.randint(0, 51)
                player_cards.append(cards[number])
                print(f"Your card: {cards[number]}")
                print('Whats your choice?')
                move = str(input())

        #adding cards for casyno
        if count_points(casino_cards, casino_score) <= 16:
            number = random.randint(0, 51)
            casino_cards.append(cards[number])

        print('------------------------')
        print("Second card reveal:\n")
        print(casino_cards[1])
        print('Player cards:')
        print('########################')
        for i in range(len(player_cards)):
            print(player_cards[i])
        print('########################')
        print('-------------------')
        print('Casino cards:')
        print('########################')
        for i in range(len(casino_cards)):
            print(casino_cards[i])
        print('########################')


        player_score = count_points(player_cards, player_score)
        casino_score = count_points(casino_cards, casino_score)
        count_ace = how_many_aces(player_cards,count_ace)
        #@print(count_ace)
        print(f"Your score: {player_score}")
        print(casino_score)

        if player_score <= 21 and abs(21 - player_score) < abs(21 - casino_score):
            print('You won!!!')
        else:
            print('You lost!!!')
        break



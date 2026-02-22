import random
from money import money


# double down
# split
# add to payofdebt


class card:
    def __init__(self,rank,color):
        self.rank = rank
        self.color = color
    def __str__(self):
        return f"{self.rank} {self.color}"

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


def points_for_aces(x_ace, x_score):
    while x_ace > 0:
        if x_score + 11 + (x_ace-1) <= 21:
            x_score += 11
        else:
            x_score += 1
        x_ace = x_ace - 1
    return x_score


def hit():
    print("How much money on this bet?")
    y = int(input())
    while y > player.all:
        print("You dont have enough money. \n 1.New bet \n 2.Take debt")
        x = int(input())
        if x == 2:
            print('How much do you wanna take money for debt?')
            player.addDebt(int(input()))
        print('Place new bet:')
        y = int(input())
    return y

rank = ['2','3','4','5','6','7','8','9','10', 'jack','queen', 'king', 'ace']
colors = ['BlackHeart','RedClub','BlackDiamond','RedSpade']
t = []
for i in rank:
    for j in colors:
        t.append(card(i,j))
#print(cards[0]) #calling __str__ only of object of the class card and only when printing or converting on text
count_ace = 0

print('How much money do you wanna play for?')
x = int(input())
player = money(x, 0)
debt = player.debt = 0

rounds = 0
do_we_play = 1
while do_we_play == 1:
    round += 1
    cards = t.copy()
    random.shuffle(cards)
    player_score = 0
    casino_score = 0

    round_value = hit()

    player_cards = []
    number = random.randint(0, len(cards) -1)
    player_cards.append(cards[number])
    cards.pop(number)

    number = random.randint(0, len(cards) -1)
    player_cards.append(cards[number])
    cards.pop(number)

    print('This is your cards:')
    print(player_cards[0])
    print(player_cards[1])

    casino_cards = []
    number = random.randint(0, len(cards) -1)
    casino_cards.append(cards[number])
    cards.pop(number)

    number = random.randint(0, len(cards) -1)
    casino_cards.append(cards[number])
    cards.pop(number)

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

        while move == 'hit':
            number = random.randint(0, len(cards) -1)
            player_cards.append(cards[number])
            print(f"Your card: {cards[number]}")
            cards.pop(number)

            player_score = count_points(player_cards,0)
            aces = how_many_aces(player_cards,0)
            player_score = points_for_aces(aces,player_score)
            print('Current points:')
            print(player_score)
            if player_score > 21:
                print('You lost!')
                player.all -= round_value
                break

            print('Whats your choice?')
            move = str(input())



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


    player_score = count_points(player_cards, 0)
    casino_score = count_points(casino_cards, 0)
    #@print(count_ace)


    players_ace = how_many_aces(player_cards,0)
    casino_ace = how_many_aces(casino_cards,0)



    player_score = points_for_aces(players_ace,player_score)
    casino_score = points_for_aces(casino_ace,casino_score)

    #adding cards for casino
    while casino_score <= 16:
        number = random.randint(0, len(cards)-1)
        casino_cards.append(cards[number])
        cards.pop(number)
        casino_ace = how_many_aces(casino_cards, 0)
        casino_score = count_points(casino_cards, 0)
        casino_score = points_for_aces(casino_ace, casino_score)

    print(f"Your score: {player_score}")
    print(f"Casino score: {casino_score}")
    if casino_score > 21:
        print('You won!!!')
        player.all += round_value

    elif player_score > 21:
        print('You lost!!!')
        player.all -= round_value

    elif player_score == casino_score:
        print("Draw")

    elif (21-player_score) < (21-casino_score):
        print('You won!!!')
        player.all += round_value

    elif (21 - player_score) > (21 - casino_score):
        print('You lost!!!')
        player.all -= round_value


    print(f'Your money: {player.all}')
    print(f'Your debt: {player.debt}')



    if rounds % 5 == 0 and player.debt > 0:
        print('You need to pay your debt to continue playing:')
        if player.all >= player.debt:
            print('Paying off debt with your money...')
            player.payOffDebt(player.debt)
        else:
            print(f'You have {player.debt} debt. Go to work to pay it off')
            print(f'Your debt {player.debt}')
            do_we_play = 2
    else:
        print('Do you want another round? \n 1. Yes \n 2. No')
        do_we_play = int(input())

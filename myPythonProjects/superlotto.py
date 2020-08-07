
jackpot = 23000000
jackpot = float(jackpot)


oddsOfWinning = 1/41416353
oddsOfLoosing = (41416353-1)/41416353
expectedValue = jackpot * oddsOfWinning - (1* oddsOfLoosing)
print('Expted Value :', expectedValue)


def generateDraw():
    import random

    balls = list()
    for i in range(5):
        x = random.randint(1,47)
        balls.append(x)
    print(balls)
    x = random.randint(1,27)
    print('Power ball :', x)
    balls.append(x)
    return balls

def superlotto(draw, balls):
    winnings = 0
    matches = 0
    mega = balls[5] == draw[5]
    print(mega)
    #[:5] ommiting last ball which is powerball
    for d in draw[:4]:
        if d not in balls[:4]:
            print('no match, you lose $1')
            return False
            break
        elif d in balls:
            matches = matches + 1
        if mega:
            winnings = 1
        elif matches == 1 and mega:
            winnings = 2
        elif matches == 2 and mega:
            winnings = 10
        elif matches == 3:
            winnings = 10
        elif matches == 3 and mega :
            winnings = 56
        elif matches == 4:
            winnings = 95
        elif matches == 4 and mega :
            winnings = 1170
        elif matches == 5:
            winnings = 14820
        elif matches == 5 and mega :
            winnings = 23000000
    print('you won', winnings)
    return True

draw = generateDraw()
balls = generateDraw()

superlotto(draw, balls)


jackpot = input('enter jackpot : ')
jackpot = float(jackpot)

cost = float(input('cost of ticket : '))

oddsOfWinning = 1/292201338
oddsOfLoosing = (292201338-1)/292201338
expectedValue = jackpot * oddsOfWinning - (cost* oddsOfLoosing)
print('Expted Value :', expectedValue)


import random

balls = list()
for i in range(5):
    x = random.randint(1,69)
    balls.append(x)
print(balls)
x = random.randint(1,26)
print('Power ball :', x)

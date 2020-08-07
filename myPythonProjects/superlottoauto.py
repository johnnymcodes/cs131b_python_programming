import random
def superlotto(draw, balls):
    winnings = 0
    matches = 0
    mega = balls[5] == draw[5]
    #[:5] ommiting last ball which is powerball
    for d in draw[:4]:
        if d not in balls[:4]:
            break
        elif d in balls:
            matches = matches + 1
    if mega == False and (matches in [0, 1, 2]):
        return False
    if mega and (matches in [0, 1, 2]):
        return False
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

def generateDraw():
    import random

    balls = list()
    for i in range(5):
        x = random.randint(1,47)
        balls.append(x)
    x = random.randint(1,27)
    balls.append(x)
    return balls

# draw = generateDraw()
#
# print('draw :', draw)
# n = 0
# condition = False
# while condition  == False:
#     balls = generateDraw()
#     n = n + 1
#     condition = superlotto(draw, balls)
# print('winnings balls:' , balls)
# print('Number of tries :', n)

tries = 10
condition = False
while tries < 10 or condition == False:
    num = 0
    balls = generateDraw()
    draw = generateDraw()
    num = num + 1
    tries = num
    condition = superlotto(draw, balls)
print('your balls:', draw)
print('winnings balls:' , balls)
print('Number of tries :', num)

#There is a conditional execution structure built into Python to handle expected and unexpected errors called "try/except"

# inp = input('Enter Farenheit Temperature: ')
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0/9.0
#     print(cel)
# except:
#     print('Please enter a number')

#3.8 short-circuit evaluation of logical expressions
#When the evaluation of a loigical expression stops because
#the overall value is already known, it is called short-circuiting the evaluation.

#3.11 1 - Rewrite your pay computation to give employee 1.5 times the hourly rate for hours worked above 40 hours

# hours = input('Enter Hours worked : ')
# rate = input('Enter Rate: ')
# try: #handle non-numeric input
#     int(hours)
#     int(rate)
#     overtime = 0.0
#     overtimePay = 1.5 * rate;
#     if hours > 40:
#         overtime = hours - 40
#         hours = 40
#     pay = rate * hours + overtimePay * overtime
#     print('pay : ', pay)
# except: # handle non numeric input
#     print('Please enter a number')


#3.11 ex3 prompt for a score between 0.0 and 1.0 if the score
# is out of rance, print an error.

score = input('Enter Score : ')
try:
    int(score)
    if score > 1.0 or score < 0.0:
        print('Bad Score')
    else:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('A')
except:
    print(' Bad Score')

import random;

def rolld20():
    return random.randint(1,20)

def roll():
    outcome = rolld20()

    if ((1 < outcome) & (outcome < 10)):
        print('This was bad. This was your roll: ' + str(outcome))
    elif((10 <= outcome) & (outcome < 20)):
        print('This was good. This was your roll: ' + str(outcome))
    elif(outcome == 1):
        print('Oh No. Crtical Miss. Your roll was 1.')
    else:
        print('You are a lucky bastard. You had a lucky 20.')

roll()


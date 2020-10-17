import random

# event functions
def wheel_of_fortune():
    contestants_list_1 = contestants_list
    points_1 = dict()
    number_of_contestants_1 = len(contestants_list_1)
    contestants_eliminated_1 = 1
    starting_number_1 = 100 * number_of_contestants_1
    x_1 = 1
    contestant_points_1 = dict()
    while x_1 <= number_of_contestants_1:
        # append points to dictionary
        points_1.update({x_1: starting_number_1})
        # increase x by 1
        x_1 += 1
        starting_number_1 -= 21
        print(points_1)
    while contestants_eliminated_1 <= number_of_contestants_1:
        eliminated_one_1 = random.choice(contestants_list_1)
        contestants_list_1.pop(contestants_list_1.index(eliminated_one_1))
        contestant_points_1.update({eliminated_one_1: points_1.get(contestants_eliminated_1)})
        # increase contestants_eliminated
        contestants_eliminated_1 += 1
        print(contestant_points_1)




# main body
print('Welcome to the RV Automator.')
print('What do you want to do?')
print('''
1. The automator(dur)
2. How to use
3. Credits
Exit. Exit
''')
answer = input('Please enter a number.')
if answer == "3":
    print('''
    Made by Thecoder3281f#6650. 
    ''')
elif answer == "2":
    print('Type the contestant names, separated by commas. The number of events is equal to the number of contestants.')
    print('All events are elimination except the last three. ')
    print('The first 3 events will have no elimination.')
    print('Following that, the next n events will be triple elimination.')
    print('Then, n-3 events will be double elimination.')
    print('After that, the rest will be single elimination until there are only 3 cotestants left.')
    print('n is the number of contestants divided by 3.')
elif answer == "1":
    contestants = input('Please enter contestants names separated by commas.')
    contestants_list = contestants.split(',')
    wheel_of_fortune()
    previous_event = 1
    # main function
    # ...



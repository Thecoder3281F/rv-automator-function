import random
import copy
from time import sleep
def sorter(the_dict):
    the_dict = sorted(the_dict.items(), key=lambda x: x[1], reverse=True)
    the_dict = dict(the_dict)

def eliminator(points_dict, participants_list):
    if elimination == 0:
        participants_list.sort()
        print(points_dict)
        print('Did not eliminate any contestant.')
        print()
        sleep(1)
    elif elimination == 1:
        participants_list.sort()
        eliminated_first = list(points_dict)[len(points_dict) - 1]
        print(points_dict)
        print()
        points_dict.popitem()
        participants_list.pop()
        sleep(1)
        print(f'Eliminated {elimination} contestant who is {eliminated_first}.')
        print()
        print(points_dict)
        sleep(1)
    elif elimination == 2:
        participants_list.sort()
        eliminated_first = list(points_dict)[len(points_dict) - 1]
        eliminated_second = list(points_dict)[len(points_dict) - 2]
        print(points_dict)
        print()
        points_dict.popitem()
        points_dict.popitem()
        participants_list.pop()
        participants_list.pop()
        sleep(1)
        print(f'Eliminated {elimination} contestants who are {eliminated_second} and {eliminated_first}.')
        print()
        print(points_dict)
        sleep(1)
    elif elimination == 3:
        participants_list.sort()
        eliminated_first = list(points_dict)[len(points_dict) - 1]
        eliminated_second = list(points_dict)[len(points_dict) - 2]
        eliminated_third = list(points_dict)[len(points_dict) - 3]
        print(points_dict)
        print()
        points_dict.popitem()
        points_dict.popitem()
        points_dict.popitem()
        participants_list.pop()
        participants_list.pop()
        participants_list.pop()
        sleep(1)
        print(f'Eliminated {elimination} contestants who are {eliminated_third}, {eliminated_second} and {eliminated_first}.')
        print()
        print(points_dict)
        sleep(1)

# event functions

# wheel of fortune type
def wheel_of_fortune():
    contestant_points = dict()
    contestant_points = copy.deepcopy(contestant_points)
    print()
    print('Wheel of Fortune')
    print('Try to be selected first')
    points = dict()
    number_of_contestants = len(main_contestants_list)
    contestants_selected = 1
    starting_number = 1000
    x = 1
    
    while x <= number_of_contestants:
        # append points to dictionary
        points.update({x: starting_number})
        # increase x by 1
        x += 1
        starting_number -= 21
    while contestants_selected <= number_of_contestants:
        selected_one = random.choice(contestants_list)
        contestants_list.pop(contestants_list.index(selected_one))
        contestant_points.update({selected_one: points.get(contestants_selected)})
        # increase contestants_eliminated
        contestants_selected += 1
        print(f'{selected_one} was chosen. (contestants selected: {contestants_selected - 1})')
        print()
    sorter(contestant_points)
    eliminator(contestant_points, main_contestants_list)

def wheel_of_misfortune():
    print()
    print('Wheel of Misfortune')
    print('Try not to be selected')
    points = dict()
    number_of_contestants = len(main_contestants_list)
    contestants_list = copy.deepcopy(main_contestants_list)
    contestants_list_clone = copy.deepcopy(contestants_list)
    contestants_selected = 1
    starting_number = 1000
    x = 1
    contestant_points = dict()
    while x <= number_of_contestants:
        # append points to dictionary
        points.update({x: starting_number})
        # increase x by 1
        x += 1
        starting_number += 21
    while contestants_selected <= number_of_contestants:
        selected_one = random.choice(contestants_list_clone)
        contestants_list_clone.pop(contestants_list_clone.index(selected_one))
        contestant_points.update({selected_one: points.get(contestants_selected)})
        # increase contestants_eliminated
        contestants_selected += 1
    sorter(contestant_points)
    eliminator(contestant_points, contestants_list)
        

# random number comparison type

def drive_down_the_m6():
    print()
    print('Drive down the M6')
    print('Drive the furthest down the M6 before running out of fuel')
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
    print('After that, the rest will be single elimination until there are only 3 contestants left.')
    print('n is the number of contestants divided by 3.')
elif answer == "1":
    elimination = 0
    current_event = 1
    contestants = input('Please enter contestants names separated by commas.')
    main_contestants_list = contestants.split(',')
    while current_event <= 3:
        contestants_list = copy.deepcopy(main_contestants_list)
        elimination = 1
        wheel_of_fortune()
        # wheel_of_misfortune()
        current_event += 1
    #while current_event <= len(main_contestants_list) / 3:
    #   elimination = 3
        # n events with triple elimination

    #    current_event += 1    
    #while current_event <= len(main_contestants_list) / 3 * 2 - 3:
    #    elimination = 2
        # n-3 events with double elimination

    #    current_event += 1
    #while len(main_contestants_list) != 3:
    #    elimination = 1
        # events until 3 contestants

    #    current_event += 1
    # finale
    # random events
else:
    raise TypeError


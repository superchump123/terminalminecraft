import basic_functions
import json
import random


def help():
    help_list = ['help -- displays this list',
                 'give -- gives an item to the player',
                 'remove -- clears an item slot',
                 'see -- displays the hotbar in all its glory',
                 'add -- add items to an existing slot',
                 'creeper -- special secret command',
                 'random -- adds a random item & random amount to your hotbar',
                 ]
    print('Here are the options:\n')
    for o in sorted(help_list):
        print(o)
    print('\n')


def give(hotbar):
    hotbar_full = basic_functions.check_full(hotbar)

    while not hotbar_full:
        adding_item = input('What item do you want to give? ')
        if adding_item != '':
            break

    while not hotbar_full:
        amount_adding = int(input('How many of that item do you want? '))
        if amount_adding > 0:
            break

    available_slot = basic_functions.get_available_slot(hotbar)
    try:
        hotbar[available_slot]['full'] = True
        hotbar[available_slot]['item_name'] = adding_item
        hotbar[available_slot]['amount'] = amount_adding
    except (IndexError, TypeError):
        hotbar_full = True
        print('\nHotbar is full.  Please enter a different command.')

    for s in hotbar:
        print(s)

    return hotbar


def remove(hotbar):
    to_remove = int(input('what slot do you want to remove? '))
    hotbar[to_remove - 1]['full'] = False
    hotbar[to_remove - 1]['item_name'] = ''
    hotbar[to_remove - 1]['amount'] = 0

    for s in hotbar:
        print(s)


def add(hotbar):
    view_hotbar = False
    while not view_hotbar:
        choice = input('Do you need to see the hotbar first? (y/n) ').lower()
        if choice == 'y' or choice.startswith('y'):
            view_hotbar = True
        else:
            break

    if view_hotbar:
        for s in hotbar:
            print(s)

    to_add = int(input('What slot do you want to add to? ')) - 1
    adding_amount = int(input('How many items to add? '))
    hotbar[to_add]['amount'] += adding_amount

    return hotbar


def random_item(hotbar):
    hotbar_full = basic_functions.check_full(hotbar)

    available_slot = basic_functions.get_available_slot(hotbar)
    with open('items.json', 'r') as file:
        items = json.load(file)
        try:
            hotbar[available_slot]['full'] = True
            hotbar[available_slot]['item_name'] = random.choice(items)
            hotbar[available_slot]['amount'] = random.randint(1, 65)
        except (IndexError, TypeError):
            hotbar_full = True
            print('\nHotbar is full.  Please enter a different command.')

        for s in hotbar:
            print(s)

        return hotbar


def quit():
    return False

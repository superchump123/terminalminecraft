import basic_functions as bf
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
                 'quit -- exit program',
                 'show args -- shows optional cli arguments to use when running program',
                 'move -- moves the items of one slot to different empty slot',
                 ]
    print('Here are the options:\n')
    for o in sorted(help_list):
        print(o)
    print('\n')


def give(hotbar):
    hotbar_full = bf.check_full(hotbar)

    while not hotbar_full:
        adding_item = input('What item do you want to give? ')
        if adding_item != '':
            break

    while not hotbar_full:
        amount_adding = 0
        while amount_adding > 64 or amount_adding >= 0:
            amount_adding = int(
                input('How many of that item do you want (up to 64)? '))
            if amount_adding <= 64:
                break

            elif amount_adding < 0:
                continue

        if amount_adding > 0:
            break

    if not hotbar_full:
        for s in hotbar:
            if not s['full']:
                s['item_name'] = adding_item
                s['amount'] = amount_adding
                s['full'] = True
                break

            else:
                continue
    else:
        print('Hotbar is full.  Try another command?')

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

    return hotbar


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
    hotbar_full = bf.check_full(hotbar)

    with open('items.json', 'r') as file:
        items = json.load(file)
        if not hotbar_full:
            for s in hotbar:
                if not s['full']:
                    s['item_name'] = random.choice(items)
                    s['amount'] = random.randint(1, 65)
                    s['full'] = True
                    break

                else:
                    continue
        else:
            print('Hotbar is full.  Try another command?')

        for s in hotbar:
            print(s)

        return hotbar


def show_args():
    print('args:')
    print('    -y -- auto runs the main program loop')


def quit():
    return False


def move(hotbar):
    slot_moving = 1
    while slot_moving > 0 and slot_moving < 10:
        slot_moving = int(input('What slot do you want to move? '))
        if slot_moving > 0 and slot_moving < 10:
            break
    slot_moving -= 1

    where_moving = 1
    while where_moving > 0 and where_moving < 10:
        where_moving = int(
            input('What slot do you want to move those items to? '))
        if where_moving > 0 and where_moving < 10:
            break
    where_moving -= 1

    if hotbar[slot_moving]['full'] and not hotbar[where_moving]['full']:
        hotbar[where_moving]['full'] = True
        hotbar[where_moving]['item_name'] = hotbar[slot_moving]['item_name']
        hotbar[where_moving]['amount'] = hotbar[slot_moving]['amount']

        hotbar[slot_moving]['full'] = False
        hotbar[slot_moving]['item_name'] = ''
        hotbar[slot_moving]['amount'] = 0

    elif not hotbar[slot_moving]['full'] and not hotbar[where_moving]['full']:
        print('The slot you wanted to move was empty.  Please try again.')

    elif not hotbar[slot_moving]['full'] and hotbar[where_moving]['full']:
        print('The slot you wanted to move those items to is full')

    elif hotbar[slot_moving]['full'] and hotbar[where_moving]['full']:
        print('The slot you wanted to move was full, and so was the slot you were moving those items to')

    for s in hotbar:
        print(s)

    return hotbar

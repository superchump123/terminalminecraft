import commands

hotbar = [{'full': False, 'item_name': '', 'amount': 0} for s in range(9)]

play = input('"play" minecraft? (y/n): ').lower()
if play == 'y':
    run = True
else:
    run = False


while run:
    command = input(
        'What would you like to do? Type help for options. ').lower()

    if command == 'help':
        commands.help()

    elif command == 'give':
        hotbar = commands.give(hotbar)

    elif command == 'quit':
        run = commands.quit()

    elif command == 'remove':
        hotbar = commands.remove(hotbar)

    elif command == 'see':
        for s in hotbar:
            print(s)

    elif command == 'add':
        hotbar = commands.add(hotbar)

    elif command == 'creeper':
        aww = 'AWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
        man = 'MANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'
        print(f'{aww}\n{man}!!!!!!!!')

    elif command == 'random item':
        hotbar = commands.random_item(hotbar)

    else:
        print('Not a valid command.  Type help for a list of commands.\n')

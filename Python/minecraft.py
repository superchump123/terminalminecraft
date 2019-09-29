'''I will be writing this project in multiple different langauges, as
I think it will be a good miniature project each language I learn.
I will attempt to make the program structure as similar as possible across
all languages this project is written in.'''

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

    else:
        print('Not a valid command.  Type help for a list of commands.\n')

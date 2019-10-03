def check_full(hotbar):
    full_slots = 0
    for s in hotbar:
        if s['item_name'] != '':
            full_slots += 1

    if full_slots == 9:
        return True
    else:
        return False


def ask_to_play():
    play = input('"play" minecraft? (y/n): ').lower()
    if play == 'y':
        return True
    else:
        return False

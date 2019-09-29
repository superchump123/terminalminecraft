def check_full(hotbar):
    full_slots = 0
    for s in hotbar:
        if s['item_name'] != '':
            full_slots += 1

    if full_slots == 9:
        return True
    else:
        return False


def get_available_slot(hotbar):
    empty_slot = 1
    for s in hotbar:
        if not s['full']:
            return empty_slot - 1
        else:
            empty_slot += 1

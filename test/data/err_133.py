# these will match

def continue_at_end_of_while():
    while True:
        continue

def continue_at_end_of_for_loop():
    for _ in range(10):
        continue

def continue_at_end_of_else_block():
    pass

def continue_in_match():
    for x in range(10):
        match x:
            case 1:
                continue

            case 2:
                continue

            case _:
                continue

def continue_in_with_block():
    while True:
        with open("file.txt") as f:
            continue


# these will not

def continue_in_match_with_trailing_stmt():
    for x in range(10):
        match x:
            case 1:
                continue

            case _:
                continue

def continue_match_with_single_continue():
    for x in range(10):
        match x:
            case 1:
                continue

            case 2:
                pass

def while_loop_with_just_a_continue():
    while True:
        continue

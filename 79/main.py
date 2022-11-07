#  Created by Simone Margio
#  www.simonemargio.im

#  A simple text-based version of the Tic Tac Toe game


GAME_MAP = [["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]

GAME_RULES = "\nRULES\n\
1. The game is played on a grid that's 3 squares by 3 squares.\n\
2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.\n\
3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n\
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n\n"

GAME_SCORE = {"You": 0, "Opponent": 0}


def menu():
    """Print the game menu"""
    while True:
        print("-- Tic Tac Toe --")
        print("1-New Game")
        print("2-Rules")
        print("0-Exit")
        choice = input("Select with number:")
        print("\n\n")

        if choice == "1":
            new_game()
        if choice == "2":
            rules()
        if choice == "0":
            break


def rules():
    """Print game's rules"""
    print(GAME_RULES)


def print_game():
    """Print map game"""
    for i in GAME_MAP:
        for j in i:
            print(j, end=' ')
        print("")


def print_score():
    print(f"--Score--\n[You: {GAME_SCORE['You']} - Opponent:{GAME_SCORE['Opponent']}]\n")


def new_game():
    """Start a new game"""
    print_score()
    # 1 = Your turn
    # 0 = Opponent turn
    player_start = randint(0, 1)
    engine(player_start)


def new_move(player):
    """Take new move input"""
    choice = input(f"\nIt's {player} turn!\nEnter row and column numbers (1,2,3) to fix spot:")
    format_and_set_move(choice, player)


def format_and_set_move(n, player_name):
    """Check if the player has chosen a valid move, format his input and confirm the move"""
    choice = ""

    for single_element in n:
        if single_element != " ":
            choice += single_element

    # The move must have only two numbers and must not exceed the game map cells
    if choice.isdigit() and len(choice) == 2 and 1 <= int(choice[0]) <= 3 and 1 <= int(choice[1]) <= 3:
        row = int(choice[0]) - 1
        col = int(choice[1]) - 1
        if GAME_MAP[row][col] == "-":
            player_symbol = return_symbol_from_player_name(player_name)
            set_move(row, col, player_symbol)
        else:
            print(f"There is already {GAME_MAP[row][col]}! Retry.")
            new_move(player_name)
    else:
        print("Invalid column and/or row! Retry.")
        new_move(player_name)


def return_symbol_from_player_name(player_name):
    if player_name == "opponent":
        return "O"
    else:
        return "X"


def set_move(row, column, player_symbol):
    """Set current player symbol to cell row column"""
    print(f"Your move - Row:{row} - Column:{column}")
    GAME_MAP[row][column] = player_symbol


def check_win(player_symbol):
    """Check if one player as winning row"""
    if is_win_vertical_horizontal(player_symbol):
        win(player_symbol)

    if is_win_diagonal(player_symbol):
        win(player_symbol)

    if is_tie():
        win("T")


def win(player_symbol):
    """Declare winning player"""
    if player_symbol == "X":
        print(f"\nPlayer WIN!\n")
        GAME_SCORE['You'] += 1
    else:
        if player_symbol == "O":
            print(f"\nOpponent WIN!\n")
            GAME_SCORE['Opponent'] += 1
        else:
            print("\nTie!\n")
    reset_game()
    menu()


def reset_game():
    """Clear map game"""
    for i in range(3):
        for j in range(3):
            GAME_MAP[i][j] = "-"


def is_win_vertical_horizontal(player_symbol):
    """Check if one player has winning vertical or horizontal"""
    win_v = 0
    win_h = 0

    for i in range(3):
        for j in range(3):
            if GAME_MAP[j][i] == player_symbol:
                win_v += 1
            if GAME_MAP[i][j] == player_symbol:
                win_h += 1
            if win_v == 3 or win_h == 3:
                return True
        win_v = 0
        win_h = 0
    return False


def is_win_diagonal(player_symbol):
    """Check if one player has winning diagonal"""
    if GAME_MAP[0][0] == player_symbol and GAME_MAP[1][1] == player_symbol and GAME_MAP[2][2] == player_symbol:
        return True
    if GAME_MAP[0][2] == player_symbol and GAME_MAP[1][1] == player_symbol and GAME_MAP[2][0] == player_symbol:
        return True
    return False


def is_tie():
    """Check there's a tie"""
    for i in range(3):
        for j in range(3):
            if GAME_MAP[i][j] == '-':
                return False
    return True


# Yep, I don't want import any libraries as random
def randint(a, b):
    """Return random integer in range [a, b], including both end points."""
    return a + randbelow(b - a + 1)


def randbelow(n):
    """Return a random int in the range [0,n).  Raises ValueError if n<=0."""
    if n <= 0:
        raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r


def random_bytes(n):
    """Return n random bytes"""
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)


def engine(current_player):
    # It's played until one player wins
    while True:
        print_game()
        # Player turn
        if current_player == 1:
            new_move("your")
            check_win("X")
            current_player = 0
        # Opponent turn
        else:
            current_player = 1
            new_move("opponent")
            check_win("O")


# Start
menu()

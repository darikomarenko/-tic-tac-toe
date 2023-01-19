def draw_board(board):
    print("-" * 13)
    for i in range(3):
        line = "|"
        for j in range(3):
            idx = str(i * 3 + j + 1)
            line += f" {board[idx] or idx} |"
        print(line)
    print("-" * 13)


def take_input(player_token):
    # valid_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        if not player_answer in board.keys():
            print("Некорректный ввод, введите число от 1 до 9")
            continue
        if board[player_answer]:
            print("Эта клетка занята")
            continue
        else:
            board[player_answer] = player_token
            valid = True


def get_token(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def check_win_conditions(board):
    win_conditions = (
        ("1", "2", "3"),
        ("4", "5", "6"),
        ("7", "8", "9"),
        ("1", "4", "7"),
        ("2", "5", "8"),
        ("3", "6", "9"),
        ("1", "5", "9"),
        ("3", "5", "7"),
    )
    for win_condition in win_conditions:
        if board[win_condition[0]] == board[win_condition[1]] == board[win_condition[2]]:
            return board[win_condition[0]] is not None
    return False


if __name__ == "__main__":
    board = {"1": None, "2": None, "3": None, "4": None, "5": None, "6": None, "7": None, "8": None, "9": None}
    has_winner = False
    turn_number = 0
    while not has_winner:
        turn_number += 1
        if turn_number > len(board):
            break
        draw_board(board)
        token = get_token(turn_number)
        take_input(token)
        has_winner = check_win_conditions(board)
    draw_board(board)
    if has_winner:
        print(f"Победил '{token}' на {turn_number} ходу!")
    else:
        print("Ничья!")

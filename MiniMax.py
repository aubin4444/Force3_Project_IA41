from GameArea import GameArea
from Player import Player

def evaluate(state, player):
    grade = 0
# Attribuer une note pour player
    if player.circletoken_id == 0:
        grade += 0
    elif player.circletoken_id == 1:
        grade += 1
    elif player.circletoken_id == 2:
        grade += token_alignment(state, player)
        grade += 2
    else:
        grade += token_alignment(state, player)
        grade += 3

    return grade

def token_alignment(state, player):
    board_lines = []
    board_columns = []
    board_diagonals = []

    for y in range(0, 3):
        line = 0
        for x in range(0, 3):
            if state.gamearea[x][y].squaretoken is None:
                line -= 1
            elif state.gamearea[x][y].squaretoken.circletoken is None:
                line += 0
            elif state.gamearea[x][y].squaretoken.circletoken.color != player.color:
                line -= 1
            else:
                line += 1
        board_lines.append(line)

    for x in range(0, 3):
        column = 0
        for y in range(0, 3):
            if state.gamearea[x][y].squaretoken is None:
                column -= 1
            elif state.gamearea[x][y].squaretoken.circletoken is None:
                column += 0
            elif state.gamearea[x][y].squaretoken.circletoken.color != player.color:
                column -= 1
            else:
                column += 1
        board_columns.append(column)

    right_diagonal = 0  # \
    for x in range(0, 3):
        if state.gamearea[x][x].squaretoken is None:
            right_diagonal -= 1
        elif state.gamearea[x][x].squaretoken.circletoken is None:
            right_diagonal += 0
        elif state.gamearea[x][x].squaretoken.circletoken.color != player.color:
            right_diagonal -= 1
        else:
            right_diagonal += 1
    board_diagonals.append(right_diagonal)

    left_diagonal = 0  # /
    for x in range(0, 3):
        if state.gamearea[x][2-x].squaretoken is None:
            left_diagonal -= 1
        elif state.gamearea[x][2-x].squaretoken.circletoken is None:
            left_diagonal += 0
        elif state.gamearea[x][2-x].squaretoken.circletoken.color != player.color:
            left_diagonal -= 1
        else:
            left_diagonal += 1
    board_diagonals.append(left_diagonal)

    temp = 0
    for i in range(3):
        if board_lines[i] == 3 or board_columns[i] == 3:
            return 7
        if board_lines[i] == 2:
            temp += 1
        if board_columns[i] == 2:
            temp += 1

    for i in range(2):
        if board_diagonals[i] == 3:
            return 7
        elif board_diagonals[i] == 2:
            temp += 1

    if temp == 3:
        return 6
    elif temp == 2:
        return 5
    elif temp == 1:
        return 2
    else:
        return 0

if __name__ == '__main__':
    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)
    #board.moveSquareToken(board.gamearea[0][1])
    board.addCircleToken(0, 0, player_1)
    board.addCircleToken(1, 0, player_2)
    board.addCircleToken(2, 1, player_2)
    board.addCircleToken(2, 0, player_1)
    board.addCircleToken(2, 2, player_1)
    board.moveSquareToken(board.gamearea[2][0])
    board.displayGameArea()
    print(evaluate(board, player_1))


from copy import deepcopy

from GameArea import GameArea
from Player import Player
from GameMode import isWinnerIA
from move import move
from Tile import Tile
import CONSTANT

def grades(liste):
    if len(liste) == 0:
        grade = 0
        return grade
    elif len(liste) == 1:
        grade = 1
        return grade
    else:
        head = liste.pop(0)
        body = deepcopy(liste)

        grade = grades(liste)

        for i in range(len(body)):
            next = body[i]

            if head[0] == next[0]:
                grade += 1 + 2*i
            """if head[0] == next[1]:
                grade -= 1
            if head[1] == next[0]:
                grade -= 1"""
            if head[1] == next[1]:
                grade += 1 + 2*i
        return grade

# Checking if row can be complete by player or opponent
def evaluate(board,ismax,player_id):

    """# The player_id is the id of the player who we want to will
    # The ismax is just to know if is the turn of the max or min player
    players = [board.player_1, board.player_2]
    if player_id == 0:
        thegoodplayer = players[0]
        thebadplayer = players[1]
    elif player_id == 1:
        thegoodplayer = players[1]
        thebadplayer = players[0]"""

    token_player1, token_player2 = rec_circletoken(board)

    print("coordonnées des token du player 1 sont : " + str(token_player1) + " et la note est " + str(grades(token_player1)))
    print("coordonnées des token du player 2 sont : " + str(token_player2) + " et la note est " + str(grades(token_player2)))

    """
    # Si player_1 au moins 1 token sur le board
    if len(p1_tok) >= 1:
        x0 = p1_tok[0].get_X()
        y0 = p1_tok[0].get_Y()
        # Si player_1 a 1 token sur le board (note = 1)
        if len(p1_tok) == 1:
            result = 1
        # Si player_1 au moins 2 tokens sur le board
        elif len(p1_tok) >= 2:
            x1 = p1_tok[1].get_X()
            y1 = p1_tok[1].get_Y()
            # Si player_1 a 2 token sur le board
            if len(p1_tok) == 2:
                # Si les 2 ne sont pas alignés (note = 2)
                if x0 != x1 and y0 != y1:
                    result = 2
                # Si les 2 sont alignés (note = 3)
                else :
                    result = 3
            # Si player_1 a 3 tokens sur le board
            elif len(p1_tok) == 3:
                x2 = p1_tok[2].get_X()
                y2 = p1_tok[2].get_Y()
                # Si les 3 tokens sont alignés (note = 10)
                if (x0 == x1 and x1 == x2) or (y0 == y1 and y1 == y2):
                    result = 10
                elif (x0 == x1)
            """

    """# So thegoodplayer is the player who we want to will
    # thebadplayer is the player who we want to lose
    # they depend of the player_id
    if ismax == 1:
        if isWinnerIA(board,thegoodplayer):
            return 10
        elif isWinnerIA(board,thebadplayer):
            return -10
        else:
            return 0

    elif ismax == 0:
        if isWinnerIA(board,thegoodplayer):
            return 10
        elif isWinnerIA(board,thebadplayer):
            return -10
        else:
            return 0"""
def rec_circletoken(board):
    player_1_token = []
    player_2_token = []
    for i in range(3):
        for j in range(3):
            if board.gamearea[i][j].isSquareToken():
                if board.gamearea[i][j].getSquareToken().isCircleToken():
                    if board.gamearea[i][j].getSquareToken().getCircleToken().player_id == 0:
                        player_1_token.append(board.gamearea[i][j].getSquareToken().getCircleToken())
                    else:
                        player_2_token.append(board.gamearea[i][j].getSquareToken().getCircleToken())

    coo_token_player1 = rec_circletoken_coordonnées(player_1_token)
    coo_token_player2 = rec_circletoken_coordonnées(player_2_token)

    return coo_token_player1, coo_token_player2

def rec_circletoken_coordonnées(player_token):
    coordonnées = []

    # Si le player au moins 1 token sur le board
    if len(player_token) >= 1:
        x0 = player_token[0].get_X()
        y0 = player_token[0].get_Y()
        coordonnées.append([x0, y0])
    # Si le player au moins 2 tokens sur le board
    if len(player_token) >= 2:
        x1 = player_token[1].get_X()
        y1 = player_token[1].get_Y()
        coordonnées.append([x1, y1])
    # Si le player a 3 tokens sur le board
    if len(player_token) == 3:
        x2 = player_token[2].get_X()
        y2 = player_token[2].get_Y()
        coordonnées.append([x2, y2])
    return coordonnées

# Define a list of two dimentions (list of coordinates) for where the token can be moved
def allmovecirculartokens(board):
    tab = [[]]
    for col in range(3):
        for row in range(3):
            if board.gamearea[row][col].squaretoken is not None:
                if board.gamearea[row][col].squaretoken.circletoken is None:
                    tab.append([row, col])
    # Remove the first element of the list
    tab.pop(0)
    return tab

# Define a list of two dimentions (list of coordinates) of which square token can be moved
def allmovesquaretokens(board):
    tab = []
    # Récupération de la tile sur laquelle il n'y a pas de square token
    for i in range(3):
        for j in range(3):
            if not board.gamearea[i][j].isSquareToken():
                empty_tile = board.gamearea[i][j]
    # Récupération des id des square token pouvant être déplacé de 1 sur le board
    temp = CONSTANT.moveable_squaretoken[str(empty_tile.tile_id)]
    # Récupération des coordonnées de chacunes des cases pouvant être déplacée de 1
    for x in range(len(temp)):
        tab.append(CONSTANT.correlation[str(temp[x])])

    return tab
#
def get_possible_moves(board,ismax):

    allmove = move()
    allmove.place_token = [[]]
    allmove.place_token = allmovecirculartokens(board)
    allmove.move_tokens = [[]]
    allmove.move_tokens = allmovecirculartokens(board)
    allmove.move_square = allmovesquaretokens(board)

    return allmove

def make_move(board,litlemove,indexmove,ismax,player_id,circle_tokenid):

    if player_id == 0:
        thegoodplayer = board.player_1
        thebadplayer = board.player_2
    elif player_id == 1:
        thegoodplayer = board.player_2
        thebadplayer = board.player_1

    # Just for checking errors
    if board is None:
        print("board is none")

    # The indexmove is to select the type of move(0=place token,1=move token,2=move square 3 move 2square)
    if indexmove ==0:
        if ismax:
            # litlemove is a list of two dimentions (list of coordinates) for where the token can be moved
            board.addCircleToken(litlemove[0], litlemove[1], thegoodplayer)
        else:
            board.addCircleToken(litlemove[0], litlemove[1], thebadplayer)
    if indexmove == 1:
        if ismax:
            board.moveCircleToken(litlemove[0], litlemove[1], thegoodplayer, circle_tokenid)
        else:
            board.moveCircleToken(litlemove[0], litlemove[1], thebadplayer, circle_tokenid)
    if indexmove == 2:
        board.moveSquareToken(board.gamearea[litlemove[0]][litlemove[1]], True)


def minmax(state, depth, ismax, player_id):
    if player_id == 0:
        thegoodplayer = state.player_1
        thebadplayer = state.player_2
    else:
        thegoodplayer = state.player_2
        thebadplayer = state.player_1

    # evaluate the board
    score = evaluate(state, ismax,player_id)
    if score == 6:
        return score
    if score == -6:
        return score
    # Si la profondeur maximale est atteinte
    if depth == 0:
        return 0

    # Récupération des coordonnées à tester
    listofmove = get_possible_moves(state, 1).move_tokens
    listofmove2 = get_possible_moves(state, 1).place_token
    listofmove3 = get_possible_moves(state, 1).move_square

    if ismax:
        # Initialisation de la pire valeur
        bestValue = -5000
        # Test de déplacement des squaretoken sur toutes les coordonnées disponibles du board
        for move in listofmove3:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 2, True, player_id, -1)
            value = minmax(newState, depth - 1, False, player_id)
            # Test de la valeure obtenue
            bestValue = max(bestValue, value)

        # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board(tout les moves)
        for move in listofmove:
            # Pour chacun des circle token du board
            for i in range(thegoodplayer.getnumberofcircletoken()):
                    # Création d'une copie du board
                    newState = deepcopy(state)
                    # Execution du coup
                    make_move(newState, move, 1, True,player_id,i)
                    # Appelle de minmax sur le nouveau board
                    value = minmax(newState, depth - 1, False,player_id)
                    # Test de la valeure obtenue
                    bestValue = max(bestValue, value)

        for move in listofmove2:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 0, True, player_id,-1)
            value = minmax(newState, depth - 1, False, player_id)
            # Test de la valeure obtenue
            bestValue = max(bestValue, value)

        return bestValue
    else:
        bestValue = 5000

        for move in listofmove3:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 2, False, player_id, -1)
            value = minmax(newState, depth - 1, True, player_id)
            # Test de la valeure obtenue
            bestValue = min(bestValue, value)

        for move in listofmove:
          for i in range(thebadplayer.getnumberofcircletoken()):
                  # Création d'une copie du board
                  newState = deepcopy(state)
                  # Éxecution du coup
                  make_move(newState, move, 1, False,player_id,i)
                  #on appelle minmax sur le nouveau board
                  value = minmax(newState, depth - 1, True,player_id)
                  # Test de la valeure obtenue
                  bestValue = min(bestValue, value)


        for move in listofmove2:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 0, False, player_id, -1)
            value = minmax(newState, depth - 1, True, player_id)
            # Test de la valeure obtenue
            bestValue = min(bestValue, value)

        return bestValue

# Fonction permettant de trouver le meilleur coup grâce à minmax pour un joueur donné
# Évaluation de tous les coups possibles au premier tour avec minmax
# Renvois le board avec le meilleur coup effectué


def findBestMove(board, player):
    # Initialisation de l'id du joueur avec qui l'on souhaite optimiser le coup avec minmax
    player_id = player.player_id

    if player_id == 0:
        thegoodplayer = board.player_1
        thebadplayer = board.player_2
    elif player_id == 1:
        thegoodplayer = board.player_2
        thebadplayer = board.player_1

    # Initialisation des valeurs par défauts
    bestVal = -1000
    bestMove = (-1, -1)
    indexmovea=-1
    # Récupération des coordonnées à tester
    listofmove = get_possible_moves(board, 1).move_tokens
    listofmove2 = get_possible_moves(board, 1).place_token
    listofmove3 = get_possible_moves(board, 1).move_square

    # Test de déplacement des squaretoken sur toutes les coordonnées disponibles du board
    for move in listofmove3:
        # Création d'une copie du board
        newState = deepcopy(board)
        # Execution du coup
        make_move(newState, move, 2, True, player_id, -1)
        moveVal = minmax(newState, 2, False, player_id)
        if moveVal > bestVal:
            bestMove = move
            bestVal = moveVal
            indexmovea = -2

    # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board(tout les moves)
    for move in listofmove:
        # Pour chacun des circle token du board
        for i in range(thegoodplayer.getnumberofcircletoken()):
                # Création d'une copie du board
                newState = deepcopy(board)
                # Éxecution du coup
                make_move(newState, move, 1, True, player_id, i)
                moveVal = minmax(newState, 2, False, player_id)

                # Si la valeure de coup joué est meilleure que la valeure du meilleur coup
                if moveVal > bestVal:
                    # Le coup joué devient le meilleur coup
                    bestMove = move
                    bestVal = moveVal
                    indexmovea=i
                if bestVal == 10:
                    break

    for move in listofmove2:
        if bestVal == 10:
            break
        # Création d'une copie du board
        newState = deepcopy(board)
        # Execution du coup
        make_move(newState, move, 0, True, player_id, -1)
        moveVal = minmax(newState, 2, False, player_id)

        if moveVal > bestVal:
            bestMove = move
            bestVal = moveVal
            indexmovea = -1

    if player_id == 0:
        colortoken = "Rouge"
    else:
        colortoken = "Bleu"

    if indexmovea == -1:
        print("le meilleur coup est de placer un nouveau token de couleur "+colortoken+" en position  " +
              str(bestMove) + " \nThe values of minimax of the best Move is : " + str(bestVal))
    elif indexmovea == -2:
        print("le meilleur coup est de bouger le square token ayant l'identifiant " +
              str(board.gamearea[bestMove[0]][bestMove[1]].tile_id) +
              " \nThe values of minimax of the best Move is : " + str(bestVal))
    else:
        print("le meilleur coup est de bouger le circle token numero : " +
              colortoken + str(indexmovea) + " en position " + str(bestMove) +
              " \nThe values of minimax of the best Move is : " + str(bestVal))

    print("Move effectué \n")

    if indexmovea == -1:
        make_move(board, bestMove, 0, True, player_id, indexmovea)
    elif indexmovea == -2:
        make_move(board, bestMove, 2, True, player_id, -1)
    else:
        make_move(board, bestMove, 1, True, player_id, indexmovea)

    return board


if __name__ == '__main__':
    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)

    board.addCircleToken(1, 0, player_1)
    board.addCircleToken(2, 0, player_1)
    board.addCircleToken(1, 2, player_1)
    board.addCircleToken(0, 2, player_2)
    board.moveSquareToken(board.gamearea[1][2])
    board.displayGameArea()
    evaluate(board, 1, 1)
    #board = findBestMove(board, board.player_2)
    #board.displayGameArea()
    #evaluate(board, 1, 1)











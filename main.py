from GameArea import GameArea
from Player import Player
from CircleToken import CircleToken
import GameMode as gm
import NewMinmax as ai
from tkinter import *
import pygame
pygame.init()

#Creation of players
player_1 = Player(0, "R")
player_2 = Player(1, "B")


#Creation of the game board
board = GameArea(player_1, player_2)
board.displayGameArea()


#Générer la fenêtre
pygame.display.set_caption("Force 3 Game")
screen = pygame.display.set_mode((1080, 720))

#Importer et charger l'arrière plan
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (1200, 700))

running = True

while running:

    # Appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0))

    # Appliquer l'image de la Grid
    #screen.blit(board.image, (70, 30))
    for y in range(3):
        for x in range(3):
            screen.blit(board.gamearea[x][y].image, (200 + (210 * x), 0 + (210 * y)))
            if x != 1 or y != 1:
                screen.blit(board.gamearea[x][y].squaretoken.image, (225 + (210 * x),25 + (210 * y)))


    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #que l'évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

#Choice of game mode
mode = gm.start()


#Assigning ai to players
if mode == 2 or mode == 3:
    player_2.isia = True
if mode == 3:
    player_1.isia = True

player = [player_1, player_2]



round = 1
check = "0"

while check == "0":
    if round == 0:
        round = 1
    else:
        round = 0
    if player[round].isia == True:
        board, check = ai.findBestMove(board, player[round])
    else:
        check = gm.next_round(board, player[round])
    board.displayGameArea()
exit()


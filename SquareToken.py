from CircleToken import CircleToken
import pygame

class SquareToken(pygame.sprite.Sprite):
    """This class instanciate a square token which can carry a circle token or not"""
    def __init__(self, tile_id):
        self.image = pygame.image.load('assets/Square_token.png')
        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()
        self.circletoken = None
        self.tile_id = tile_id

    #Put a circle token on the square token
    def setCircleToken(self, circletoken):
        self.circletoken = circletoken

    #If it carries a token it returns it otherwise it returns the None value
    def getCircleToken(self):
        return self.circletoken

    #Check if the square token carries a circle token
    def isCircleToken(self):
        if self.circletoken is None:
            return False
        else:
            return True

    #Creates a circle token and assigns it to the square token
    def createCircletoken(self, pos_X, pos_Y, color, player_id, token_id):
        self.circletoken = CircleToken(pos_X, pos_Y, color, player_id, token_id)
        return self.circletoken
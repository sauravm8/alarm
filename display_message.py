import pygame
import time
import config
import threading

class Displaying_message(threading.Thread):

    daemon = True

    def __init__(self, text):
        super(Displaying_message, self).__init__()
        pygame.init()

        self.display_width = config.DISPLAY_HEIGHT
        self.display_height = config.DISPLAY_WIDTH

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))

        self.text = text


    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.white)
        return textSurface, textSurface.get_rect()

    def run(self):
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = self.text_objects(self.text, largeText)
        TextRect.center = ((self.display_width / 2), (self.display_height / 2))
        self.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

"""
#Testing
displaying_message_obj = Displaying_message("ho ho ho")
displaying_message_obj.start()
"""
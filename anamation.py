# -*- coding: utf-8 -*-
"""
Brendan Eye anamation 
"""


#Initialize
import random
import pygame

def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Charlie!")

    #Entities
    #yellow background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("papayawhip")

    #load an image
    cardinal = pygame.image.load("Charlie.png")
    cardinal = cardinal.convert_alpha()
    cardinal = pygame.transform.scale(cardinal, (100, 100))

    # set up some cardinal variables
    cardinal_x = screen.get_width()/2
    cardinal_y = screen.get_height()/2

    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True

        #Loop
    while keepGoing:

        #Time
        clock.tick(30)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #modify cardinal value
        cardinal_x += random.randint(-100, 100)
        cardinal_y += random.randint(-100, 100)
        #check boundaries
        if cardinal_x >= screen.get_width():
            cardinal_x = screen.get_width()/2
      
        if cardinal_y >= screen.get_height():
             cardinal_y = screen.get_height()/2
        if cardinal_y <=0:
                 cardinal_y = screen.get_height()/2


        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(cardinal, (cardinal_x, cardinal_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
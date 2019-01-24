"""
Alex U's Snake Game
Pygame is required to run this code, and this can be found by a simple google.

The change in this code was purely conceptual, I did not use any exterior ideas.
"""

import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (0,155,0)
purple = (239,112,239)
Lgreen=(0,200,0)
gray=(132,132,132)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')


clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)

#1. Purple Snake
def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, purple, [XnY[0],XnY[1],block_size,block_size])
    

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0

    def surroundingArea():
        x=random.randint(0,1)
        if x == 0:
            distance = round(random.randrange(20,50)/10)*10
        elif x == 1:
            distance = -1 * round(random.randrange(20,50)/10)*10
        return(distance+0)

    PrandAppleX = randAppleX + surroundingArea()
    PrandAppleY = randAppleY + surroundingArea()
    
    while not gameExit:
        #2.gray Background
        while gameOver == True:
            gameDisplay.fill(gray)
            message_to_screen("game over, press C to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change=0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change=0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change=0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change=0
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change
        #2.gray background still
        gameDisplay.fill(gray)

        #3.Apple Thickness is 20
        AppleThickness = 20
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness,AppleThickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        #4. Adding Poison Apple
        pygame.draw.rect(gameDisplay, Lgreen, [PrandAppleX, PrandAppleY, AppleThickness,AppleThickness])

        
        

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(block_size, snakeList)

        
        pygame.display.update()

##        if lead_x == randAppleX and lead_y == randAppleY:
##            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
##            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
##            snakeLength += 2

        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
                PrandAppleX = randAppleX + surroundingArea()
                PrandAppleY = randAppleY + surroundingArea()
                #5. Adding random posion apple location and more length when contact is made
                snakeLength += 5

        if lead_x >= PrandAppleX and lead_x <= PrandAppleX + AppleThickness:
            if lead_y >= PrandAppleY and lead_y <= PrandAppleY + AppleThickness:
                gameOver = True

        
        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()

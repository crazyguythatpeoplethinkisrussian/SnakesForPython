# These are import statements, just like in Java!
# They help us so we don't have to rewrite code someone else has already written
import pygame, sys
from random import randint
from pygame.locals import *
from Helpers import *
from Constants import *



# This is the head of the snake.
# What type is it?!?!
snakeHead = Rect(blockSize, blockSize, blockSize, blockSize)
snakeHead2 = Rect(blockSize, blockSize, blockSize, blockSize)

# This is the body of the snake.
# These brackets mean that the body is a list;
# In other words, there might be many parts to the body.
snakeBody = []
snakeBody2 = []
# This is the apple.
# Calling randomRect starts the apple off in a random place on the screen.
apple = randomRect()

# Set up the screen. Don't worry about this code - it tells python that we want a screen of a certain size
pygame.init()
scrHeight = yBound * blockSize
scrWidth = xBound * blockSize
screen = pygame.display.set_mode((scrHeight, scrWidth))
initWalls(screen)
clock = pygame.time.Clock()

# This loop is very interesting. When will it stop running?
# (hint- when is the while condition false?)
while True:
    clock.tick(40)

    # This gets the keyboard input. Don't worry too much about the first couple lines.
    for keypress in pygame.event.get():
        if keypress.type == QUIT:
            quitGame()

        # This is where we switch directions based on which key is pressed.
        # What do you think elif means? Does it sound like anything you've heard before?
        # Why do we check direction != UP, direction != DOWN, etc. ?
        elif keypress.type == KEYDOWN:
            # Check for the up arrow key
            if keypress.key == K_UP and direction != UP and direction != DOWN:
                direction = UP
            # Check for the down arrow key
            elif keypress.key == K_DOWN and direction != DOWN and direction != UP:
                direction = DOWN
            # Check for the left arrow key
            elif keypress.key == K_LEFT and direction != LEFT and direction != RIGHT:
                direction = LEFT
            # Check for the right arrow key
            elif keypress.key == K_RIGHT and direction != RIGHT and direction != LEFT:
                direction = RIGHT


    # Copy the head for later use.
    oldPiece2 = snakeHead2.copy()
    # Move the head in the direction we are facing.
    snakeHead2 = moveHead(snakeHead2, direction2)
    oldPiece = snakeHead.copy()
    # Move the head in the direction we are facing.
    snakeHead = moveHead(snakeHead, direction)
    # Update the snake's body (excluding the head).
    # This piece of code takes each piece in the body and shifts it to where the next piece is
    # so it looks like the snake is moving!
    for i in range(0, len(snakeBody2)):
        temp = snakeBody2[i].copy()
        snakeBody2[i] = moveBody(oldPiece, snakeBody2[i])
        oldPiece = temp
    for i in range(0, len(snakeBody)):
        temp = snakeBody[i].copy()
        snakeBody[i] = moveBody(oldPiece, snakeBody[i])
        oldPiece = temp
    # These are variables that are True or False depending on conditions.
    # What do we call these kinds of variables?
    hasHitWall = snakeHead.collidelist(walls) != -1
    hasHitBody = snakeHead.collidelist(snakeBody or snakeBody2) != -1
    hasEaten = snakeHead.colliderect(apple)
    hasHitWall = snakeHead2.collidelist(walls) != -1
    hasHitBody = snakeHead2.collidelist(snakeBody or snakeBody2) != -1
    hasEaten = snakeHead2.colliderect(apple)

    # Checks if the head collides with the wall.
    if(hasHitWall):
        quitGame()

    # We need to check if the head has collided with the body!
    # How can we do this?
    # (hint- it should be very similar to the line above!)
    # Go ahead and do it here!
    if (hasHitBody):
        quitGame()
    snakeBody.append(oldPiece)
    # Checks if the head collides with the apple.
    if (hasEaten):
        apple = randomRect()


    #Graphically draws all the updates we just made.
    draw(oldPiece, snakeHead, snakeHead2, snakeBody,snakeBody2, apple, hasEaten, screen)
    pygame.display.flip()







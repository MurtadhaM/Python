

import random
import sys
import time

# Listen for keyboard input
import keyboard

# Set the speed of the game (Refresh rate in seconds)
speed = .1




# MATRIX SIZE
rows = 5
cols = 6


stopRow = 3
stopCol = 3




# Set the starting position of the snake
snakeRow = 1
snakeCol = 1

# Set the starting position of the food
foodRow = 3
foodCol = 3


def randomizeFood():
    global foodRow
    global foodCol
    foodRow = random.randint(1, rows)
    foodCol = random.randint(1, cols)

# When the arrow keys are pressed, the corresponding


def printMatrix(score):
    print('\n\n\n\n\n\n\t')
    print('Score: ' + str(score))
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if col == snakeCol and row == snakeRow:
                print('🐍', end='')
            elif col == foodCol and row == foodRow:
                print('🍎', end='')
            else:
                print('. ', end='')
        print()


def moveSnake(direction):
    global snakeRow
    global snakeCol
    # Limit tnhe snake to the matrix
    if snakeCol == 1 and direction == 'left':
        return
    elif snakeCol == cols and direction == 'right':
        return
    elif snakeRow == 1 and direction == 'up':
        return
    elif snakeRow == rows and direction == 'down':
        return
    # Move the snake

    if direction == 'left':
        snakeCol = snakeCol - 1
    elif direction == 'right':
        snakeCol = snakeCol + 1
    elif direction == 'up':
        snakeRow = snakeRow - 1
    elif direction == 'down':
        snakeRow = snakeRow + 1


# Listen for keyboard input
keyboard.on_press_key("left arrow", lambda _: moveSnake('left'))
keyboard.on_press_key("right arrow", lambda _: moveSnake('right'))
keyboard.on_press_key("up arrow", lambda _: moveSnake('up'))
keyboard.on_press_key("down arrow", lambda _: moveSnake('down'))


def startGame():
    TimeForFood = 0
    score = 0
    while True:
        TimeForFood = TimeForFood + 1
        # Change the food position every 4 seconds
        if TimeForFood == 30:
            randomizeFood()
            TimeForFood = 0
        printMatrix(score)
        time.sleep(speed)
        if snakeCol == foodCol and snakeRow == foodRow:
            score = score + 1
            randomizeFood()

        # elif snakeCol == stopCol and snakeRow == stopRow:
        #     print('You lose!')
        #     sys.exit()


startGame()



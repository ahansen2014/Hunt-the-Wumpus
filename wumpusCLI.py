'''
Author: Andrew R. Hansen, 26/4/2019
This CLI version has been written as a teaching aid.  The goal of this version is to create a solution
that is easily modified so students can add their own modifications without too much difficulty.
Change log
26/4/2019: ver1.0 original release
18/4/2022: ver2.0 update to Python3
'''
from random import randint

# The caves array with all the neighbours in it.
caves = [[1,4,7], [0,2,9], [1,3,11], [2,4,13], [0,3,5], [4,6,14], [5,7,16], [0,6,10], [9,11,18], [1,8,10], [7,9,19], [2,8,12],
         [11,13,17], [3,12,14], [5,13,15], [14,16,17], [6,15,19], [12,15,18], [8,17,19], [10,16,18]]

# Keep track of the current cave
currentCave = 0

# Create empty arrays to hold the special caves
wumpusCave = []
batCaves = []
pitCaves = []

# Create a boolean value to keep track of whether the player is alive or dead.
isAlive = True

# Give the player an arrow
arrows = 1

def setUpCaves():
    specialCaves = [] # A new list of special caves
    while len(specialCaves) < 5:
        randomCave = randint(1,19)
        if randomCave not in specialCaves:
            specialCaves.append(randomCave)

    wumpusCave.append(specialCaves[0]) # The Wumpus goes in the first cave
    pitCaves.append(specialCaves[1])
    pitCaves.append(specialCaves[2]) # The pits are in the second and third caves
    batCaves.append(specialCaves[3])
    batCaves.append(specialCaves[4]) # The bats are in the fourth and fifth caves

    # print('Diagnostics:')
    # print('Wumpus cave:', wumpusCave)
    # print('Bat caves:', batCaves)
    # print('Pit caves:', pitCaves)

def updateStatus():
    global isAlive # This needs to be globalised so we can set it to FALSE if the player dies

    if currentCave in wumpusCave:
        statusString = 'You are in the Wumpus cave!  \nYou are now DEAD! \nGame Over.'
        isAlive = False # The player is now dead so they cannot move.

    elif currentCave in pitCaves:
        statusString = 'You have fallen down a bottomless pit.  \nYou are now DEAD!  \nGame Over.'
        isAlive = False # The player is now dead so they cannot move.

    else:
        statusString = 'You are in cave: ' + str(currentCave) + '\n'
        statusString += 'Tunnels lead to caves: ' + str(caves[currentCave][0]) + ', ' + str(caves[currentCave][1]) + ', ' + str(caves[currentCave][2]) # The neighbours of the current cave

        if wumpusCave[0] in caves[currentCave]:
            statusString += '\nYou smell something terrible!'

        if pitCaves[0] in caves[currentCave] or pitCaves[1] in caves[currentCave]:
            statusString += '\nYou feel a breeze.'

        if batCaves[0] in caves[currentCave] or batCaves[1] in caves[currentCave]:
            statusString += '\nYou hear flapping'

    return statusString

def checkBats():
    global currentCave # If we want to change a global variable we have to use this line to get access
    if currentCave in batCaves:
        print('You have been carried off by giant bats and dropped in a random cave.')
        currentCave = randint(0, 19)


def doMove(targetCave):
    global currentCave # If we want to change a global variable we have to use this line to get access
    if isAlive and targetCave in caves[currentCave]: # If the move is valid ...
        currentCave = targetCave # ... update the current cave.
    else:
        print('You cannot move there.')

def doShoot(targetCave):
    global isAlive
    if targetCave in caves[currentCave]:  # If the shot is allowed
        if targetCave == wumpusCave[0]:
            print('You killed the Wumpus!\nGame Over!')
            isAlive = False
        else:
            print('You have no arrows left.\nIt is only a matter of time before the Wumpus eats you.\nGame Over!')
            isAlive = False
    else:
        print('You cannot shoot to there.')


### MAIN CODE ###

setUpCaves()
print(updateStatus())
while isAlive:
    userInput = input('Command: ')
    command = userInput.split(' ')
    if command[0] == 'move':
        doMove(int(command[1]))
        checkBats()
        print(updateStatus())
    if command[0] == 'shoot':
        doShoot(int(command[1]))


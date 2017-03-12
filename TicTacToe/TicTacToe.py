#imports------------

import random
import os
import time

#Hardcoded------------

board = [" "] * 10

#defenations---------------

def mainBoard():
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def scRefresh():
    os.system("cls")
    mainBoard()

def playMove():
    referValue = int(input("Your move?: "))
    if board[referValue] == " ":
        board[referValue] = "X"
    else:
        print("that move is taken")
        playMove()

def aiMove():
    aiValue = random.randint(1,9)
    if board[aiValue] == " ":
        board[aiValue] = "O"
    else:
        aiMove()

def playMoveDisplay():
    scRefresh()
    playMove()
    scRefresh()

def aiMoveDisplay():
    scRefresh()
    time.sleep(1)
    aiMove()
    scRefresh()

def aiPlayFirst():
    aiMoveDisplay()
    while True:
        playMoveDisplay()
        aiMoveDisplay()

def userPlayFirst():
    playMoveDisplay()
    while True:
        aiMoveDisplay()
        playMoveDisplay()

def winPoss():
    return(board[])

#Execution----------------------

while True:
    whoFirst = (input("who first?(B=Bot/P=Player) : "))
    if whoFirst == "B":
        aiPlayFirst()
    elif whoFirst == "P":
        userPlayFirst()
    else:
        print("please input a valid choice!")

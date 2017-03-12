#imports------------

import random
import os
import time

#Hardcoded------------

board = ["OMG THIS SHITTY BUG WASTED HOWERS TO ACTUALLY FIGURE OUT! STUPID THING!"," "," "," "," "," "," "," "," "," "]

#Fancy-----------------------------

def title():
    print(",---------. .-./`)     _______            ,---------.    ____        _______            ,---------. .---.  .---.   ___    _ ,---.    ,---. _______   ")
    print("\          \\ .-.')   /   __  \           \          \ .'  __ `.    /   __  \           \          \|   |  |_ _| .'   |  | ||    \  /    |\  ____  \ ")
    print(" `--.  ,---'/ `-' \  | ,_/  \__)           `--.  ,---'/   '  \  \  | ,_/  \__)           `--.  ,---'|   |  ( ' ) |   .'  | ||  ,  \/  ,  || |    \ | ")
    print("    |   \    `-'`\"`,-./  )        _ _    _ _  |   \   |___|  /  |,-./  )        _ _    _ _  |   \   |   '-(_{;}_).'  '_  | ||  |\_   /|  || |____/ / ")
    print("    :_ _:    .---. \  '_ '`)     ( ' )--( ' ) :_ _:      _.-`   |\  '_ '`)     ( ' )--( ' ) :_ _:   |      (_,_) '   ( \.-.||  _( )_/ |  ||   _ _ '. ")
    print("    (_I_)    |   |  > (_)  )  __(_{;}_)(_{;}_)(_I_)   .\'   _    | > (_)  )  __(_{;}_)(_{;}_)(_I_)   | _ _--.   | \' (`. _` /|| (_ o _) |  ||  ( \' )  ")
    print("   (_(=)_)   |   | (  .  .-'_/  )(_,_)--(_,_)(_(=)_)  |  _( )_  |(  .  .-'_/  )(_,_)--(_,_)(_(=)_)  |( ' ) |   | | (_ (_) _)|  (_,_)  |  || (_{;}_) |")
    print("    (_I_)    |   |  `-'`-'     /              (_I_)   \ (_ o _) / `-'`-'     /              (_I_)   (_{;}_)|   |  \ /  . \ /|  |      |  ||  (_,_)  /")
    print("    '---'    '---'    `._____.'               '---'    '.(_,_).'    `._____.'               '---'   '(_,_) '---'   ``-'`-'' '--'      '--'/_______.' ")
    print("                                                                                                                                                     ")
    print("                               |_                              _   _  ____   _  _   ____   ___  ____ ")
    print("                               |_)\/                          ) \_/ (/ __ \ ) \/ ( / __ \ / _( / __ \\")
    print("                                  /                           |  _  |))__(( |  \ | ))__(( ))_  ))__((")
    print("                                                              )_( )_(\____/ )_()_( \____/ \__( \____/")

def rules():
    print("they shall be added later :D")

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
    title()
    rules()
    mainBoard()

def playMove():
    referValue = moveInpValid("Your move: ")
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
        checkGameWon()
        aiMoveDisplay()
        checkGameWon()

def userPlayFirst():
    playMoveDisplay()
    while True:
        aiMoveDisplay()
        checkGameWon()
        playMoveDisplay()
        checkGameWon()

def moveInpValid(prompt):
    while True:
        try:
            inpVal = int(input(prompt))
        except ValueError:
            print ("Please input integers only!")
            continue
        if not (inpVal >= 1 and inpVal <= 9):
            print("the move can only be between 1-9")
            continue
        else:
            break
    return inpVal

def winPoss():
    return(board[" "])

def playerWon():
    return(
        #horrizontal
        (board[1] == "X" and board[2] == "X" and board[3] == "X" ) or
        (board[4] == "X" and board[5] == "X" and board[6] == "X" ) or
        (board[7] == "X" and board[8] == "X" and board[9] == "X" ) or
        #vertical
        (board[7] == "X" and board[4] == "X" and board[1] == "X") or
        (board[8] == "X" and board[5] == "X" and board[2] == "X") or
        (board[9] == "X" and board[6] == "X" and board[3] == "X") or
        #diagnoa
        (board[1] == "X" and board[5] == "X" and board[9] == "X") or
        (board[7] == "X" and board[5] == "X" and board[3] == "X"))

def aiWon():
    return (
        # horrizontal
        (board[1] == "O" and board[2] == "O" and board[3] == "O") or
        (board[4] == "O" and board[5] == "O" and board[6] == "O") or
        (board[7] == "O" and board[8] == "O" and board[9] == "O") or
        # vertical
        (board[7] == "O" and board[4] == "O" and board[1] == "O") or
        (board[8] == "O" and board[5] == "O" and board[2] == "O") or
        (board[9] == "O" and board[6] == "O" and board[3] == "O") or
        # diagnoal
        (board[1] == "O" and board[5] == "O" and board[9] == "O") or
        (board[7] == "O" and board[5] == "O" and board[3] == "O"))

def checkGameWon():
    if playerWon():
        print("YAY!YOU HAVE WON THE GAME")
        exitSeq()
    elif aiWon():
        print("Oh no! you have lost the game")
        exitSeq()
    elif boardFull():
        print("The Game is a Draw!")
        exitSeq()
    else:
        return False

def boardFull():
    if " " in board:
        return False
    else:
        return True

def exitSeq():
    exitQ = input("do you want to  Retry [R] or Exit [E]").upper()
    if exitQ == "E":
        exit()
    elif exitQ == "R":
        mainGame()
    else:
        exitSeq()

def mainGame():
    scRefresh()
    whoFirst = (input("who first?(B=Bot/P=Player) : ")).upper()
    if whoFirst == "B":
        aiPlayFirst()
    elif whoFirst == "P":
        userPlayFirst()
    else:
        print("please input a valid choice!")
        mainGame()


#Execution----------------------

mainGame()
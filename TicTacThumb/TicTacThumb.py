# imports------------

import random
import os
import time

# Hardcoded------------

board = ["OMG THIS SHITTY BUG WASTED HOWERS TO ACTUALLY FIGURE OUT! STUPID THING!", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Fancy-----------------------------

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
    print("                                                                   |_                              _   _  ____   _  _   ____   ___  ____ ")
    print("                                                                   |_)\/                          ) \_/ (/ __ \ ) \/ ( / __ \ / _( / __ \\")
    print("                                                                      /                           |  _  |))__(( |  \ | ))__(( ))_  ))__((")
    print("                                                                                                  )_( )_(\____/ )_()_( \____/ \__( \____/")

def rules():
    print("===========================================================================================================================================================")
    print("||                                                                                    Grid:                                                              ||")
    print("||                                                                                      ||  7|8|9  ||                                                    ||")
    print("||How to play TIC-TAC-THUMB?                                                            ||  -+-+-  ||                                                    ||")
    print("||Its ez! All you have to do is just bring the game to a DRAW! :D                       ||  4|5|6  ||                                                    ||")
    print("||Yep, you read that right! Unlike other similar looking games...                       ||  -+-+-  ||                                                    ||")
    print("||you can claim yourself the victor only if you can bring the game to a DRAW ! XD       ||  1|2|3  ||                                                    ||")
    print("===========================================================================================================================================================")


# definitions---------------

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
            time.sleep(0.5)
            scRefresh()
            continue
        if not (inpVal >= 1 and inpVal <= 9):
            print("the move can only be between 1-9")
            time.sleep(0.7)
            scRefresh()
            continue
        else:
            break
    return inpVal

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
        print("OH NOH! You have won the game! ;=;")
        exitSeq()
    elif aiWon():
        print("OH NOOOO! You have lost to a bot with (IQ lvl < 0!)! >,<")
        exitSeq()
    elif boardFull():
        print("Amazin'! You have brought the game to a DRAW! YAYYY!!!~ xD")
        exitSeq()
    else:
        return False

def boardFull():
    if " " in board:
        return False
    else:
        return True

def exitSeq():
    exitQ = input("Do you want to  Retry [R] or Exit [E]: ").upper()
    if exitQ == "E":
        exit()
    elif exitQ == "R":
        resetBoard()
        mainGame()
    else:
        print("Please input a valid choice!")
        time.sleep(0.5)
        scRefresh()
        exitSeq()

def resetBoard():
    global board
    del board[:]
    board = [" "] * 10
    board[0] = "something other than nothing"

def mainGame():
    scRefresh()
    whoFirst = (input("Who goes first?[B=Bot/P=Player] : ")).upper()
    if whoFirst == "B":
        aiPlayFirst()
    elif whoFirst == "P":
        userPlayFirst()
    else:
        print("please input a valid choice!")
        time.sleep(0.5)
        mainGame()


#Execution----------------------

input("Please press [Alt + Enter] before we begin! *Important*")
mainGame()
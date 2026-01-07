import time
import random
skip = input("do you want to skip the start yes or no:  ")
if skip == "no":
    print("this is rock paper scissors it is not rigged i promise")
    time.sleep(2)
    print("basicaly it will ask rock, paper, or scissors")
    time.sleep(2)
    print("the computor pick before you guess so its not rigged")
    time.sleep(2)
    game = random.randint(1, 3)
    player = input("pick rock paper or scissors:  ")
if player == "rock":
    game = 1
    print("the computor picked rock go agian restart the game")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 1
    print(" the computor pick rock you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 1
    print("the computor pick rock you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "rock":
    game = 2
    print("the computor pick paper you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 2
    print("the computor pick paper you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 2
    print("the computor pick paper you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "rock":
    game = 3
    print("the computor pick scissors you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 3
    print("the computor pick scissors you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 3
    print("the computor pick scissors go agian restart the game")
    play_agian = input("do you want to play agian yes or no:   ")
else:
    print("invalid input restart the game")
    play_agian = input("do you want to play agian yes or no:   ")
    if skip == "yes":
        game = random.randint(1, 3)
player = input("pick rock paper or scissors:  ")
if player == "rock":
    game = 1
    print("the computor picked rock go agian restart the game")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 1
    print(" the computor pick rock you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 1
    print("the computor pick rock you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "rock":
    game = 2
    print("the computor pick paper you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 2
    print("the computor pick paper you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 2
    print("the computor pick paper you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "rock":
    game = 3
    print("the computor pick scissors you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 3
    print("the computor pick scissors you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 3
    print("the computor pick scissors go agian restart the game")
    play_agian = input("do you want to play agian yes or no:   ")
else:
    print("invalid input restart the game")
play_agian = input("do you want to play agian yes or no:   ")
if play_agian == "no":
    quit()
elif play_agian == "yes":
      game = random.randint(1, 3)
player = input("pick rock paper or scissors:  ")
if player == "rock":
    game = 1
    print("the computor picked rock go agian restart the game")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 1
    print(" the computor pick rock you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 1
    print("the computor pick rock you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "rock":
    game = 2
    print("the computor pick paper you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 2
    print("the computor pick paper you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 2
    print("the computor pick paper you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "rock":
    game = 3
    print("the computor pick scissors you win restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "paper":
    game = 3
    print("the computor pick scissors you lose restart to play agian")
    play_agian = input("do you want to play agian yes or no:   ")
elif player == "scissors":
    game = 3
    print("the computor pick scissors go agian restart the game")
    play_agian = input("do you want to play agian yes or no:   ")
else:
    print("invalid input restart the game")
    play_agian = input("do you want to play agian yes or no:   ")
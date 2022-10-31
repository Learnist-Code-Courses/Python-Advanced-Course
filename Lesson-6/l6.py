# Lesson 6

import random

name = ""
def main():
    hello()
    play_games()
    goodbye()

def hello():
    print("Hello player! What's your name?")
    name = input()
    print("Welcome " + name + "!")

def goodbye():
    print("Thank you for playing! Please come back soon :)")

def play_games():
    time_to_go = False
    while(time_to_go == False):
        print("Here at the arcade we have two games: 1: a fun guessing game, 2: rock paper scissors!")
        print("Say which game you want to play")
        print("(say goodbye if you want to leave)")

        player_input = input()

        if player_input == "1":
            guessing_game()
        elif player_input == "2":
            rock_paper_scissor()
        elif player_input == "goodbye":
              time_to_go = True
        else:
              print("Hmmm... I'm not sure what you mean by that...")
 
def rock_paper_scissor():

    print("Rock, paper, or scissor?")

    alternatives = ["rock", "paper", "scissor"]

    game_hand = random.choice(alternatives)

    answer = input()

    print("I had: " + game_hand)

    if game_hand == answer:
        print("draw!")
    elif answer == "rock" and game_hand == "scissor":
        print("You win!")
    elif answer == "paper" and game_hand == "rock":
        print("You win!")
    elif answer == "scissor" and game_hand == "paper":
        print("You win!")
    else:
        print("you loose!")


if __name__ == "__main__":
    main()

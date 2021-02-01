import random


# ask the person for their choice (rock, paper, or scissors)
# and validate that they chose a valid option
#

def play_game():
    options = ["rock", "paper", "scissors"]
    player_1_done = False

    player_1_move = ""

    score1 = 0
    score2 = 0

    for x in range(3):
        while not player_1_done:
            player_1_move = str(input("Choose your move (rock, paper, or scissors): ")).lower()
            if player_1_move not in options:
                print("Please enter a valid move.")
                continue
            else:
                # noinspection PyUnusedLocal
                player_1_done = True
                break
        # have the computer randomly select rock, paper, or scissors
        player_2_move = random.choice(options)

        print()
        print("Player 1 chooses " + player_1_move)
        print("Player 2 chooses " + player_2_move)

        # determine who the winner is
        # display the winner
        if player_1_move == "rock":
            if player_2_move == "rock":
                print("Tie!")
                print()
            elif player_2_move == "paper":
                print("Paper beats rock. +1 point for Player 2")
                print()
                score2 += 1
            elif player_2_move == "scissors":
                print("Rock beats scissors. +1 point for Player 1")
                print()
                score1 += 1
        elif player_1_move == "paper":
            if player_2_move == "paper":
                print("Tie!")
                print()
            elif player_2_move == "rock":
                print("Paper beats rock. +1 point for Player 1")
                print()
                score1 += 1
            elif player_2_move == "scissors":
                print("Scissors beat paper. +1 point for Player 2")
                print()
                score2 += 1
        elif player_1_move == "scissors":
            if player_2_move == "scissors":
                print("Scissors vs Scissors. Tie!")
                print()
            elif player_2_move == "rock":
                print("Rock beats scissors. +1 point for Player 2")
                print()
                score2 += 1
            elif player_2_move == "paper":
                print("Scissors beat paper. +1 point for Player 1")
                print()
                score1 += 1

        print("Player 1 Score:", score1, "points.")
        print("Player 2 Score:", score2, "points.")
        print()
        player_1_done = False

    if score1 > score2:
        print("Player 1 Wins!")
        print()
    elif score2 > score1:
        print("Player 2 Wins!")
        print()
    else:
        print("Tie!")
        print()

    play_again = input("Play again y/n? ").lower()

    if play_again == "y":
        play_game()
    else:
        print("Bye!")
        print()


play_game()

# best 2 out of 3
# or, give the user a choice of how many rounds they want to play
# ask the user if they want to play again

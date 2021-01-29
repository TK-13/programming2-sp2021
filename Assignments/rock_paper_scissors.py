import random

# ask the person for their choice (rock, paper, or scissors)
# and validate that they chose a valid option

options = ["rock", "paper", "scissors"]
moveP = False

score1 = 0
score2 = 0

while not moveP:
    player1 = str(input("Choose your move (rock, paper, or scissors): "))
    if not bool(player1 in options):
        print("Please enter a valid move.")
        continue
    else:
        moveP = True
        break
# have the computer randomly select rock, paper, or scissors
player2 = random.choice(options)

print("Player 1 chooses", player1)
print("Player 2 chooses", player2)

# determine who the winner is
# display the winner
if player1 == "rock":
    if player2 == "rock":
        print("Tie!")
    elif player2 == "paper":
        print("Paper beats rock. +1 point for Player 2")
        score2 += 1
    elif player2 == "scissors":
        print("Rock beats scissors. +1 point for Player 1")
        score1 += 1
elif player1 == "paper":
    if player2 == "paper":
        print("Tie!")
    elif player2 == "rock":
        print("Paper beats rock. +1 point for Player 1")
        score1 += 1
    elif player2 == "scissors":
        print("Scissors beat paper. +1 point for Player 2")
        score2 += 1
elif player1 == "scissors":
    if player2 == "scissors":
        print("Scissors vs Scissors. Tie!")
    elif player2 == "rock":
        print("Rock beats scissors. +1 point for Player 2")
        score2 += 1
    elif player2 == "paper":
        print("Scissors beat paper. +1 point for Player 1")
        score1 += 1


# best 2 out of 3
# or, give the user a choice of how many rounds they want to play
# ask the user if they want to play again
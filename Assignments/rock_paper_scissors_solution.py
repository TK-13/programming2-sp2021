import random


def determine_winner(user_choice, computer_choice):
    user_return_val = "user"
    computer_return_val = "computer"

    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win this round!")
            return user_return_val
        else:  # we know computer_choice is paper
            print("Computer wins this round!")
            return computer_return_val
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("Computer wins this round!")
            return computer_return_val
        else:  # we know computer_choice is rock
            print("You win this round!")
            return user_return_val
    else:  # we know user_choice is scissors
        if computer_choice == "rock":
            print("Computer wins this round!")
            return computer_return_val
        else:  # we know computer_choice is paper
            print("You win this round!")
            return user_return_val


def main():
    options = ["rock", "paper", "scissors"]
    play = True

    print("\nWelcome to rock, paper, scissors!\n")

    while play:
        computer_score = 0
        user_score = 0
        while user_score < 2 and computer_score < 2:

            # get user's choice
            user_choice = None
            while user_choice not in options:
                user_choice = input("Do you choose rock, paper, or scissors? \n")
                user_choice = user_choice.lower()

            # get computer's choice
            computer_choice = random.choice(options)
            print("Computer chose {0}\n".format(computer_choice))

            # determine round winner and increment score
            winner = determine_winner(user_choice, computer_choice)
            if winner == "user":
                user_score += 1
            elif winner == "computer":
                computer_score += 1

            # print score
            print("\nScore")
            print("------------")
            print("You: {0}".format(str(user_score)))
            print("Computer: {0}\n".format(str(computer_score)))

        # check who won the game
        if user_score == 2:
            print("You win the game!")
        else:
            print("The computer wins the game!")

        # ask to play again
        play_again = ""
        while play_again.lower() != 'y' and play_again.lower() != 'n':
            play_again = input("\nWould you like to play again? Type Y for yes, or N for no.\n")

        if play_again.lower() == 'y':
            play = True
        else:
            play = False


if __name__ == "__main__":
    main()


"""
PSEUDOCODE

1. ask the user for a choice until they choose a valid one
2. make the computer choose
3. check round winning conditions
4. add to score depending on winner
5. end game when someone wins best 2 out of 3
6. ask user if they want to play again
"""

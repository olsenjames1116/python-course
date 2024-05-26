from random import choice
from sys import exit
from enum import Enum


def guess_number(name='Player1'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        player_choice = int(input(
            f"\n{name}, guess which number I'm thinking of... 1, 2 or 3.\n\n"))

        if player_choice not in [1, 2, 3]:
            print("Please enter 1, 2 or 3.")
            return guess_number()

        computer_choice = int(choice('123'))

        print(f"\n{name} chose {player_choice}.")
        print(f"I was thinking about the number {computer_choice}.")

        def decide_winner():
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player_choice == computer_choice:
                player_wins += 1
                return f"\n{name} won."
            else:
                python_wins += 1
                return "\nYou lost."

        game_result = decide_winner()
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Python wins: {python_wins}")
        print(f"Your winning percentage: {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            play_again = input("\nY for Yes or Q to Quit\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉🎉🎉🎉")
            print("\nThank you for playing.")
            if __name__ == "__main__":
                exit()

    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guess_number_game = guess_number(args.name)
    guess_number_game()

from sys import exit
from guess_number import guess_number
from rps import rps


def arcade(name='Player1'):
    while True:
        print(f"\n{name}, please enter a 1, 2 or x")

        print("\nPlease choose a game:")
        print("1 = Rock Paper Scissors")
        print("2 = Guess My Number")

        choice = input("\nOr press \"x\" to exit the Arcade\n")

        if choice.lower() not in ["1", "2", "x"]:
            print("Please enter 1, 2 or x.")
            return arcade()

        def choose_game():
            if choice == '1':
                rps_game = rps(name)
                rps_game()
            elif choice == '2':
                guess_number_game = guess_number(name)
                guess_number_game()
            else:
                print("\nSee you next time!")
                print(f"\nBye {name}!")
                exit()

        choose_game()


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

    arcade_game = arcade(args.name)
    arcade_game()

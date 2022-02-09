import random

COLORS = ["red", "blue", "yellow", "green"]
NEGATIVES = ["no", "No", "n", "N"]

def generate_rand_order(options):
    """Returns a randomized list based on the values defined in COLORS """
    random_order = random.choices(options, k=4)
    return random_order

def input_parser(guess):
    """Simple parser to parse the player's guesses.
    Removes all spaces in case players use them.
    Then converts uppercase letters to lowercase and splits the user input by comma"""
    no_spaces = guess.replace(" ", "")
    parsed_guess = no_spaces.lower().split(",")
    return parsed_guess

def play_game():
    """
    Function to handle 'gameplay'. Will generate a random sequence and prompt the player to guess it.
    Returns if player has spent more than his 10 allowed turns or if the player guesses the sequence.
    """
    print("Welcome to Mastermind.\n"
          "Your task is to guess a random 4 item long sequence of red, blue, yellow and green. \n"
          "Note that colors can be used multiple times, and as such, all 4 colors are not always used.\n"
          "Example guess:\n"
          "yellow, green, red, blue\n")
    game_sequence = generate_rand_order(COLORS)
    turn = 0
    player_guess = input_parser(input("Try to guess the sequence: "))
    while True:
        if player_guess == game_sequence:
            print("Congratulations, you guessed the sequence! \n"
                  "The correct sequence was indeed %s " % game_sequence)
            return
        else:
            turn += 1
            correct_places = []
            correct_colors = 0
            temp_sequence = game_sequence.copy()  # needed to manage color guesses when multiples of same color exists

            if turn == 10:
                print("You did not guess the sequence within the 10 turn limit, you lose.")
                return

            for i in range(0, len(player_guess)):
                if player_guess[i] == game_sequence[i]:
                    correct_places.append(player_guess[i])
                if player_guess[i] in temp_sequence:
                    correct_colors += 1
                    temp_sequence.remove(player_guess[i])

            # case if guess had both correct places and correct colors
            if len(correct_places) > 0 and (correct_colors != 0):
                print("You're still not there, but %d of the colors were correct,"
                      "and you even had %d in the right place!" % (correct_colors, len(correct_places)))
                player_guess = input_parser(input("What's your next guess? "))

            # case if guess had no correct places, but some correct colors
            elif len(correct_places) == 0 and (correct_colors != 0):
                print("You're still not there, but %s of the colors were correct!" % correct_colors)
                player_guess = input_parser(input("What's your next guess? "))

            # case if nothing was guessed correctly
            else:
                print("Looks like you didnt guess anything correctly :(")
                player_guess = input_parser(input("What's your next guess? "))


if __name__ == '__main__':
    while True:  # while loop to allow multiple games without program exiting
        game_start = input("Would you like to play a game of Mastermind? Y/n \n")
        if game_start not in NEGATIVES:
            play_game()
        else:
            print("You have chosen not to play, exiting")
            exit()

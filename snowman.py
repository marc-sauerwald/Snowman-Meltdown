import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___
     /___\\
     (o o)
     ( : )
     ( : )
    """,
    # Stage 1: Bottom part starts melting
    """
      ___
     /___\\
     (o o)
     ( : )
    """,
    # Stage 2: Only the head remains
    """
      ___
     /___\\
     (o o)
    """,
    # Stage 3: Snowman completely melted
    """
      ___
     /___\\
    """
]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the word progress."""
    # Show the snowman at current stage
    print(STAGES[mistakes])

    # Build the word display with underscores for unguessed letters
    word_display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            word_display += letter + " "
        else:
            word_display += "_ "

    print("Word:", word_display)
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Display initial game state
    display_game_state(mistakes, secret_word, guessed_letters)

    # TODO: Build your full game loop here.
    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()
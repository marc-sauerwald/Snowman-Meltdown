import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum mistakes allowed (one less than total stages)
MAX_MISTAKES = len(STAGES) - 1


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


def is_word_guessed(secret_word, guessed_letters):
    """Checks if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def get_valid_guess(guessed_letters):
    """Prompts the user for a valid letter guess."""
    while True:
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_game():
    """Main game loop."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    
    print("Welcome to Snowman Meltdown!")
    print(f"The word has {len(secret_word)} letters. Save the snowman!\n")
    
    # Main game loop
    while mistakes < MAX_MISTAKES and not is_word_guessed(secret_word, guessed_letters):
        # Display current state
        display_game_state(mistakes, secret_word, guessed_letters)
        
        # Get a valid guess
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
        else:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word. The snowman is melting!\n")
    
    # Game over - display final state
    display_game_state(mistakes, secret_word, guessed_letters)
    
    # Determine outcome
    if is_word_guessed(secret_word, guessed_letters):
        print("Congratulations! You saved the snowman!")
        print(f"The word was: {secret_word}")
    else:
        print("Oh no! The snowman has completely melted!")
        print(f"The word was: {secret_word}")


if __name__ == "__main__":
    play_game()

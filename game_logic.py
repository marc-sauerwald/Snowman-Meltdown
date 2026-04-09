"""
Game logic for the Snowman Meltdown.

This module contains all game functions including display, input handling,
game loop, and replay functionality.
"""

import os
import random

from ascii_art import STAGES


# =============================================================================
# CONSTANTS
# =============================================================================

WORDS = [
    "python", "git", "github", "snowman", "meltdown",
    "programming", "keyboard", "developer", "function", "variable"
]

MAX_MISTAKES = len(STAGES) - 1

DIVIDER_WIDTH = 40


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def clear_screen():
    """Clear the terminal screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_word():
    """Select and return a random word from the word list."""
    return random.choice(WORDS)


# =============================================================================
# DISPLAY FUNCTIONS
# =============================================================================

def display_header():
    """Display the game header."""
    print("=" * DIVIDER_WIDTH)
    print("        ❄️  SNOWMAN MELTDOWN  ❄️")
    print("=" * DIVIDER_WIDTH)


def display_snowman(mistakes):
    """Display the snowman at the current melting stage."""
    print(STAGES[mistakes])


def build_word_display(secret_word, guessed_letters):
    """
    Build the word display string with revealed and hidden letters.

    Args:
        secret_word: The word to guess.
        guessed_letters: List of letters already guessed.

    Returns:
        String with guessed letters shown and unguessed as underscores.
    """
    display_chars = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_chars.append(letter.upper())
        else:
            display_chars.append("_")
    return " ".join(display_chars)


def display_guessed_letters(guessed_letters, secret_word):
    """
    Display the correctly and incorrectly guessed letters.

    Args:
        guessed_letters: List of all guessed letters.
        secret_word: The secret word being guessed.
    """
    correct = sorted([l.upper() for l in guessed_letters if l in secret_word])
    wrong = sorted([l.upper() for l in guessed_letters if l not in secret_word])

    if correct:
        print(f"  ✓ Correct: {', '.join(correct)}")
    if wrong:
        print(f"  ✗ Wrong:   {', '.join(wrong)}")


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display the complete current game state.

    Args:
        mistakes: Number of incorrect guesses made.
        secret_word: The word to guess.
        guessed_letters: List of letters already guessed.
    """
    clear_screen()
    display_header()
    display_snowman(mistakes)

    word_display = build_word_display(secret_word, guessed_letters)

    print("-" * DIVIDER_WIDTH)
    print(f"  Word: {word_display}")
    print(f"  Mistakes: {mistakes}/{MAX_MISTAKES}")

    if guessed_letters:
        display_guessed_letters(guessed_letters, secret_word)

    print("-" * DIVIDER_WIDTH)
    print()


def display_end_game(won, secret_word, mistakes):
    """
    Display the end game message.

    Args:
        won: Boolean indicating if the player won.
        secret_word: The word that was being guessed.
        mistakes: Total number of mistakes made.
    """
    print()
    print("=" * DIVIDER_WIDTH)

    if won:
        print("  🎉 CONGRATULATIONS! 🎉")
        print("  You saved the snowman!")
        print(f"  The word was: {secret_word.upper()}")
        print(f"  Mistakes made: {mistakes}")
    else:
        print("  💧 GAME OVER 💧")
        print("  The snowman has completely melted!")
        print(f"  The word was: {secret_word.upper()}")

    print("=" * DIVIDER_WIDTH)
    print()


def display_final_stats(games_won, games_played):
    """
    Display final statistics when the player quits.

    Args:
        games_won: Number of games won.
        games_played: Total number of games played.
    """
    clear_screen()
    print()
    print("=" * DIVIDER_WIDTH)
    print("  Thanks for playing Snowman Meltdown!")
    print(f"  Final Score: {games_won}/{games_played} games won")
    print("=" * DIVIDER_WIDTH)
    print()


# =============================================================================
# INPUT VALIDATION FUNCTIONS
# =============================================================================

def validate_guess(guess, guessed_letters):
    """
    Validate the user's guess.

    Args:
        guess: The user's input string.
        guessed_letters: List of previously guessed letters.

    Returns:
        Tuple of (is_valid, error_message).
        If valid, error_message is None.
    """
    if len(guess) == 0:
        return False, "Please enter a letter."

    if len(guess) != 1:
        return False, "Please enter exactly ONE letter."

    if not guess.isalpha():
        return False, "Please enter a letter (a-z), not numbers or symbols."

    if guess in guessed_letters:
        return False, f"You already guessed '{guess.upper()}'. Try a different letter."

    return True, None


def get_valid_guess(guessed_letters):
    """
    Prompt the user for a valid letter guess.

    Args:
        guessed_letters: List of previously guessed letters.

    Returns:
        A valid single lowercase letter not previously guessed.
    """
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        is_valid, error_message = validate_guess(guess, guessed_letters)

        if is_valid:
            return guess

        print(f"  ⚠️  {error_message}\n")


def ask_play_again():
    """
    Ask the user if they want to play again.

    Returns:
        True if the user wants to play again, False otherwise.
    """
    valid_yes = ('y', 'yes')
    valid_no = ('n', 'no')

    while True:
        answer = input("  Play again? (y/n): ").strip().lower()

        if answer in valid_yes:
            return True
        if answer in valid_no:
            return False

        print("  Please enter 'y' for yes or 'n' for no.\n")


# =============================================================================
# GAME LOGIC FUNCTIONS
# =============================================================================

def is_word_guessed(secret_word, guessed_letters):
    """
    Check if all letters in the secret word have been guessed.

    Args:
        secret_word: The word to guess.
        guessed_letters: List of letters already guessed.

    Returns:
        True if all letters have been guessed, False otherwise.
    """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def process_guess(guess, secret_word, mistakes):
    """
    Process a guess and return the result.

    Args:
        guess: The guessed letter.
        secret_word: The word being guessed.
        mistakes: Current number of mistakes.

    Returns:
        Tuple of (new_mistakes, feedback_message).
    """
    if guess in secret_word:
        message = f"  ✓ Good job! '{guess.upper()}' is in the word.\n"
        return mistakes, message

    message = f"  ✗ Sorry, '{guess.upper()}' is not in the word.\n"
    return mistakes + 1, message


def play_game():
    """
    Run a single round of the Snowman Meltdown game.

    Returns:
        True if the player won, False otherwise.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    # Initial display
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"  The word has {len(secret_word)} letters. Save the snowman!\n")

    # Main game loop
    while mistakes < MAX_MISTAKES:
        if is_word_guessed(secret_word, guessed_letters):
            break

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        mistakes, feedback = process_guess(guess, secret_word, mistakes)
        display_game_state(mistakes, secret_word, guessed_letters)
        print(feedback)

    # Determine and display outcome
    won = is_word_guessed(secret_word, guessed_letters)
    display_end_game(won, secret_word, mistakes)

    return won


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main():
    """Main entry point with game loop and replay functionality."""
    clear_screen()

    games_played = 0
    games_won = 0

    while True:
        won = play_game()
        games_played += 1

        if won:
            games_won += 1

        print(f"  📊 Stats: {games_won} wins / {games_played} games played")
        print()

        if not ask_play_again():
            display_final_stats(games_won, games_played)
            break


if __name__ == "__main__":
    main()

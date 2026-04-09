import random
import os
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown", "programming", "keyboard", "developer"]

# Maximum mistakes allowed (one less than total stages)
MAX_MISTAKES = len(STAGES) - 1


def clear_screen():
    """Clears the terminal screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the word progress."""
    clear_screen()
    
    # Header
    print("=" * 40)
    print("        ❄️  SNOWMAN MELTDOWN  ❄️")
    print("=" * 40)
    
    # Show the snowman at current stage
    print(STAGES[mistakes])
    
    # Build the word display with underscores for unguessed letters
    word_display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            word_display += letter.upper() + " "
        else:
            word_display += "_ "
    
    print("-" * 40)
    print(f"  Word: {word_display}")
    print(f"  Mistakes: {mistakes}/{MAX_MISTAKES}")
    
    # Show guessed letters
    if guessed_letters:
        wrong_guesses = [l.upper() for l in guessed_letters if l not in secret_word]
        correct_guesses = [l.upper() for l in guessed_letters if l in secret_word]
        
        if correct_guesses:
            print(f"  ✓ Correct: {', '.join(sorted(correct_guesses))}")
        if wrong_guesses:
            print(f"  ✗ Wrong:   {', '.join(sorted(wrong_guesses))}")
    
    print("-" * 40)
    print()


def is_word_guessed(secret_word, guessed_letters):
    """Checks if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def get_valid_guess(guessed_letters):
    """Prompts the user for a valid letter guess with input validation."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        
        # Validate: must not be empty
        if len(guess) == 0:
            print("  ⚠️  Please enter a letter.\n")
            continue
        
        # Validate: must be exactly one character
        if len(guess) != 1:
            print("  ⚠️  Please enter exactly ONE letter.\n")
            continue
        
        # Validate: must be alphabetical
        if not guess.isalpha():
            print("  ⚠️  Please enter a letter (a-z), not numbers or symbols.\n")
            continue
        
        # Validate: must not be already guessed
        if guess in guessed_letters:
            print(f"  ⚠️  You already guessed '{guess.upper()}'. Try a different letter.\n")
            continue
        
        return guess


def display_end_game(won, secret_word, mistakes):
    """Displays the end game message."""
    print()
    print("=" * 40)
    
    if won:
        print("  🎉 CONGRATULATIONS! 🎉")
        print("  You saved the snowman!")
        print(f"  The word was: {secret_word.upper()}")
        print(f"  Mistakes made: {mistakes}")
    else:
        print("  💧 GAME OVER 💧")
        print("  The snowman has completely melted!")
        print(f"  The word was: {secret_word.upper()}")
    
    print("=" * 40)
    print()


def ask_play_again():
    """Asks the user if they want to play again."""
    while True:
        answer = input("  Play again? (y/n): ").strip().lower()
        
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("  Please enter 'y' for yes or 'n' for no.\n")


def play_game():
    """Main game loop for a single round."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    
    # Initial display
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"  The word has {len(secret_word)} letters. Save the snowman!\n")
    
    # Main game loop
    while mistakes < MAX_MISTAKES and not is_word_guessed(secret_word, guessed_letters):
        # Get a valid guess
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            # Update display first, then show message
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"  ✓ Good job! '{guess.upper()}' is in the word.\n")
        else:
            mistakes += 1
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"  ✗ Sorry, '{guess.upper()}' is not in the word.\n")
    
    # Determine outcome
    won = is_word_guessed(secret_word, guessed_letters)
    display_end_game(won, secret_word, mistakes)
    
    return won


def main():
    """Main function with replay loop."""
    clear_screen()
    
    # Statistics
    games_played = 0
    games_won = 0
    
    while True:
        # Play a round
        won = play_game()
        games_played += 1
        if won:
            games_won += 1
        
        # Show statistics
        print(f"  📊 Stats: {games_won} wins / {games_played} games played")
        print()
        
        # Ask to play again
        if not ask_play_again():
            clear_screen()
            print()
            print("=" * 40)
            print("  Thanks for playing Snowman Meltdown!")
            print(f"  Final Score: {games_won}/{games_played} games won")
            print("=" * 40)
            print()
            break


if __name__ == "__main__":
    main()

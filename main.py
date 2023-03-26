# To end the program
import sys

# User inputs a word
word = input("Enter a secret word: ")
# Stores the length of the word
wordLength = len(word)
print("You have a " + str(wordLength) + " letter word to guess.")

# String of all guessed letters
guessedLetters = ""
# String of all correctly guessed letters
remainingLetters = ""

# User can only have 6 attempts
attemptsLeft = 6

def notice(attempts):
    print("remaining invalid guesses: " + str(attempts))

# Function that prints correctly guessed letters
def hangman(display):
    # Checks each letter in the word
    for letter in word:
        # If the letter has been guessed correctly by the user
        if letter in guessedLetters:
            display += letter  # The letter is added to the blanks that will be display
        # If the letter has not been guessed yet
        else:
            display += "_"  # A blank will be displayed instead of the letter

    # Print the correctly guessed letters
    for char in display:
        print(char, end=" ")

    # If all the letters in the word have been correctly guessed by the user
    if display == word:
        print("\t---- CONGRATULATIONS")  # User wins
        sys.exit()  # Game ends
    # If the user has not guessed all letters in the word yet
    else:
        print()  # Prints new line
        remainingLetters = ""  # Restart display of letters


hangman(guessedLetters)
notice(attemptsLeft)

# Loop until user runs out of attempts
while attemptsLeft != 0:
    # User guesses a letter in the word
    guess = input("\nGuess any letter: ")
    # If the user guesses a letter correctly
    if guess in word:
        guessedLetters += guess  # Add the letter to guessedLetters
        hangman(remainingLetters)
    # If the user guesses a wrong letter
    else:
        attemptsLeft -= 1  # Decrements number of attempts left
        hangman(remainingLetters)
        notice(attemptsLeft)

# User loses
print("\n---- Sorry, you lose!")

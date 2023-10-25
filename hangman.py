import random

def select_word():
    with open("C:\\Users\\dhanu\\OneDrive\\Documents\\words.txt", "r") as file:
        words = file.readlines()
        word = random.choice(words).strip().lower()
    return word

def draw_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]
    return stages[6 - attempts]

def play_game():
    word = select_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Player 2, start guessing!")

    while attempts > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print("Guessed word:", guessed_word)
        print("Attempts left:", attempts)
        print(draw_hangman(attempts))

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            attempts -= 1

        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("Game over! You ran out of attempts. The word was:", word)

play_game()

import random
from words import words_list


def get_word():
    word = random.choice(words_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()

        # Handle guesses
        if len(guess) == 1 and guess.isalpha():  # single letter guess
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good Job!!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                word_completion = "".join(word_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  # full word guess
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Incorrect guess.")

        # Display hangman and word progress
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you got the word right!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

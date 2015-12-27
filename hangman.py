import random
import requests
import sys

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def hangman():
    while True:
        word = random.choice(WORDS).decode("utf-8")
        if len(word) > 5:
            continue
        elif len(word) < 3:
            continue
        else:
            break
    print(word)

    print("Let's play hangman!")
    placeholders = len(word) * "_ "
    print(placeholders)
    while True:
        letter = input("Guess a letter: ")

        if letter in word:
            print("You guessed a letter!")
            place = word.index(letter)
            new_placeholder = placeholders.split(" ")
            places = find(word, letter)
            for place in places:
                new_placeholder[place] = letter
            placeholders = " ".join(new_placeholder)
            print(placeholders)
            guess_word = input("Would you like to guess the word? Y/n?: ")
            if guess_word != "n":
                word_guess = input("Your guess?: ")
                if word_guess == word:
                    print("You guessed it!!!")
                    play_again = input("Play again Y/n?: ")
                    if play_again != "n":
                        hangman()
                    else:
                        sys.exit()
                else:
                    continue
            else:
                continue

        elif letter not in word:
            print("Sorry that letter isn't in the word!")
            print(placeholders)
        else:
            print("Sorry my word was {}".format(word))
            sys.exit()
hangman()

import random

def star(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_word = ""
    for char in word:
        if char in alphabet:
            new_word += "*"
        else:
            new_word += char
    return new_word

def find(word, letter):
    found = []
    for pos, char in enumerate(word):
        if char == letter:
            found.append(pos)
    if found:
        return found
    return False

GALLOWS = ["""

  +---+
  |   |
      |
      |
      |
      |
=========""", """

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

def hangman():
    with open("dict.txt", "r") as f:
        lines = [word for word in f.read().split("\n") if len(word) != 0]
        word = random.choice(lines)
    guessed = []
    guesses = 6
    hidden = list(star(word))
    while guesses != 0:
        if hidden == list(word):
            print("You win! The word was " + word)
            break
        print(GALLOWS[6-guesses])
        print("\n\nThe word is " + "".join(hidden))
        print("You have currently used the letters: " + ", ".join(guessed))
        print("You have " + str(guesses) + " guesses left.")
        guess = input("Guess a letter \n").lower()
        if not find(word, guess):
            guesses -= 1
        elif guess in guessed:
            print("\n\nYou have already guessed the letter " + guess)
        else:
            for pos in find(word, guess):
                hidden[pos] = guess
        if guess not in guessed:
            guessed.append(guess)
    print("You lose! The word was " + word)    
        
        
        
hangman()

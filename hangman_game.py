
import random

stages = [
    """ 
    """,
    """




    =========
    """,
    """
      |
      |
      |
      |
      |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
    =========
    """
]

def hangman_game(words):
    word = random.choice(words)
    word1=word.lower()
    attempts=9
    found=set()
    gives=set()
    runda=0

    print("Guess the word! - Enter a letter\n")
    while(attempts>0):
        print(f'Number of remaining attempts: {attempts}')
        for i in range(len(word)):
            if word1[i] in found:
                print(word[i], end=' ')
            else:
                print('_', end=' ')

        print('\n')
        if set(found) == set(word1):
            print("Well done! Game over.")
            exit()


        res = input()
        print("\n")

        if not res.isalpha():
            print("That is not a letter! Try again.\n")
            continue

        while len(res)!=1:
            res = input("Too many characters - Enter one letter again.\n")
        res= res.lower()


        if res in gives:
            print("You already entered that letter - Enter a letter again.\n")
            continue
        gives.add(res)

        if res in word1:
           found.add(res)
        else:
            attempts-=1
            runda+=1
            print(stages[runda])



    print(f'You lost. The correct word was: {word}')



words = [
    "komputer",
    "parasol",
    "dynia",
    "zegarek",
    "wulkan",
    "księżyc",
    "kalafior",
    "rower",
    "smok",
    "teatr"
]
if __name__ == "__main__":
    hangman_game(words)
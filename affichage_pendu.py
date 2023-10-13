

import sys
import os

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def affichage(num: int) -> str:
    if not str(num).isdigit():
        print("/!\ affichage_pendu.py => affichage() : la variable 'num' n'est pas un numérique")
        sys.exit(0)
    
    if num < 0 or num > 6:
        print("/!\ affichage_pendu.py => affichage() : la valeur demander n'est pas dans l'interval prévu :", num)
        sys.exit(0)

    _ = os.system('clear')
    print("JEU DU PENDU - V1.1")
    print("")
    print(hangman_pics[num])
import json
import random
import pyinputplus
from colorama import Fore


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']    # Acceptable answers
file = open('nouns.json')
dict_nouns = json.load(file)                    # Loads the entire dictionary
list_nouns = dict_nouns['nouns'][:]             # List of words
word = random.choice(list_nouns).upper()        # Random one word
game = ['_' for x in range(len(word))]          # List letters in word with char "_". On start game is only "_"
fails = 0                                       # Value of incorrect letters
list_fails = []
color_index = []


while True:
    print(f'\nFails: ', end='')
    for x in list_fails:                                                      # Print fails - red [bad letter]
        print(f'[{Fore.RED}{x}{Fore.RESET}]', end='')
    for y in range(10 - fails):
        print(f'[{Fore.GREEN}*{Fore.RESET}]', end='')                           # Print chance - green [*]
    print('      ')

    if fails == 10:                                                             # Game Over
        print(f'You Lose !  -  Passwort = {word}')
        break

    for i, let in enumerate(game):
        if i in color_index:
            print(f'{Fore.BLUE}{let}{Fore.RESET}', end=' ')                     # Print last guessed letter in color
        else:
            print(let, end=' ')                                                 # Print other guessed letters

    if '_' not in game:                                                         # If all letters guessed
        print(f'\n---> You Win! - fails = {fails} <---')
        break
    else: print(end='        ')

    answer = pyinputplus.inputChoice(letters, prompt='enter a letter: ')        # Answer a player
    letters.remove(answer)                                                      # Delete a letter from the list of answers

    table_word = []
    color_index = []
    for z in word:                                                              # Copy word
        table_word.append(z)

    if answer in word:                                                          # If letter of answer is in word
        for x in range(word.count(answer)):
            ind = table_word.index(answer)
            table_word[ind] = '-'                                               # Letter guessed. Char = "-"
            game[ind] = answer                                                  # Show letter in word
            color_index.append(ind)

    else:
        fails += 1                                                              # Add 1 fail
        list_fails.append(answer)



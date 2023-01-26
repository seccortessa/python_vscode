import random
from hangman_words import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

stages = list(reversed(stages))


print("Bienvenido al juego del ahorcado")

chosen_word = random.choice(word_list)
chosen_word_list =[]

hidden_word = ""
hidden_word_list = []
# print(chosen_word)
contador_death = 0




for i in chosen_word:
    hidden_word += "_"
    hidden_word_list.append("_")
    chosen_word_list.append(i)
game_over = False

actual_stage = stages[contador_death]
print(hidden_word)
print()

while not game_over:
    
    char_in = input("Ingrese una letra: ").lower()

    if char_in in chosen_word:
        for char_index in range(len(chosen_word)):
            if chosen_word[char_index] == char_in:
                hidden_word_list[char_index] = chosen_word[char_index]
                hidden_word_list[char_index] = chosen_word[char_index]
    else:
        contador_death += 1
    hidden_word=""
    actual_stage = stages[contador_death]
    for i in range(len(chosen_word)):
        hidden_word += hidden_word_list[i]
    print(actual_stage)
    print(hidden_word)
    if contador_death >= 6:
        game_over = True
        print("The word was ",chosen_word)
        print("Game over, you lose")
    if hidden_word == chosen_word:
        game_over = True
        print("you win!!")
    # print(chosen_word)

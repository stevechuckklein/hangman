#1. Modify the game, so a word is selected randomly from a list of words.

#Solution: http://tinyurl.com/j7rb8or

import random

def hangman():
  word_list = ["butt", "face", "shoulder", "knee"]
  word = word_list[random.randint(0,len(word_list)-1)]
  wrong = 0
  stages = ["",
         "__________      ",
         "|        |      ",
         "|        |      ",
         "|        0      ",
         "|       /|\     ",
         "|       / \     ",
         "|               "
          ]
  rletters = list(word)
  board = ["__"] * len(word)
  win = False
  print("Welcome to Hangman")

  while wrong < len(stages) - 1:
  	print("\n")
  	msg = "Guess a letter: "
  	char = input(msg)
  	if char in rletters:
  		cind = rletters.index(char)
  		board[cind] = char
  		rletters[cind] = '$'
  	else:
  		wrong += 1
  	print((" ".join(board)))
  	e = wrong + 1
  	print("\n".join(stages[0: e]))
  	if "__" not in board:
  		print("You win!")
  		print("".join(board))
  		win = True
  		break
  if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

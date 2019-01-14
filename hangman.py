import random
def main():
  user = input("What's your name? ")
  print("Hello %s! Welcome to my Hangman game!" % user)
  print()
  word = get_word()
  word_len = len(word)
  guess = ""
  board = ["_"] * word_len
  print_board(word, word_len, board, guess)

  mistakes = 0
  while mistakes != 6:
    if "_" in board:
      guess = input("Guess a letter! ")
      print()
      guess = guess.lower()
      if guess not in word:
        mistakes += 1
        add_mistake(mistakes)
        print_board(word, word_len, board, guess)
        print()
      else:
        add_mistake(mistakes)
        print_board(word, word_len, board, guess)
        print()
    else:
      break
  if mistakes == 6:
    print("You lost :(")
    print("The word was",word)
  print("You won!!!")

def get_word():
  words = ["school", "neighborhood", "newspaper", "television", "python"]
  word_ct = len(words)
  num = random.randrange(0,word_ct - 1)
  return words[num]
  
def print_board(word, length, board, guess):
  for i in range(length):
    if word[i] == guess:
      board[i] = guess
  print(board)

def add_mistake(incorrect):
  if incorrect == 1:
    print(" O")
  elif incorrect == 2:
    print(" O")
    print(" |")
  elif incorrect == 3:
    print(" O")
    print("-|")
  elif incorrect == 4:
    print (" O")
    print("-|-")
  elif incorrect == 5:
    print(" O")
    print("-|-")
    print("/")
  elif incorrect == 6:
    print(" O")
    print("-|-")
    print("/ \\")
  print()
main()
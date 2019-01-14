import random

def main():
  print("Welcome to the guessing game!")
  print()
  num = random.randint(1,10)
  print(num)
  correct = False
  guess = input("Guess a number between 1-50: ")
  
  while not correct:
    if int(guess) == num:
      correct = True
    elif int(guess) < num:
      print("Your guess is too low...")
      guess = input("Guess again?: ")
    elif int(guess) > num:
      print("Your guess is too high...")
      guess = input("Guess again?: ")
  print()
  print("Congratulations, you guessed it!")
     
main()
import random

def main():
  print("Welcome to the dice roller!")
  rand = random.randint(1,6)
  print("You rolled a",rand)
  choice = input("Would you like to roll again? [Y/N] ")
  while choice.upper() == "Y":
    rand = random.randint(1,6)
    choice = input("Would you like to roll again? [Y/N] ")
  print("Thanks for playing!")

main()
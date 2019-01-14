def main():
  print("Welcome to Madlibs!")
  print()
  noun1 = input("enter a plural noun: ")
  adj1 = input("enter an adjective: ")
  noun2 = input("enter a plural noun: ")
  adj2 = input("enter an adjective: ")
  noun3 = input("enter a singular noun: ")
  adj3 = input("enter a positive adjective: ")
  person = input("enter a person's name: ")

  print()
  print("Here's a poem for you!")
  print()

  print(noun1,"are",adj1)
  print(noun2,"are",adj2)
  print(noun3,"is",adj3)
  print("and so is",person)

main()
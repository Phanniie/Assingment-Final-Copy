import time 
import os
import sys
import room1
import main

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.06)

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.07)
  value = input()  
  return value  

def clear_console():
    os.system('clear')

#Options of what people can answer
answer_A = ["A", "a"]
answer_B = ["B", "b"]
yes = ["yes", "YES", "yea", "y", "Y", "Yes"]
no = ["no", "NO", "nah", "n", "N", "No"]

#For if people type things not required/in the system
required = ("I'm sorry, I don't understand what you want to do. Please choose one of the options provided. \n\n")

#The optioins provided in MENU
def menu():
  typingPrint("""Would you like to: \n A. Quit Game
 B. Learn How To Play Game""")
  choice = input('\n>>> ')
  if choice in answer_A:
    time.sleep(1)
    clear_console()
    typingPrint("Thank you for playing!")
    time.sleep(2)
    main.restart()

  elif choice in answer_B:
    typingPrint("\nIn each room, you are given 2-3 doors with numbers on them to choose from. ")
    time.sleep(0.5)
    typingPrint("(Hint: The numbers could signify your fate ;) )\n\n")
    time.sleep(1)
    typingPrint("All doors are locked, however, if you play our little game and win, you get to open ONE door. ")
    time.sleep(0.5)
    typingPrint("Make your way through these doors to get to the exit where you will win your $1 million!\n\n")
    typingPrint("*Disclaimer: ")
    time.sleep(0.5)
    typingPrint("You might find yourself in some rooms you've already been in before. ")
    time.sleep(0.5)
    typingPrint("If this were to happen, the only way to open the doors is if you play our game again or quit. ")
    time.sleep(1.5)
    typingPrint("\n\nGood Luck!")
    time.sleep(2)
    clear_console()
    question()

  else:
    print(required)
    time.sleep(1.5)
    clear_console()
    menu()

#If people are ready to proceed into the game 
def question():
  typingPrint("Do you wish to proceed? yes/no ")
  choice = input(">>> ")
  if choice in yes:
    time.sleep(1)
    clear_console()
    starting()
    clear_console()
    room1.room_1()
    
  elif choice in no:
    time.sleep(1)
    clear_console()
    menu()

  else:
    typingPrint(required)
    time.sleep(1.5)
    clear_console()
    question()


def starting():
  time.sleep(1)  
  typingPrint("starting in 3..")
  time.sleep(1)
  typingPrint("2..")
  time.sleep(1)
  typingPrint("1..")
  time.sleep(1)
  clear_console()

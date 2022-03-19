import time
import os
import sys
import start

#Type writing effect for print statements
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.06)

#Type writing effect for input statements
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.07)
  value = input()  
  return value  

#Used to clear screen
def clear_console():
    os.system('clear')

#Options of what people can answer
yes = ["yes", "YES", "yea", "y", "Y", "Yes"]
no = ["no", "NO", "nah", "n", "N", "No"]

#For if people type things not required/in the system
required = ("I'm sorry, I don't understand what you want to do. Please choose one of the options provided. \n\n")

#The beginning
def intro():
  name = typingInput('What is your name? >>> ')
  time.sleep(1)
  clear_console()
  typingPrint("Hi " +name+  ", you have just been kidnapped :D")
  time.sleep(1)
  typingPrint("\n\nFear not! ")
  time.sleep(0.5)
  typingPrint("Because YOU have been CHOSEN to compete in our game to WIN $1 million! (yayy)\n\n")
  time.sleep(1.5)
  start.participate()

if __name__ == '__main__':
  intro()

#What will appear after you die, quit game, of complete the game
def restart():
  typingPrint("\n\nWould you like to play again? yes/no")
  choice = input('\n>>> ')

  if choice in no:
    clear_console()
    time.sleep(1.5)
    typingPrint("The screen will now clear itself in 3..")
    time.sleep(1)
    typingPrint("2..")
    time.sleep(1)
    typingPrint("1..")
    time.sleep(1)
    clear_console()
    sys.exit()

  elif choice in yes:
    clear_console()
    time.sleep(1)
    intro()

  else:
    typingPrint(required)
    time.sleep(1)
    restart()

if __name__ =='__main__':
  restart()
import time 
import os
import sys
import menu
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
yes = ["yes", "YES", "yea", "y", "Y", "Yes"]
no = ["no", "NO", "nah", "n", "N", "No"]
hint = ["HINT", "hint", "Hint"]
MENU = ["MENU", "menu", "Menu"]
ready = ["READY", "ready", "Ready"]

#For if people type things not required/in the system
required = ("I'm sorry, I don't understand what you want to do. Please choose one of the options provided. \n\n")

#Asking if player wants to participate
def participate():
  choice = typingInput("Would you like to paticipate? yes/no >>> ")
  time.sleep(1)
  if choice in yes:
    typingPrint("Yay! I knew you would say yes :D")
    time.sleep(0.5)
    typingPrint("\n\nLets get started shall we!")
    time.sleep(1.5)
    clear_console()
    queue()

  elif choice in no:
    time.sleep(0.5)
    typingPrint("oh...")
    time.sleep(1)
    typingPrint("I really thought you would've said yes :(")
    time.sleep(1.5)
    typingPrint("\n\nOh well! ")
    time.sleep(0.5)
    typingPrint("You're already here so bad luck! You're going to play anyways >:D")
    time.sleep(2)   
    clear_console()
    queue()

  else:
    typingPrint(required)
    time.sleep(1.5)
    participate()

    
#The menu
def queue():
  time.sleep(0.5)
  print('*BOOM*')
  time.sleep(1.5)
  typingPrint('\nYou are now magically in the queue room! ')
  time.sleep(0.5)
  typingPrint("If you wish to start, say READY. If you wish to know how to play the game, say MENU") 
  choice = input('\n>>> ')
  
  if choice in ready:
    time.sleep(0.5)
    clear_console()
    menu.starting()
    clear_console()
    room1.room_1()

  elif choice in MENU:
    time.sleep(1)
    clear_console()
    menu.menu()

  else:
    typingPrint(required)
    time.sleep(1.5)
    clear_console()
    queue()
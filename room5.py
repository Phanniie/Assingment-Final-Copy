import time
import os
import sys
import room2
import menu

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

#For if people type things not required/in the system
required = ("I'm sorry, I don't understand what you want to do. Please choose one of the options provided. \n\n")

#Room 5
def room_5():
  clear_console()
  time.sleep(0.5)
  typingPrint('You are now in room 5.')
  time.sleep(1)
  typingPrint("\n\nHmm. There seems to be a bug in our system that we don't have a game to play D: ")
  time.sleep(0.5)
  typingPrint("Oh well! There is only one door you can go through anyways which seems to be: \n")
  time.sleep(0.5)
  print(""" Door 666. Located on your left""")
  time.sleep(1)
  typingPrint("\n\nHere's the situation, I'll give you a free opportunity to go through it! Will you go through the door? yes/no")
  choice = input("\n>>> ")
  if choice in yes:
    time.sleep(1)
    room2.room_2()

  elif choice in no:
    rejection()
      
  else:
    typingPrint(required)
    time.sleep(1)
    room_5() 

#Saving they have to go through the door
def rejection():
  typingPrint("\nWell... this is quite awkward. Unfortunately for you, the only way to leave this room is to go through door 666. Trust me, you'll be fine! Do you wish to go through door 666? yes/no")

  choice = input("\n>>> ")
  if choice in yes:
    typingPrint("\nSee, what did I say! You should really learn how to trust people more!")
    time.sleep(2)
    room2.room_2()

  elif choice in no:
    rejection()

import time
import os
import sys
import room3
import main
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
answer_1 = ["1", "ONE", "one","Door 1","door 1"]
answer_2 = ["2", "TWO", "two","Door 2", "door 2"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
David = ["David", "david", "DAVID"]
hint = ["HINT", "hint", "Hint"]

#For if people type things not required/in the system
required = ("I'm sorry, I don't understand what you want to do. Please choose one of the options provided. \n\n")

#Room 2
def room_2():
  clear_console()
  time.sleep(0.5)
  typingPrint("You've made it to room 2! Would you like to: ")
  time.sleep(1)
  print("""\n A. Play a Game
 B. Go to MENU""")
  choice = input('>>> ')
  if choice in answer_A:
    time.sleep(1)
    clear_console()
    riddle()

  elif choice in answer_B:
    clear_console()
    menu.menu()

  else:
    typingPrint(required)
    time.sleep(1.5)
    room_2()

#Mini Game for room 2
def riddle():
  typingPrint("The game for this room is 'Knowing your riddles'! (Don't worry, it shouldn't be too hard). ")
  time.sleep(0.5)
  typingPrint("Like usual, if you win, you get to open one of the doors. However, if you lose, you die.")
  time.sleep(2)
  typingPrint("\n\nGood Luck!")
  time.sleep(2)
  clear_console()
  typingPrint("David’s parents have three sons: Snap, Crackle, and... who? \n(Enter HINT if you need help)\n")
  choice = input(">>> ")
  if choice in David:
    typingPrint("\nYay you got it! ")
    time.sleep(0.5)
    typingPrint("See, it's not too bad right?")
    time.sleep(1.5)
    room_2_doors()

  elif choice in hint:
    typingPrint("\nLook carefully at the first half of the question ;)\n")
    time.sleep(1.5)
    clear_console()
    riddle()

  else:
    typingPrint("\nHm, it was worth a try(?) ")
    time.sleep(0.5)
    typingPrint("But, I guess the question was just a little too difficult for you huh? :( ")
    time.sleep(1.5)
    clear_console()
    typingPrint('*Two people – seeming to be parents, walks into the room.')
    time.sleep(0.5)
    typingPrint('They look at you in digust and anger whilst saying: "How dare you forget your own brother!".')
    time.sleep(0.5)
    typingPrint('You feel their wrath and the next thing you know it...')
    time.sleep(1)
    typingPrint("YOU DIED*")
    time.sleep(2)
    clear_console()
    typingPrint("Thank you for Playing!")
    time.sleep(2)
    main.restart()

#Doors options for room 2
def room_2_doors():
  time.sleep(0.5)
  typingPrint(" Your reward for completing it is... ")
  time.sleep(1)
  typingPrint("choosing which door you want to go through! There are 2 doors.")
  print("""\n Door 1. Located on your left
 Door 2. Located straight ahead """) 
  time.sleep(1)
  typingPrint("\nDo you wish to go through door one or two?")
  choice = input("\n>>> ")
  if choice in answer_1:
    typingPrint('\nDamn, you must have quite the bad luck to lose so quickly.')
    time.sleep(0.5)
    typingPrint("\n\nYOU DIED! :D")
    time.sleep(2)
    clear_console()
    typingPrint("Thank You for Playing!")
    time.sleep(2)
    main.restart()

  elif choice in answer_2:
    time.sleep(1)
    room3.room_3()
    
  else:
    typingPrint(required)
    clear_console()
    room_2_doors()


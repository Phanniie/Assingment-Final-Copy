import time
import os
import sys
import room1
import room5
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
answer_3 = ["3", "THREE", "three","Door 3","door 3"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

#For if people type things not required/in the system
required = ("I'm sorry, I don't understand what you want to do. Please choose one of the options provided. \n\n")

#Room 4
def room_4():
  clear_console()
  time.sleep(0.5)
  typingPrint("You are now in room 4. Would you like to:")
  time.sleep(1)
  print("""\n A. Play a Game
 B. Go to MENU""")
  choice = input('>>> ')
  if choice in answer_A:
    time.sleep(1)
    clear_console()
    knowledge()

  elif choice in answer_B:
    clear_console()
    menu.menu()

  else:
    typingPrint(required)
    time.sleep(1)
    room_4()

#Mini Game for room 4
def knowledge():
  typingPrint("This room will require your knowledge! ")
  time.sleep(0.5)
  typingPrint("Because the game for this room is 'Two Truths, One Lie!'")
  time.sleep(1.5)
  clear_console()
  typingPrint("Just like its name, there are two truths and one lie.")
  time.sleep(0.5)
  typingPrint(" Your job is to find out which one is the LIE")
  time.sleep(1)
  print("""\n\n A. The last words of the MARS rover Opportunity was "My battery is low and it's getting dark" \n       
 B. The city of Canberra became the Australian Capital City because Melbourne and Sydney wouldn't stop arguing over who should get it \n
 C. According to NASA, The Great Wall of China can be seen from Space\n\n""")
  time.sleep(0.5)
  typingPrint("(Enter HINT if you need help!)\nWhich one do you think is the lie? (a/b/c) ")
  choice = input('>>> ')
  
  if choice in answer_A:
    typingPrint("WRONG!")
    time.sleep(1)
    typingPrint(" This is actually true! In fact, Opportunity is most known for this quote! (and because it's one of NASA most succesful rover to date) \n\n")
    time.sleep(1)
    typingPrint("Well...")
    time.sleep(0.5)
    typingPrint("I guess this is where we say goodbye (｡•́︿•̀｡)")
    time.sleep(1.5)
    clear_console()
    typingPrint("*Freezing air begins to fill the room. You stand there as lights begin to switch off slowly. You whisper to yourself, 'It's cold and it's getting dark T^T'*")
    time.sleep(1)
    typingPrint("\n\nYOU DIED")
    time.sleep(2)
    clear_console()
    typingPrint("Thank you for Playing!")
    time.sleep(2)
    main.restart()

  elif choice in answer_B:
    typingPrint("WRONG!")
    time.sleep(1)
    typingPrint(" This is actually true! In fact, Sydney and Melbourne had to compromise resulting in the establishment of Canberra! \n\n")
    time.sleep(1)
    typingPrint("Well...")
    time.sleep(0.5)
    typingPrint("I guess this is where we say goodbye (｡•́︿•̀｡)")
    time.sleep(1.5)
    clear_console()
    typingPrint("*You see a Kangaroo with boxing gloves enter the room. It looked angry. ")
    time.sleep(0.5)
    typingPrint("As you run around the room trying to find an escape, you feel something hard hit the back of your head.*")
    time.sleep(1)
    typingPrint("\n\nYOU DIED")
    time.sleep(2)
    clear_console()
    typingPrint("Thank you for Playing!")
    time.sleep(2)
    main.restart()

  elif choice in answer_C:
    typingPrint("CORRECT!")
    time.sleep(1)
    typingPrint(" You must know you stuff!\n\n")
    time.sleep(1.5)
    typingPrint("Time for my favourite part! ")
    time.sleep(1)
    room_4_doors()

  elif choice in hint:
    typingPrint("Fine, because you asked so nicely, I'll give you a 50/50 chance! The answer it either A or C")
    time.sleep(1.5)
    clear_console()
    knowledge()

  else:
    typingPrint(required)
    time.sleep(1.5)
    clear_console()
    knowledge()

#Door options for room 4
def room_4_doors():
  typingPrint('There are three doors you can go through.')
  time.sleep(0.5)
  print("""\n Door 1. Located on your left
 Door 2. Located straight ahead  
 Door 3. Located on your right""")
  typingPrint("\nDo you wish to go through door one, two, or three?")
  choice = input('\n>>> ')
  if choice in answer_1:
    time.sleep(1)
    room5.room_5()

  elif choice in answer_2:
    typingPrint("\nYou opened the door to see a bright white light on the other side... without any hesitation, you walked towards it happily.")
    time.sleep(0.5)
    typingPrint("\n\nYOU DIED!")
    time.sleep(2)
    clear_console()
    typingPrint("Thank You for Playing!")
    time.sleep(2)
    main.restart()

  elif choice in answer_3:
    typingPrint("\nYOU DIED")
    time.sleep(2)
    typingPrint("\n\nJust kidding! Did I get you?!")
    time.sleep(1)
    clear_console()
    typingPrint('You enter a pitch black corridor. You have no idea where you are walking, however, you eventually run into a wall. While checking to see if its a dead end, you feel a door knob. ')
    room1.room_1()
    
  else:
    typingPrint(required)
    time.sleep(1.5)
    clear_console()
    room_4_doors()

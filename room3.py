import time
import os
import sys
import room6
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
answer_666 = ["666", "six hundred and sixty six","Door 666","door 666"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]

#For if people type things not required/in the system
required = ("I'm sorry, I don't understand what you want to do. Please choose one of the options provided. \n\n")

#Room 3
def room_3():
  clear_console()
  time.sleep(0.5)
  typingPrint("You are now in room 3. Do you want to:")
  time.sleep(1)
  print("""\n A. Play a Game
 B. Go to MENU""")
  choice = input('>>> ')
  if choice in answer_A:
    time.sleep(1)
    clear_console()
    math()

  elif choice in answer_B:
    clear_console()
    menu.menu()

  else:
    typingPrint(required)
    time.sleep(1)
    room_3()

#Mini Game for room 3
def math():
  typingPrint("The game for this room will be a little different! why you ask? because it involves Maths! ")
  time.sleep(0.5)
  typingPrint("I hope you've been paying attention during your math classes ;)")
  time.sleep(1.5)
  clear_console()
  typingPrint("Solve for x if: 2x-4=22\n")
  choice = input('>>> x = ')
  if choice == '13':
    typingPrint("\nYay, you got it!")
    time.sleep(0.5)
    typingPrint(" Good job friend. You must be one smart fellow at school! Now, enough with the compliments. Back to the doors :D\n\n")
    time.sleep(1)
    room_3_doors()

  else:
    typingPrint("Ah... maybe you should've paid more attention during class ┐(´～｀)┌")
    time.sleep(1.5)
    clear_console()
    typingPrint("This is one of the boring deaths but...")
    time.sleep(0.5)
    typingPrint("*After failing the math question, you were forced to learn everything relating to maths. After about 10 minutes, you started to experience a brain overload*")
    time.sleep(1)
    typingPrint("\n\nYOU DIED")
    time.sleep(2)
    clear_console()
    typingPrint("Thank You for Playing!")
    time.sleep(2)
    main.restart()

#Door options for room 3
def room_3_doors():           
  typingPrint("There are three doors you can go through.")
  time.sleep(0.5)
  print("""\n Door 1. Located on your left
 Door 666. Located straight ahead
 Door 2. Located on your right""")
  typingPrint("\nDo you wish to go through door one, two, or 666")
  choice = input('\n>>> ')
  if choice in answer_1:
    typingPrint("\nHmm...")
    time.sleep(0.5)
    typingPrint("I'm afraid you won't be getting your $1 million today.")
    time.sleep(0.5)
    typingPrint("Or ever...")
    time.sleep(1)
    typingPrint("\n\nYOU DIED!")
    time.sleep(2)
    clear_console()
    typingPrint("Thank You for Playing!")
    time.sleep(2)
    main.restart()

  elif choice in answer_2:
    time.sleep(1)
    room6.room_6()

  elif choice in answer_666:
    typingPrint("\nHehe, ")
    time.sleep(0.5)
    typingPrint("I don't know what you expected with this door but, Satan has come to collect your soul :D")
    time.sleep(0.5)
    typingPrint("\n\nYOU DIED! (In the arms of satan </3)")
    time.sleep(2)
    clear_console()
    typingPrint("Thank You for Playing!")
    time.sleep(2)
    main.restart()

  else:
    typingPrint(required)
    time.sleep(1)
    room_3()

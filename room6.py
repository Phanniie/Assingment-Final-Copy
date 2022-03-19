import time
import os
import sys
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
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_666 = ["666", "six hundred and sixty six","Door 666","door 666"]
answer_777 = ["777", "seven hundred and seventy seven","Door 777","door 777"]
hint = ["HINT", "hint", "Hint"]

#For if people type things not required/in the system
required = ("I'm sorry, I don't understand what you want to do. Please choose one of the options provided. \n\n")

#Room 6
def room_6():
  clear_console()
  time.sleep(0.5)
  typingPrint("Woah! I'm surprised, you actually made it to room 6! ")
  time.sleep(0.5)
  typingPrint("*Spoiler Alert!* This is the last room before victory! ")
  time.sleep(1)
  typingPrint("Would you like to:")
  time.sleep(0.5)
  print("""\n A. Play a Game
 B. Go to MENU""")
  choice = input('>>> ')
  if choice in answer_A:
    time.sleep(1)
    clear_console()
    number()

  elif choice in answer_B:
    clear_console()
    menu()

  else:
    typingPrint(required)
    time.sleep(10)
    room_6()

#Mini Game for room 6
def number():
  typingPrint("Welcome to your final game! ")
  time.sleep(0.5)
  typingPrint("The game we will playing is...")
  time.sleep(1)
  typingPrint("Guess the number! (Yayy)")
  time.sleep(2)
  clear_console()
  typingPrint("Between 0-5, ")
  time.sleep(0.5)
  typingPrint("""which number am I thinking of?
(Enter HINT if you need help)\n""")
  choice = input(">>> ")
  
  if choice in hint:
    typingPrint("\nBecause this is the last game, the only hint I can give you is that it is 3 or above.")
    time.sleep(1.5)
    clear_console()
    number()
    
  elif choice != '4':
    time.sleep(1)
    typingPrint("Noo! you were so close T^T")
    time.sleep(0.5)
    typingPrint("\n\nYou were a good contestant. But, I guess not good enough...")
    time.sleep(0.5)
    typingPrint("This is honestly so sad. ")
    time.sleep(1.5)
    typingPrint("\n\nGoodbye my friend :( It was fun.")
    time.sleep(1.5)
    clear_console()
    typingPrint("*A big black ball falls into the middle of the room. With closer inspection, you see numbers in big red text counting down from ")
    time.sleep(1)
    typingPrint("5..")
    time.sleep(1)
    typingPrint("4..")
    time.sleep(1)
    typingPrint("3..")
    time.sleep(1)
    typingPrint("2..")
    time.sleep(1)
    typingPrint("1..")
    time.sleep(2)
    clear_console()
    typingPrint("*BOOMMM*")
    time.sleep(1)
    typingPrint("\n\nYOU DIED")
    time.sleep(2)
    clear_console()
    typingPrint("Thank you for Playing!")
    time.sleep(1.5)
    main.restart()

  elif choice == '4':
    time.sleep(1)
    typingPrint("\nYAYYY! ")
    time.sleep(1)
    typingPrint("You actually got it! I'm so proud of you! ")
    time.sleep(0.5)
    typingPrint("The final thing left to do now is choose a door!\n\n")
    room_6_doors()

  else:
    typingPrint(required)
    time.sleep(1.5)
    clear_console()
    number()

#Door options for room 6
def room_6_doors():
  time.sleep(1)
  typingPrint("Which door will you choose?\n")
  time.sleep(0.5)
  print(""" Door 777. Located in front of you on your right
 Door 666. Located in front of you on your left""")
  choice = input(">>> ")
  if choice in answer_666:
    typingPrint('\nNoo! ')
    time.sleep(0.5)
    typingPrint("\nWhy did you have to choose this door! You were sooooo close T^T")
    time.sleeo(0.5)
    typingPrint("I really thought you would be the first to win!")
    time.sleep(1)
    typingPrint("\n\nGoodbye my friend :( It was fun.")
    time.sleep(1.5)
    clear_console()
    typingPrint("\n\n*A big black hooded figure appears before you. Satan has come to collect your soul*")
    time.sleep(2)
    typingPrint('\n\nYOU DIED')
    time.sleep(2)
    clear_console()
    typingPrint("Thank You for Playing!")
    time.sleep(2)
    main.restart()

  elif choice in answer_777:
    typingPrint("\nCongratulations young one! ")
    time.sleep(0.5)
    typingPrint("You survived our game! As promised, you shall now get your $1 million!")
    time.sleep(1)
    clear_console()
    typingPrint("*You are now magically in the celebration room! With balloons and confetti everywhere, you are handed a big, heavy brief case the size of a small suitcase. You open it to see stacks of $100 bills all worth up to $1 million. As you pick one stack up to look, you realise something is off. You indeed got your $1 million...")
    time.sleep(0.5)
    typingPrint("just in counterfiet money... :D *")
    time.sleep(2)
    clear_console()
    typingPrint("Thank You for Playing!")
    time.sleep(2)
    main.restart()
  
  else:
    typingPrint(required)
    time.sleep(1)
    room_6()

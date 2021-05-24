import random
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print("Welcome to the 'Guess The Number' game!")
    time.sleep(3)
    print("Coded by Mehmet Akif VARDAR")
    time.sleep(3)
    print("https://mehmetakifvardar.com")
    time.sleep(3)
    diff = int(input("Please choose the difficulty of the game:\n"
          "(1) Easy - 0,50\n"
          "(2) Medium - 0,150\n"
          "(3) Hard - 0,300\n"
          "Enter the number of difficulty you choose: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if diff == 1:
        life = 10
        print("You have "+(str(life))+" life points. Guess the correct number before your life points reset.\n")
        a = random.randint(0,50)
        b = int(input("Guess the number between 0,50!: "))
        while True:
            if b == a:
                print("Congratz! You found it!")
                key = input('Enter any key to play again: ')
                if key:
                    os.system('cls' if os.name=='nt' else 'clear')
                    break
            elif b < a:
                print("Secret number is higher than "+(str(b))+" !")
                life = life - 1
                if life == 0:
                    print("Secret number was "+(str(a))+"!")
                    key = input("You are out of life points. Enter any key to play again: ")
                    if key:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print("You have " + (str(life)) + " life points left. Keep going!")
                    b = int(input("Try again!: "))
                    os.system('cls' if os.name == 'nt' else 'clear')

            elif b > a:
                print("Secret number is lower than " + (str(b)) + "!")
                life = life - 1
                if life == 0:
                    print("Secret number was " + (str(a)) + "!")
                    key = input("You are out of life points. Enter any key to play again: ")
                    if key:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print("You have " + (str(life)) + " life points left. Keep going!")
                    b = int(input("Try again!: "))
                    os.system('cls' if os.name == 'nt' else 'clear')
    elif diff == 2:
        life = 10
        print("You have " + (str(life)) + " life points. Guess the correct number before your life points reset.\n")
        a = random.randint(0, 150)
        b = int(input("Guess the number between 0,150!: "))
        while True:
            if b == a:
                print("Congratz! You found it!")
                key = input('Enter any key to play again: ')
                if key:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
            elif b < a:
                print("Secret number is higher than " + (str(b)) + " !")
                life = life - 1
                if life == 0:
                    print("Secret number was " + (str(a)) + "!")
                    key = input("You are out of life points. Enter any key to play again: ")
                    if key:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print("You have " + (str(life)) + " life points left. Keep going!")
                    b = int(input("Try again!: "))
                    os.system('cls' if os.name == 'nt' else 'clear')

            elif b > a:
                print("Secret number is lower than " + (str(b)) + "!")
                life = life - 1
                if life == 0:
                    print("Secret number was " + (str(a)) + "!")
                    key = input("You are out of life points. Enter any key to play again: ")
                    if key:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print("You have " + (str(life)) + " life points left. Keep going!")
                    b = int(input("Try again!: "))
                    os.system('cls' if os.name == 'nt' else 'clear')
    elif diff == 3:
        life = 10
        print("You have " + (str(life)) + " life points. Guess the correct number before your life points reset.\n")
        a = random.randint(0, 300)
        b = int(input("Guess the number between 0,300!: "))
        while True:
            if b == a:
                print("Congratz! You found it!")
                key = input('Enter any key to play again: ')
                if key:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
            elif b < a:
                print("Secret number is higher than " + (str(b)) + " !")
                life = life - 1
                if life == 0:
                    print("Secret number was " + (str(a)) + "!")
                    key = input("You are out of life points. Enter any key to play again: ")
                    if key:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print("You have " + (str(life)) + " life points left. Keep going!")
                    b = int(input("Try again!: "))
                    os.system('cls' if os.name == 'nt' else 'clear')

            elif b > a:
                print("Secret number is lower than " + (str(b)) + "!")
                life = life - 1
                if life == 0:
                    print("Secret number was " + (str(a)) + "!")
                    key = input("You are out of life points. Enter any key to play again: ")
                    if key:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print("You have " + (str(life)) + " life points left. Keep going!")
                    b = int(input("Try again!: "))
                    os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print("Bruh, just enter 1,2 or 3")
        time.sleep(2)
        exit(0)
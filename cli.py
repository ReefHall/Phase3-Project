import pyfiglet as pyg 
import os
from time import sleep
from lib.models.robot_designs import robot1, robot2, robot3, robot1_red, robot1_blue, robot1_green, robot2_red, robot2_blue, robot2_green, robot3_red, robot3_blue, robot3_green
from lib.models.robot_story_opening import intro, header_one
from lib.models.evil_robot_ending import evil_robot_ending, evil_end
from lib.models.good_robot_ending import good_robot_ending, good_end
from lib.models.good_animal_design import cat, dog, elephant
from lib.models.evil_animal_design import spider, bat, wolf 
from lib.models.evil_enhancement import hulk, smart, jokes
from lib.models.good_enhancement import intelligence, physical, social
from lib.models.robot import Robot

begin = input("Are you ready to begin? (y/n): ")
if begin.lower() == 'y':
    sleep(1)
    # Print the ASCII header
    print(header_one)
    sleep(1) # Wait for 1 second before printing the intro text
    # Print the intro text
    for line in intro.split("\n"):
        print(line)
        sleep(1.5) # Wait for 0.2 seconds before printing the next line
else:
    print("Okay, see you later!")

input("PRESS `ENTER` TO CONTINUE ")
os.system('clear')

print("                                                                           \033[1m\033[33mLike a mad scientist, you created three designs......\033[0m\n")
sleep(2.5)

print(f"1.\n{robot1}")
sleep(2.5)
print(f"2.\n{robot2}")
sleep(2.5)
print(f"3.\n{robot3}\n")
sleep(2.5)
a = Robot()
while(a.ascii == ""):
    robo_design = input("\nWhich do you choose?\n")
    sleep(1)

    if(robo_design == '1'):
        a.ascii = robot1

    elif(robo_design == '2'):
        
        a.ascii = robot2
    elif(robo_design == '3'):
        a.ascii = robot3
    else:
        print("You entered wrong number")

print ("\n\n\n\33[1m\033[33mGreat choice!!!!\033[0m\n\n\n")
sleep(2)
print("\33[1m\033[33mInitially, you made your robot’s exterior sleek and metallic looking. The metallic was excellent, but you thought you’d push yourself further.\033[0m\n\n\n\n")
sleep(2)
print("You decided to change the metallic color to:\n1.\33[96mBlue\33[00m\n2.\33[91mRed\33[00m\n3.\33[92mGreen\33[00m\n")
while(a.color == None):
    robo_color = input("Which color do you choose? ")
    if(robo_color == '1'):
        a.color = "Blue"
    elif(robo_color == '2'):
        a.color = "Red"
    elif(robo_color == '3'):
        a.color = "Green"
    else:
        print("Wrong color entered, try again")

if(a.ascii == robot1 and a.color == "Red"):
    a.ascii = robot1_red
elif(a.ascii == robot1 and a.color == "Blue"):
    a.ascii = robot1_blue
elif(a.ascii == robot1 and a.color == "Green"):
    a.ascii = robot1_green

if(a.ascii == robot2 and a.color == "Red"):
    a.ascii = robot2_red
elif(a.ascii == robot2 and a.color == "Blue"):
    a.ascii = robot2_blue
elif(a.ascii == robot2 and a.color == "Green"):
    a.ascii = robot2_green

if(a.ascii == robot3 and a.color == "Red"):
    a.ascii = robot3_red
elif(a.ascii == robot3 and a.color == "Blue"):
    a.ascii = robot3_blue
elif(a.ascii == robot3 and a.color == "Green"):
    a.ascii = robot3_green

print("\033[1m\033[33m\n\nLook how pretty your robot is now!\033[0m\n\n\n\n")
print(a.ascii)
sleep(3)

print("""\033[1m\033[33m\n\nAs you stand there, marveling at your creation, you realize you haven’t given your robot a name.\033[0m\n""")
sleep(2)

name = input("What is your robot's name?\n")
ascii_name = pyg.figlet_format(name)
print('\n\n\033[1;7;92m' + ascii_name +'\033[0m\n\n')
a.name = name

print("""say hello to your robot.\n""")

input_text = input("Type 'hello' so that your robot can introduce itself: ")
if input_text == "hello":
    print(f'\033[1m\33mHi, my name is, {name}, Nice to meet you!\033[0m')
    print(a.ascii)
else:
    print("Sorry, I didn't understand. Please try again.")


print("\033[33m\nLastly, before your robot comes to life, you have one more big decision.\033[0m\n")
sleep(2)
print("\033[33m\nThe robot is not inherently good or evil - its actions and agenda will be determined by the programming you give it.\033[0m\n")
sleep(2)
print("\033[33m\nWill you create a robot that will help humanity, or will you create one that will seek to dominate the world?\033[0m\n")
sleep(2)
choice = input("Enter 'GOOD' to create a robot that will help humanity, or 'EVIL' to create a robot that will seek to dominate the world:\n")

# continue with the 'good' storyline
if choice == "GOOD":
    a.behavior = "GOOD"
    ascii_good = pyg.figlet_format("GOOD", font = 'isometric3')
    print(f'2. \033[96m{ascii_good}\033[00m\n')
    sleep(1)
    print("\033[33m\nYou spend hours pouring your heart into your code, carefully crafting the robot's programming.\033[0m\n")
    sleep(2)
    print("\033[33m\nYou decide you want your creation to use its abilities for good, so you program it to prioritize helping humanity.\033[0m\n")
    sleep(2)
    print("\033[33m\nBefore your robot comes to life, you want to ensure that its programming is optimized for maximum effectiveness and has all the necessary features to accomplish its goals.\033[0m\n")
    sleep(2)

    robot_animal = input(f"""\n\nChoose the animal you would like,{a.name}, to morph into:\n1. Cat\n2. Dog\n3. Elephant\n\n""")
    while(a.animal == None):
        if robot_animal == "1":
            a.animal = "Cat"
            print(cat)
        elif robot_animal == "2":
            a.animal = "Dog"
            print(dog)
        elif robot_animal == "3":
            a.animal = "Elephant"
            print(elephant)
        else:
            print("Enter a valid animal")
    print(f"""\033[92m\nYou have chosen {a.animal} as your robot's morphing ability.\033[0m\n""")
    sleep(2)
    print(f"""\033[33m\nIn order to ensure  your robot is able to accomplish your plan to make the world a better place to exist in, you need to give it a skill that will help it accomplish its goals.\033[30m\n""")
    while(a.enhancement == None):
            robot_enhancement = input(f"""\033[92mWhich enhancement do you chose for {a.name}?\n
                1. Intelligence - your robot will be able to analyze complex data and identify patterns that could lead to breakthroughs in scientific research\n
                2. Physical: your robot can perform tasks that require significant strength or speed, such as disaster relief or construction work.\n
                3. Social: your robot will be able to interact with people in a way that makes them feel understood and supported and give them a good laugh in their day.\n
                \033[0m""")
            if robot_enhancement == "1":
                print(intelligence)
                a.enhancement = "Intelligent"
            elif robot_enhancement == "2":
                print(physical)
                a.enhancement = "Strong"
            elif robot_enhancement == "3":
                print(social)
                a.enhancement = "Funny"
            else:
                print("Enter a valid number")

    print(good_robot_ending)
    sleep(3)
    print(f"""\033[33mCongratulations! You have created {a}\n\n""")
    sleep(2)
    print(f"""\033[33mThanks for attempting to save the world!😇\n\n""")
    sleep(1)
    input("\033[96mPRESS ENTER TO END GAME")
    print(good_end)

elif choice == "EVIL":
    a.behavior = "EVIL"
    ascii_evil = pyg.figlet_format("Evil", font = 'isometric3')
    print(f'2. \033[91m{ascii_evil}\033[00m\n\n')
    # continue with the 'evil' storyline
    print(f"""\033[33mAs your robot comes to life, Its movements are jerky and unpredictable, and its voice has an eerie tone.

you realize that before you can implement your plan of taking over the world with your robot companion, you need to customize your robot a bit more. 

How cool would it be if {a.name} could morph into a scary animal?\n\n""")

    print(f"""\033[33mWhat animal would you choose for {a.name}?\n\n""")
    while(a.animal == None):
        robot_animal = input(f"Choose the animal you’d like,{a.name}, to morph into:\n1. Wolf\n2. Spider\n3. Bat\n ")
        if(robot_animal == '1'):
            a.animal = "Wolf"
            print(wolf)
        elif(robot_animal == '2'):
            a.animal = "Spider"
            print(spider)
        elif(robot_animal == '3'):
            a.animal = "Bat"
            print(bat)
        else:
            print("Enter a valid animal")
    print(f"You have chosen a {a.animal} to be the form of your robot's morphing ability.\n\n")
    print(f"""It occurred to you that the only way you can reach your goal of taking over the world with your robot is to optimize a feature to make it even more powerful and deadly.
    You have three options:\n\n""")
    while(a.enhancement == None):
        robot_enhancement = input(f"""Which Enhancement do you choose for {a.name}?\n
1.Enhanced Strength - this feature will give your robot immense physical power, allowing it to crush anything in its path.\n

2.Advanced Intelligence - this feature will make your robot incredibly smart and strategic, allowing it to out-think and outmaneuver any human opponent.\n

3.Tactical Weapon - this feature will give your robot a variety of deadly weapons, not limited to missiles, bombs, and laser guns, but also insanely corny jokes.\n""")
        if(robot_enhancement == '1'):
            print(hulk)
            a.enhancement ="Strong"
        elif(robot_enhancement == '2'):
            print(smart)
            a.enhancement = "Intelligent"
        elif(robot_enhancement == '3'):
            print(jokes)
            a.enhancement = "Funny"
        else:
            print("Enter a valid number")

    for line in evil_robot_ending.split("\n"):
        print(line)
        sleep(2)
    print(f"Congratulations! You have created {a}.\n\n")
    sleep(2)
    print("Thanks for trying to dominate the world!\n\n")
    sleep(1)
    input("\033[91mPRESS `ENTER` TO END GAME")
    print(evil_end)

else:
    print("Invalid choice. Please try again.")
    # ask the user to make a valid choice and restart the process

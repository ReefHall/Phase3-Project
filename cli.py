import pyfiglet as pyg   
import time
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
    time.sleep(.5)
    # Print the ASCII header
    print(header_one)
    time.sleep(1) # Wait for 1 second before printing the intro text
    # Print the intro text
    for line in intro.split("\n"):
        print(line)
        time.sleep(.5) # Wait for 0.2 seconds before printing the next line
else:
    print("Okay, see you later!")

input("PRESS `ENTER` TO CONTINUE ")
os.system('clear')

print("""\033[1m\033[33mLike a mad scientist, you created three designs......\033[0m\n""")
time.sleep(.5)

print(f"1.\n{robot1}")
sleep(2)
print(f"2.\n{robot2}")
sleep(2)
print(f"3.\n{robot3}\n")
sleep(2)
a = Robot()
while(a.ascii == ""):
    robo_design = input("\nWhich do you choose?\n")
    time.sleep(.5)

    if(robo_design == '1'):
        a.ascii = robot1

    elif(robo_design == '2'):
        
        a.ascii = robot2
    elif(robo_design == '3'):
        a.ascii = robot3
    else:
        print("You entered wrong number")

print("\33[1m\033[33mInitially, you made your robot’s exterior sleek and metallic looking. The metallic was excellent, but you thought you’d push yourself further.\033[0m\n")
print("You decided to change the metallic color to: \n1.\33[96mBlue\33[00m\n2.\33[91mRed\33[00m\n3.\33[92mGreen\33[00m\n")
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


print(f"Your {a.color}robot design:\n{a.ascii}")


print("""\033[1m\033[33mAs you stand there, marveling at your creation, you realize you haven’t given your robot a name.\033[0m\n""")

name = input("What is your robot's name?\n")
ascii_name = pyg.figlet_format(name)
print(ascii_name)
a.name = name

print(""" say hello to your robot.\n""")

input_text = input("Type 'hello' so that your robot can introduce itself: ")
if input_text == "hello":
    print(pyg.figlet_format(f"Hi, my name is {a.name}. Nice to meet you!"))
    print(f"{a.ascii}")
else:
    print("Sorry, I didn't understand. Please try again.")


print("\nLastly, before your robot comes to life, you have one more big decision.\n")
print("\nThe robot is not inherently good or evil - its actions and agenda will be determined by the programming you give it.\n")
print("\nWill you create a robot that will help humanity, or will you create one that will seek to dominate the world?\n")
choice = input("Enter 'good' to create a robot that will help humanity, or 'evil' to create a robot that will seek to dominate the world:\n")


if choice == "good":
    a.behavior = "GOOD"
    ascii_good = pyg.figlet_format("Good", font= 'isometric1')
    print(f'1. \033[98m{ascii_good}\033[00m')
    # continue with the 'good' storyline
    print("You spend hours pouring your heart into your code, carefully crafting the robot's programming.\n")
    print("You decide you want your creation to use its abilities for good, so you program it to prioritize helping humanity.\n")
    print("Before your robot comes to life, you want to ensure that its programming is optimized for maximum effectiveness and has all the necessary features to accomplish its goals.\n")
    robot_animal = input(f"Choose the animal you’d like,{a.name}, to shapeshift into:\n1. Cat\n2. Dog\n3. Elephant\n")
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
    print(f"You have chosen a,{a.animal},to be the form of your robot's shapeshifting ability.")
    sleep(2)
    print(f"In order to ensure  your robot is able to accomplish your plan to make the world a better place to exist in, you need to give it a skill that will help it accomplish its goals.\n")
    sleep(2)
    while(a.enhancement == None):
            robot_enhancement = input(f"""Which enhancement do you chose {a.name}?
    1. Intelligence - your robot will be able to analyze complex data and identify patterns that could lead to breakthroughs in scientific research
    2. Physical: your robot can perform tasks that require significant strength or speed, such as disaster relief or construction work.
    3. Social: your robot will be able to interact with people in a way that makes them feel understood and supported and give them a good laugh in their day.
    """)
            if robot_enhancement == "1":
                a.enhancement = "Intelligent"
                print(intelligence)
            elif robot_enhancement == "2":
                a.enhancement = "Strong"
                print(physical)
            elif robot_enhancement == "3":
                a.enhancement = "Funny"
                print(social)
            else:
                print("Enter a valid number")
    print(good_robot_ending)
    sleep(3)
    print(f"Congratulations! You have created {a}. Thanks for playing!")
    sleep(3)
    input("PRESS ENTER TO END GAME ")
    print(good_end)







elif choice == "evil":
    a.behavior = "EVIL"
    ascii_evil = pyg.figlet_format("Evil", font = 'isometric3')
    print(f'2. \033[91m{ascii_evil}\033[00m')
    # continue with the 'evil' storyline
    print("""As your robot comes to life, Its movements are jerky and unpredictable, and its voice has an eerie tone. you realize that before you can implement your plan of taking over the world with your robot companion, you need to customize your robot a bit more. How cool would it be if {a.name} could morph into a scary animal?""")
    print("""What animal would you choose to morph into?\n""")
    while(a.animal == None):
        robot_animal = input(f"Choose the animal you’d like,{a.name}, to shapeshift into:\n1. Wolf\n2. Spider\n3. Bat\n ")
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
    print(f"You have chosen a,{a.animal}, to be the form of your robot's shapeshifting ability.")
    print(f"""
    It occurred to you that the only way you can reach your goal of taking over the world with your robot is to optimize a feature to make it even more powerful and deadly.
    You have three options:\n """)
    print(f"Which Enhancement do you choose for {a.name}?\n")
    while(a.enhancement == None):
        robot_enhancement = input(f"""
1.Enhanced Strength - this feature will give your robot immense physical power, allowing it to crush anything in its path.
2.Advanced Intelligence - this feature will make your robot incredibly smart and strategic, allowing it to out-think and outmaneuver any human opponent.
3.Tactical Weapon - this feature will give your robot a variety of deadly weapons, not limited to missiles, bombs, and laser guns, but also insanely corny jokes.\n """)
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
    print(evil_robot_ending)
    print(f"Congratulations! You have created {a}. Thanks for playing!")
    input("PRESS ENTER TO END GAME ")
    print(evil_end)

    
                
                              
else:
    print("Invalid choice. Please try again.")
    # ask the user to make a valid choice and restart the process

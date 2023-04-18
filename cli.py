import time
import pyfiglet 
import os
from time import sleep
from lib.models.robot_designs import robot1, robot2, robot3, robot1_red, robot1_blue, robot1_green, robot2_red, robot2_blue, robot2_green, robot3_red, robot3_blue, robot3_green
from lib.models.robot_story_opening import intro, header_one

class Robot:
    def __init__(self, name="lou", color=None, animal=None, behavior=None):
        self.name = name
        self.color = color
        self.animal = animal
        self.behavior = behavior
        self.ascii = ''

    def __repr__(self):
        return f"{self.ascii}\nI am {self.name}, your robot. My color is {self.color}, I am {self.behavior} and I morph into a {self.animal}"
    
begin = input("Are you ready to begin? (y/n): ")
if begin.lower() == 'y':
    time.sleep(2)
    # Print the ASCII header
    print(header_one)
    time.sleep(2) # Wait for 1 second before printing the intro text
    # Print the intro text
    for line in intro.split("\n"):
        print(line)
        time.sleep(2) # Wait for 0.2 seconds before printing the next line
else:
    print("Okay, see you later!")
input("PRESS ANY KEY TO CONTINUE ")
os.system('clear')

print("""Like a mad scientist, you created three designs:""")

print(f"1.\n{robot1}")
sleep(2)
print(f"2.\n{robot2}")
sleep(2)
print(f"3.\n{robot3}\n")
sleep(2)
a = Robot()
while(a.ascii == ""):
    robo_design = input("Which do you choose? ")

    if(robo_design == '1'):
        a.ascii = robot1
    
    elif(robo_design == '2'):
        a.ascii = robot2
   
    elif(robo_design == '3'):
        a.ascii = robot3
    else:
        print("You entered wrong number")

print("Initially, you made your robot’s exterior sleek and metallic looking. The metallic was excellent, but you thought you’d push yourself further.")
print("You decided to change the metallic color to: \n1.\33[96mBlue\33[00m\n2.\33[91mRed\33[00m\n3.\33[92mGreen\33[00m\n")
while(a.color == None):
    robo_color = input("Which color do you choose? ")
    if(robo_color == '1'):
         a.color = "Blue"
    elif(robo_color == '2'):
         a.color == "Red"
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
    a.ascii = robot1_green

if(a.ascii == robot3 and a.color == "Red"):
    a.ascii = robot3_red
elif(a.ascii == robot3 and a.color == "Blue"):
    a.ascii = robot3_blue
elif(a.ascii == robot3 and a.color == "Green"):
    a.ascii = robot3_green

print(a)





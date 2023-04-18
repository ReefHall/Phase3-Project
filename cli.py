import pyfiglet as pyg   
import time
import os
from time import sleep
from lib.models.robot_designs import robot1, robot2, robot3, robot1_red, robot1_blue, robot1_green, robot2_red, robot2_blue, robot2_green, robot3_red, robot3_blue, robot3_green
from lib.models.robot_story_opening import intro, header_one

class Robot:
    def __init__(self, name="", color="", animal="", behavior=None, id=None, ascii=""):
        self.name = name
        self.color = color
        self.animal = animal
        self.behavior = behavior
        self.ascii = ''
        self.id = id

    def __repr__(self):
        return f"{self.ascii}\nI am {self.name}, your robot. My color is {self.color}, I am {self.behavior} and I morph into a {self.animal}"
    
begin = input("Are you ready to begin? (y/n): ")
if begin.lower() == 'y':
    time.sleep(1)
    # Print the ASCII header
    print(header_one)
    time.sleep(1) # Wait for 1 second before printing the intro text
    # Print the intro text
    for line in intro.split("\n"):
        print(line)
        time.sleep(1
                ) # Wait for 0.2 seconds before printing the next line
else:
    print("Okay, see you later!")
input("PRESS ANY KEY TO CONTINUE ")
os.system('clear')

print("""Like a mad scientist, you created three designs:\n""")

print(f"1.\n{robot1}")
sleep(2)
print(f"2.\n{robot2}")
sleep(2)
print(f"3.\n{robot3}\n")
sleep(2)

robo = input("Which do you choose? ")
a = Robot()

if(robo == '1'):
    a.ascii = robot1
    os.system('clear')

elif(robo == '2'):
    a.ascii = robot2
    os.system('clear')
    
elif(robo == '3'):
    a.ascii = robot3
    os.system('clear')
 
else:
    print("You entered wrong number")


#Robot Color  


#Robot Name 

print("""As you stand there, marveling at your creation, you realize you haven’t given your robot a name.""")



name = input("What is your robot's name? ")
ascii_name = pyg.figlet_format(name)
print(ascii_name)
a.name = name


print(f"Hi, my name is {a.name}.")
print(f"{a.ascii}")



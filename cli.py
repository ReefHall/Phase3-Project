import pyfiglet as pyg   
import time
import os
from time import sleep
from lib.models.robot_designs import robot1, robot2, robot3, robot1_red, robot1_blue, robot1_green, robot2_red, robot2_blue, robot2_green, robot3_red, robot3_blue, robot3_green
from lib.models.robot_story_opening import intro, header_one
from lib.models.evil_animal_design import bat, spider, wolf

class Robot:
    def __init__(self, name="", color= None, animal=None, behavior=None, id=None, ascii=""):
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
        time.sleep(1)
                 # Wait for 0.2 seconds before printing the next line
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
    a.ascii = robot1_green

if(a.ascii == robot3 and a.color == "Red"):
    a.ascii = robot3_red
elif(a.ascii == robot3 and a.color == "Blue"):
    a.ascii = robot3_blue
elif(a.ascii == robot3 and a.color == "Green"):
    a.ascii = robot3_green






#Robot Color  


#Robot Name 

print("""As you stand there, marveling at your creation, you realize you haven’t given your robot a name.""")



name = input("What is your robot's name? ")
ascii_name = pyg.figlet_format(name)
print(ascii_name)
a.name = name


print(f"Hi, my name is {a.name}.")
print(f"{a.ascii}")


print("""
                        Lastly, before your robot comes to life, you have one more big decision. The robot is not inherently good or evil - 
                        It's actions and agenda will be determined by the programming you give it. 
                        Will you create a robot that will help humanity, or will you create one that will seek to dominate the world?
                        The choice is yours….

""")
    
ascii_good = pyg.figlet_format("Good", font= 'isometric1')
ascii_evil = pyg.figlet_format("Evil", font = 'isometric3')

print(f'1. \033[98m{ascii_good}\033[00m\n2. \033[91m{ascii_evil}\033[00m\n ')

robot_behavior = input("1 or 2? ")

if(robot_behavior == "1"):
    pass
elif(robot_behavior == "2"):
    a.behavior = "Evil"
    print(f"""
                                                As your robot comes to life, Its movements are jerky and unpredictable, and its voice has an eerie tone. 
                                                you realize that before you can implement your plan of taking over the world with your robot companion, you need to customize your robot a bit more.
                                                How cool would it be if {a.name} could morph into a scary animal?""")
    sleep(1.5)
    print(""" 
                                                    What animal would you choose to morph into?\n

""")
      
    print("1.Wolf\n2.Spider\n3.Bat\n")
    while(a.animal == None):  
        robot_animal = input("Which beast... ")
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



    



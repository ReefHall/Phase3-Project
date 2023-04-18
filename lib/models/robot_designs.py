import time, os
from time import sleep
#1:
robot1 = """    
                                                                   
                                                                   X_____\\
                                                           .-^-.  ||_| |_||  .-^-.
                                                          /_\_/_\_|  |_|  |_/_\_/_\\
                                                          ||(_)| __\_____/__ |(_)||
                                                          \/| | |::|\```/|::| | |\/
                                                          /`---_|::|-+-+-|::|_---'\\
                                                        / /  \ |::|-|-|-|::| /  \ \\
                                                        /_/   /|`--'-+-+-`--'|\   \_\\
                                                        | \  / |===/_\ /_\===| \  / |
                                                        |  \/  /---/-/-\-\  o\  \/  |
                                                        | ||| | O / /   \ \   | ||| |
                                                        | ||| ||-------------|o|||| |
                                                        | ||| ||----\ | /----|o|||| |
                                                        | _|| ||-----|||-----|o|||_ |
                                                        \/|\/  |     |||     |o|\/|\/
                                                        \_o/   |----|||||----|-' \o_/
                                                               |##  |   |  ##|
                                                               |----|   |----|
                                                               ||__ |   | __||
                                                              [|'  `|] [|'  `|]
                                                              [|`--'|] [|`--'|]
                                                              /|__| |\ /| |__|\\
                                                              ||  | || || |  ||
                                                              ||__|_|| ||_|__||
                                                              ||    || ||    ||
                                                              \|----|/ \|----|/    
                                                              /______\ /______\\
                                                              |__||__| |__||__|
"""

#2: 
robot2 = """
                                                            _____                
                                                            |_|_|
                                                            |_|_|            _____
                                                            |_|_|    ____   |*_*_*|
                                                  _______   _\__\___/ __ \____|_|_   _______
                                                  / ____  |=|      \  <_+>  /      |=|  ____ \\
                                                  ~|    |\|=|======\\______//======|=|/|    |~
                                                  |_   |    \      |      |      /    |    |
                                                    \==-|     \     |  2D  |     /     |----|~~/
                                                    |   |      |    |      |    |      |____/~/
                                                    |   |       \____\____/____/      /    / /
                                                    |   |         {----------}       /____/ /
                                                    |___|        /~~~~~~~~~~~~\     |_/~|_|/
                                                    \_/         |/~~~~~||~~~~~\|     /__|\\
                                                    | |          |    ||||    |     (/|| \)
                                                    | |         /     |  |     \       \\
                                                    |_|         |     |  |     |
                                                                |_____|  |_____|
                                                                (_____)  (_____)
                                                                |     |  |     |
                                                                |     |  |     |
                                                                |/~~~\|  |/~~~\|
                                                                /|___|\  /|___|\\
                                                              <<_______><_______>>
    """
  



#3:
robot3 = """ 
                                                              .____.        .____.
                                                              |oooo|        |oooo|
                                                              |oooo| .----. |oooo|
                                                              |Oooo|/\_||_/\|oooO|
                                                              `----' / __ \ `----'
                                                              ,/ |#|/\/__\/\|#| \,
                                                            /  \|#|| |/\| ||#|/  \\
                                                            / \_/|_|| |/\| ||_|\_/ \\
                                                          |_\/     o\=----=/o    \/_|
                                                          <_>       |=\__/=|       <_>
                                                          <_>       |------|       <_>
                                                          | |    0__|======|__0    | |
                                                          |  |  | |O+------+O| |   |  |
                                                          |\/|  \_+/        \+_/   |\/|
                                                          \__/  _|||        |||_   \__/
                                                                | ||        || |
                                                               [==|]        [|==]
                                                               [===]        [===]
                                                                >_<          >_<
                                                               || ||        || ||
                                                               || ||        || ||
                                                               || ||        || ||    
                                                             __|\_/|__    __|\_/|__
                                                            /___n_n___\  /___n_n___\\
  
"""



robot1_red = f"\33[91m{robot1}\33[00m"
robot1_blue = f"\33[94m{robot1}\33[00m"
robot1_green = f"\33[92m{robot1}\33[00m"


robot2_red = f"\33[91m{robot2}\33[00m"
robot2_blue = f"\33[96m{robot2}\33[00m"
robot2_green = f"\33[92m{robot2}\33[00m"

robot3_red = f"\33[91m{robot3}\33[00m"
robot3_blue = f"\33[96m{robot3}\33[00m"
robot3_green = f"\33[92m{robot3}\33[00m"


print(robot1_red)
print(robot2_green)
print(robot3_blue)
print(robot1_blue)




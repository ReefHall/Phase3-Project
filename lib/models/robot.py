from lib.models.__init__ import CONN, CURSOR
class Robot:

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS robots (
        id INTEGER PRIMARY KEY,
        name TEXT,
        color TEXT,
        animal TEXT,
        behavior TEXT,
        enhancement Text,
        ascii TEXT
        )"""
        CURSOR.execute(sql)

    def __init__(self, name ="", color = None, animal = None, behavior = None, enhancement = None, ascii ="", id = None):
        self.name = name
        self.color = color
        self.animal = animal
        self.behavior = behavior
        self.enhancement = enhancement
        self.ascii = ascii
        self.id = id
    

    def __repr__(self):
        return f"{self.ascii}\nI am {self.name}, your robot. My color is {self.color} and I am {self.behavior}. I morph into a {self.animal} and I am {self.enhancement}."
    
    def create(self):
        self.ascii = "Robot"
        sql= """INSERT INTO robots (name, color, animal, behavior, enhancement, ascii)
        VALUES (?, ?, ?, ?, ?, ?)"""
        CURSOR.execute(sql, [self.name, self.color, self.animal, self.behavior, self.enhancement, self.ascii])
        CONN.commit()
        self.id = CURSOR.execute("SELECT id FROM robots ORDER BY id DESC").fetchone()[0]

    def update(self):
        sql = """UPDATE robots SET name = ?, color = ?, animal = ?, behavior =? enhancement = ? ascii = ? WHERE id =?"""
        CURSOR.execute(sql, [self.name, self.color, self.animal, self.behavior, self.enhancement, self.ascii, self.id])

    def save(self):
        if(self.id):
            self.update()
        else:
            self.create()

    @classmethod
    def delete(cls, id):
        sql = "DELETE FROM robots WHERE id = ?"
        CURSOR.execute(sql,[id])
        CONN.commit()

    @classmethod
    def query_all(cls):
        sql= "SELECT * FROM robots"
        all_robots = CURSOR.execute(sql).fetchall()
        robots_list = []
        for data in all_robots:
            robot = Robot(data[1], data[2], data[3], data[4], data[5], data[6])
            robot.id = data[0]
            robots_list.append(robot)
        return robots_list
    
    @classmethod
    def query_bad(cls):
        sql = "SELECT * FROM robots WHERE behavior = ?"
        evil_robots = CURSOR.execute(sql,['EVIL']).fetchall()
        robot_list = []
        for data in evil_robots:
            robot = Robot(data[1], data[2], data[3], data[4], data[5], data[6])
            robot_list.append(robot)
        return robot_list

    @classmethod
    def query_good(cls):
        sql = "SELECT * FROM robots WHERE behavior = ?"
        good_robots = CURSOR.execute(sql,['GOOD']).fetchall()
        robot_list = []
        for data in good_robots:
            robot = Robot(data[1], data[2], data[3], data[4], data[5], data[6])
            robot_list.append(robot)
        return robot_list
robot_designs = {}

with open('robot_designs.txt') as f:
    lines = f.readlines()

    for i in range(0, len(lines), 6):
        robot_id = int(lines[i].strip().split(':')[0])
        robot_design = "".join(lines[i+1:i+6])
        robot_designs[robot_id] = robot_design

print(robot_designs[1])


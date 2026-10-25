import os
import random
guy = [
    r"  _   ",
    r" |_|  ",
    r" /|\  ",
    r"  |   ",
    r" / \  "
]
lane_width = 9
def clear_terminal():
    # \033c resets the terminal, \033[H\033[J moves cursor home and clears below
    print("\033[H\033[J", end="")

# This renders out the guy from his parts
def renderGuy(index):
    clear_terminal()
    for part in guy:
        lane = [" " * 9, " " * 9, " " * 9,]
        part_centered = part.center(lane_width)
        lane[index] = part_centered
        obstacle = 1
        obstacle_lane = [f"{obstacle} " * 9, " " * 9, " " * 9,]
        print("|"+"|".join(lane))




# this uses the render guy and takes in input
def movement(): 
    movement = input("Character Movement Left (A) or Right (D) or Forward (W): ")
    if movement == "A":
        print("Left")
        index = 0
        renderGuy(index)
    elif movement == "D":
        index = 2
        print("Right")
        renderGuy(index)
    elif movement == "S":
        print("Forward")
        index = 1
        renderGuy(index)
    else:
        print("Nothing")

gameIsRunning = True

def pickDoor():
    rand = random.randint(-1,3)


while gameIsRunning:
    movement()

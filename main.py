guy = [
    r"  _  ",
    r" |_| ",
    r" /|\ ",
    r"  |  ",
    r" / \ "
]
lane_width = 9
lane = [" " * 9,"" * 9," " * 9,]
# This reneders out the guy from his parts
def renderGuy(index):
    for part in guy:
        part_centered = part.center(lane_width)
        lane[index] = part_centered
        print("|".join(lane))

def movement(): 
    movement = input("Character Movement Left (A) or Right (D) or Forward (W): ")
    if movement == "A":
        print("Left")
        index = 0
        renderGuy(index)
    elif movement == "D":
        print("Right")
        index = 2
        renderGuy(index)
    elif movement == "W":
        print("Forward")
        index = 1
        renderGuy(index)
    else:
        print("Nothing")

movement()

#Maze Solver Using Backtrack and Las Vegas
#Task 1 DSA2
#Andreea Dobre 25/10/2026
#success rate loop added - 02/11/2026

import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


#store the maze in a variable and open the maze image
IMAGE_FILE = "maze(1).png"
maze_image = Image.open(IMAGE_FILE)
maze_image = plt.imread("maze(1).png")


#display the image for the user
plt.figure(figsize=(5, 5))
plt.imshow(maze_image)
plt.title("Original Maze: Entrance at Top, Exit at Bottom")
plt.axis("off")
plt.tight_layout()
plt.show()


#definition of the maze
ROWS = 21
COLS = 21
CELL_SIZE = 10


#convert the image into a 21x21 grid
#'#' represents a wall
#'.' represents the path
#creating a list to store the 21 rows for our maze
image_array = np.array(maze_image)
maze = []
#loop all rows
for row in range(ROWS):
    grid_row = []
    #loop all cols
    for col in range(COLS):
        #the maze is 21x21 but our image is 210x20 pixels
        #so we need to check wall/path by checking in the middle of each square
        x = col * 10 + 5
        y = row * 10 + 5
        pixel = image_array[y, x]
        #if the pixel is 0 = wall (#), 1 = path(.)
        if pixel[0] == 0:
            grid_row.append("#")  #black wall
        else:
            grid_row.append(".")  #path
    maze.append(grid_row)


#start and end of the maze
start = (0,9)
end = (20,11)
maze[start[0]][start[1]] = "S"
maze[end[0]][end[1]] = "E"
print("\nMAZE GRID")
print("S = Start, E = Exit, # = Wall, . = Path\n")
#going through all 21 rows and printing the symbols for wall and path with a space between them
for row in maze:
    print(" ".join(row))
    

#walkable grid
#we will create another grid "walkable" where true = path and false = wall
walkable = []
#looping all rows
for row in maze:
    walkable_row = []
    #looping in all cells of the row
    for cell in row:
        if cell == "#":
            walkable_row.append(False)
        else:
            walkable_row.append(True)
    walkable.append(walkable_row)
    

#movement directions in order: up, right, down, left
#row, col coordinates
Up = (-1, 0)
Right = (0, 1)
Down = (1, 0)
Left = (0, -1)
directions = [Up, Right, Down, Left]


#def function: return all walkable orthogonal neighbours
def get_neighbours(position):
    #position is made of row, col coordinates
    row, col = position
    #creating the list where we will store all squares allowed to move into
    neighbours = []
    #check all 4 directions and calculating the new positions
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        #check if the position is valid
        if new_row >= 0 and new_row < ROWS:
            if new_col >= 0 and new_col < COLS:
                if walkable[new_row][new_col] == True:
                    #add the positions to the list
                    neighbours.append((new_row, new_col))
    #return the list
    return neighbours


#input from user - approach: backtrack / las vegas after maze display
choice = input("Choose a maze-solving approach: Backtracking / Las Vegas: ").strip().lower()
print("(Las Vegas = random walk, maximum 200 steps)")
#double check user is selecting one of the methods
if choice in ("backtracking", "las vegas"):
    print()
else:
    print("\nInvalid choice. Please choose Backtracking or Las Vegas.")


#BACKTRACKING
if choice == "backtracking":
    print("You chose Backtracking.")

#funciton definition
#DFS search with backtracking
#visit each square once
#if route is dead-end, return to previous square and try the next available direction
def alg_backtracking():
    #create list to remember which squares been visited 
    visited = []
    #create list to record order of squares visited
    visit_order = []
    
    #function definition inside main backtracking function
    #searching from the current square
    def search(position):
        #appending the list of visited squares
        visited.append(position)
        visit_order.append(position)
        #if the current position is the end of the maze, exit been found
        if position == end:
            return True
        # explore directions in the defined order
        # Up, Right, Down, Left
        neighbours = get_neighbours(position)
        for next_position in neighbours:
            #check if neighbour squares been visited, and if yes, skip it
            if next_position not in visited:
                #function calling itself to check the next neighbour
                if search(next_position):
                    return True
        #if none of the neighbours lead to exit, it will go back to another route
        return False
    #search starts at maze entrance
    success = search(start)
    #return if exit was found or if no route was found and list the squares visited in order
    return success, visit_order


#LAS VEGAS
#max 200 moves chose randomly in 4 directions (up, right, down, left)
#can eighter reach the exit (success) or complete the 200 moves without reaching the exit (fail)
def alg_lasvegas(max_steps=200):
    #starts at start poit of maze: (0, 9)
    current = start
    #create list that record the order of visited squares
    visit_order = [start]
    #create counter for steps/moves alg made, starting at 0
    steps = 0
    #loop that run while we are not at the end and we still have moves to make
    while current != end and steps < max_steps:
        neighbours = get_neighbours(current)
        #checks if any available neighbours or dead end
        if len(neighbours) == 0:
            #choising a random square already visited to continue until reaches 200 moves
            current = random.choice(visit_order)
        else:
            #if we have available neighbours, move randomly on one position
            current = random.choice(neighbours)
        steps = steps + 1
        visit_order.append(current)
    if current == end:
        success = True
    else:
        success = False
    return success, visit_order, steps
    

#running the selected aglorithm
if choice == "backtracking":
    success, visit_order = alg_backtracking()
    #counting the steps minus the first one that was start square
    steps = len(visit_order) - 1
    method = "Backtracking"

else:
    success, visit_order, steps = alg_lasvegas()
    method = "Las Vegas"

print("Algorithm: ", method)
print("Start: ", start)
print("Exit: ", end)
print("Moves taken: ", steps)
distinct_squares = len(set(visit_order))
print("Distinct squares visited: ", distinct_squares)

if success == True:
    print("Result: SUCCESS! The exit was found.")
else:
    print("Result: UNSUCCESSFUL. The exit was not found.")


#visualising the result
#showing the original maze and highlight every visited position.
plt.figure(figsize=(5, 5))
plt.imshow(maze_image)


#mark every visited square
#pixel coordinates are the centres of the maze cells
x_coords = []
y_coords = []
for position in visit_order:
    row = position[0]
    col = position[1]
    x = col * 10 + 5
    y = row * 10 + 5
    x_coords.append(x)
    y_coords.append(y)

plt.scatter(
    x_coords,
    y_coords,
    color="blue",
    s=20,
    label="Visited squares"
)


#mark the start and exit distinctly
start_x = start[1] * 10 + 5
start_y = start[0] * 10 + 5
plt.scatter(
    start_x,
    start_y,
    color="green",
    edgecolors="black",
    s=50,
    marker="X",
    label="Start"
)

end_x = end[1] * 10 + 5
end_y = end[0] * 10 + 5
plt.scatter(
    end_x,
    end_y,
    color="red",
    edgecolors="black",
    s=50,
    marker="X",
    label="Exit"
)


#title
if success == True:
    result_text = "Success"
else:
    result_text = "Unsuccessful"

plt.title(method + " Maze Solver\nResult: " + result_text)


#legend
plt.legend(loc="lower left")
plt.axis("off")
plt.tight_layout()
plt.show()


#test success rate
total_runs = 10000
backtracking_successes = 0
lasvegas_successes = 0

for run in range(total_runs):
    success, visit_order = alg_backtracking()
    if success:
        backtracking_successes += 1

for run in range(total_runs):
    success, visit_order, steps = alg_lasvegas()
    if success:
        lasvegas_successes += 1

backtracking_rate = (backtracking_successes / total_runs) * 100
lasvegas_rate = (lasvegas_successes / total_runs) * 100

print("\nResults after 10 000 runs")
print("Backtracking successes:", backtracking_successes)
print("Backtracking success rate:", backtracking_rate, "%")

print("Las Vegas successes:", lasvegas_successes)
print("Las Vegas success rate:", lasvegas_rate, "%")

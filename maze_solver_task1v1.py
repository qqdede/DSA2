#Maze Solver Using Backtrack and Las Vegas
#Task 1 DSA2
#Andreea Dobre 25/10/2026

import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


#store the maze in a variable and open the maze image
IMAGE_FILE = "maze(1).png"
maze_image = Image.open(IMAGE_FILE)
maze_image = plt.imread("maze(1).png")


#definition of the maze
ROWS = 21
COLS = 21
CELL_SIZE = 10


#display the image for the user
plt.figure(figsize=(5, 5))
plt.imshow(maze_image)
plt.title("Original Maze: Entrance at Top, Exit at Bottom")
plt.axis("off")
plt.tight_layout()
plt.show()    


#convert the image into a 21x21 grid
#'0' represents a wall
#'1' represents the path
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
        pixel = image_array[x, y]
        #if the pixel is 0 = wall (#), 1 = path(.)
        if pixel[0] == 0:
            grid_row.append("#")  #black wall
        else:
            grid_row.append(".")  #path
    maze.append(grid_row)


#start and end
start = (0,9)
end = (20,11)
maze[start[0]][start[1]] = "S"
maze[end[0]][end[1]] = "E"
print("\nMAZE GRID")
print("S = Start, E = Exit, # = Wall, . = Path\n")
#going trough all 21 rows and printing the symbols for wall and path with a space between them
for row in maze:
    print(" ".join(row))
    

#input from user - approach: backtrack / las vegas after maze display
choice = input("Choose an approach: backtracking / las vegas: ")

if choice == "backtracking":
    print("You chose Backtracking.")
    visited = []
    def solve_dfs(x, y):

        if (x, y) == end:
            visited.append((x, y))
            return True

        if (
            x < 0 or x >= 21 or
            y < 0 or y >= 21
            ):
            return False

        if maze[x][y] == 1:
            return False

        if (x, y) in visited:
            return False

            visited.append((x, y))

            directions = [
                (-1, 0),  # up
                (0, 1),   # right
                (1, 0),   # down
                (0, -1)   # left
            ]

        for dx, dy in directions:

            if solve_dfs(x + dx, y + dy):
                return True

        return False

elif choice == "las vegas":
    print("You chose Las Vegas.")
    import random

visited = []


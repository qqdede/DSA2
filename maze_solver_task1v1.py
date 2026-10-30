#Maze Solver Using Backtrack and Las Vegas
#Task 1 DSA2
#Andreea Dobre 25/10/2026

import matplotlib.pyplot as plt

#load the image
maze = plt.imread("maze(1).png")

#display the image before prog run
plt.imshow(maze)
plt.title("Maze")
#hide axes
plt.axis("off")
plt.show()

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

def las_vegas():

    position = start

    visited.append(position)

    for step in range(200):

        if position == end:
            return True

        x, y = position

        neighbours = []

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < 21 and
                0 <= ny < 21 and
                maze[nx][ny] == 0
            ):
                neighbours.append((nx, ny))

        if len(neighbours) == 0:
            return False

        position = random.choice(neighbours)

        visited.append(position)

    return False
    success = las_vegas()

    if success:
    print("Exit found!")
    else:
    print("Failed after 200 steps.")
    
else:
    print("Invalid choice. Please enter 'backtracking' or 'las vegas'.")

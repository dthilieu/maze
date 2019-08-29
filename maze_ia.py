#!/usr/bin/env python3
from sys import stdin, stdout, stderr


# Communicate with program
def Communicate():
    for i in range(2):
        if "HELLO" in stdin.readline():
            stdout.write("I AM A\n\n")
        elif "YOU ARE" in stdin.readline():
            stdout.write("OK\n\n")
    stdin.readline()


# Parse and store maze
def Make_maze():
    maze = []
    stdin.readline()
    while True:
        line = stdin.readline()
        if line == "\n":
            break
        elif "#" in line:
            maze.append(line)
        # stderr.write(line)
    return maze


# Find Player's position
def Find_Player(maze):
    player = [0, 0]
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == "A":
                player[0] = x
                player[1] = y
                break
    return player


# Find coin position and its before steps from player to coin
def Find_coin(maze, player, directions):
    coin = ()
    explored = {}
    queue = [player]
    neighbor = ()
    valid_cell = ["o", "!", " "]
    resources = ["o", "!"]
    while queue:
        node = queue.pop(0)
        for direction in directions.values():
            if ((node[0] + direction[0] in range(len(maze))) and
               (node[1] + direction[1] in range(len(maze[0])))):
                neighbor = tuple([node[0] + direction[0],
                                 node[1] + direction[1]])
                if (maze[neighbor[0]][neighbor[1]] in valid_cell and
                   neighbor not in explored):
                    explored[neighbor] = node
                    queue.append(list(neighbor))
                if maze[neighbor[0]][neighbor[1]] in resources:
                    coin = neighbor
                    break
        if coin == neighbor:
            if tuple(player) in explored:
                del explored[tuple(player)]
            break
    return (coin, explored)


# Find shortest path to coin
def Find_shortest_path(player, coin, explored):
    path = [coin]
    if coin in explored:
        before = tuple(explored[coin])
        while True:
            path.append(before)
            if before in explored:
                before = tuple(explored[before])
            else:
                break
    return path


# Control steps on maze
def Control_steps(player, path, directions, maze):
    while True:
        player = Find_Player(maze)
        coin_and_explored = Find_coin(maze, player, directions)
        coin = coin_and_explored[0]
        explored = coin_and_explored[1]
        path = Find_shortest_path(player, coin, explored)
        # Move to coin
        player = path.pop()
        while path:
            next_step = path.pop()
            check_dir = (player[0] - next_step[0], player[1] - next_step[1])
            if check_dir == directions["left"]:
                stdout.write("MOVE LEFT\n\n")
                player = next_step
            elif check_dir == directions["right"]:
                stdout.write("MOVE RIGHT\n\n")
                player = next_step
            elif check_dir == directions["up"]:
                stdout.write("MOVE UP\n\n")
                player = next_step
            elif check_dir == directions["down"]:
                stdout.write("MOVE DOWN\n\n")
                player = next_step
            maze = Make_maze()


# Main function
def main():
    directions = {"left": (0, 1), "right": (0, -1), "up": (1, 0),
                  "down": (-1, 0)}
    Communicate()
    maze = Make_maze()
    player = Find_Player(maze)
    coin_and_explored = Find_coin(maze, player, directions)
    coin = coin_and_explored[0]
    explored = coin_and_explored[1]
    path = Find_shortest_path(player, coin, explored)
    Control_steps(player, path, directions, maze)


if __name__ == "__main__":
    main()

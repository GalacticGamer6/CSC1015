# A very tired and struggling NEeraav
#it keeps fkn merging when just spawning
#21/04/2024
#The push utils for 2048

def push_up(grid):

    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            if grid[i][j] != 0:
                for b in range(i, 0, -1):
                    if grid[b - 1][j] == 0:
                        grid[b - 1][j] = grid[b][j]
                        grid[b][j] = 0
                    elif grid[b - 1][j] == grid[b][j]:
                        grid[b - 1][j] *=2
                        grid[b][j] = 0
                        break

def push_down(grid):
    # Loop through each column
    for j in range(len(grid)):
        for i in range(len(grid)-2,-1,-1):
            if grid[i][j] != 0:
                for b in range(i,len(grid)-1):
                    if grid[b+1][j] == 0:
                        grid[b+1][j] = grid[b][j]
                        grid[b][j] = 0
                    elif grid[b+1][j] == grid[b][j]:
                        grid[b+1][j] *=2
                        grid[b][j] = 0
                        break

def push_left(grid):
    for i in range(len(grid)):
        for j in range(1, len(grid[i])):
            if grid[i][j] != 0:
                for b in range(j, 0, -1):
                    if grid[i][b - 1] == 0:
                        grid[i][b - 1] = grid[i][b]
                        grid[i][b] = 0
                    elif grid[i][b - 1] == grid[i][b]:
                        grid[i][b - 1] *=2
                        grid[i][b] = 0
                        break

def push_right(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 2, -1, -1):
            if grid[i][j] != 0:
                for b in range(j, len(grid[i]) - 1):
                    if grid[i][b + 1] == 0:
                        grid[i][b + 1] = grid[i][b]
                        grid[i][b] = 0
                    elif grid[i][b + 1] == grid[i][b]:
                        grid[i][b + 1] *=2
                        grid[i][b] = 0
                        break
def create_grid(grid):
    # Initialize an empty grid
    for i in range(4):
        # Append a row of four zeros to the grid
        grid.append([0] * 4)
    return grid

def check_won(grid):
    #same as the 0 checking but for 32 instead:
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] >= 32:
                return True
    return False

def print_grid(grid):
    #printing out the border pattern
    print("+--------------------+")

    for i in range(len(grid)):
        #printing out the first bar for each row of the grid, makings ure that thw row will print on the same line
        print("|",end = "")
        #printing the row and leaving 4 spaces
        for j in range(len(grid[i])):
            #printing a blank instead of 0:
            if grid[i][j] == 0:
                print(" " * 5,end="")
            else:
                print(str(grid[i][j]) + " "*(5 -(len(str(grid[i][j])))),end = "")
        #printing a new line to start the next row and closing the last line of each row
        print("|")
    print("+--------------------+")

def check_lost(grid):

    # Setting some booleans
    no_zero = True
    no_equals = True

    #just loop through and check for 0 in each set(row)
    for i in grid:
        if 0 in i:
            no_zero = False


    #checking for adjacent
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            #Now we start the edge cases ffs

            #edge cases for corners
            if(row == 0 and col == 0):
                if grid[row][col] == grid[row][col + 1] or grid[row][col] == grid[row + 1][col]:
                    no_equals = False
            elif(row == len(grid) - 1 and col == 0):
                if grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row][col + 1]:
                    no_equals = False
            elif(row == 0 and col == len(grid[row]) - 1):
                if grid[row][col] == grid[row][col - 1] or grid[row][col] == grid[row + 1 ][col]:
                    no_equals = False
            elif(row == len(grid)-1 and col == len(grid[row])-1):
                if grid[row][col] == grid[row][col - 1] or grid[row][col] == grid[row - 1][col]:
                    no_equals = False

            #edge cases for row's 1,4 and columns 1 and 4
            elif(row == 0):
                if grid[row][col] == grid[row][col + 1] or grid[row][col] == grid[row][col - 1] or grid[row][col] == grid[row + 1][col]:
                    no_equals = False
            elif(row == len(grid) - 1):
                if grid[row][col] == grid[row][col - 1] or grid[row][col] == grid[row ][col + 1] or grid[row][col] == grid[row - 1][col]:
                    no_equals = False

            elif(col == 0):
                if grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row][col + 1]:
                    no_equals = False
            elif(col == len(grid[row]) - 1):
                if grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row][col - 1]:
                    no_equals == False

            #now just that inner 2x2 check
            else:
                if grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row][col + 1] or grid[row][col] == grid[row][col - 1]:
                    no_equals = False

    #now we evaluate the booleans
    if(no_zero == True and no_equals == True):
        return True
    else:
        return False

def copy_grid(grid):
    copied = []
    copied = create_grid(copied)

    #just looping through and copoying cell by cell
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            copied[row][col] = grid[row][col]
    return copied

def grid_equal(grid1,grid2):
    # just loop through both in parralell and see if they equal
    for row in range(len(grid1)):
        for col in range(len(grid1[row])):
            if grid1[row][col] != grid2[row][col]:
                return False
    return True
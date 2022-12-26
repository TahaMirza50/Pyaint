from .arrow_settings import *
from .settings import *

class Arrows:
    
    def __init__(self):
        pass
                
    def make_arrow(self, row, col, drawing_color, grid, MULTI_HEAD):
        global LAST_POS, BRUSH_SIZE
        last_pos = LAST_POS
        BRUSH_SIZE = 1
        grid[row][col] = drawing_color
        if(LAST_POS == (-1, -1)):
            grid[row][col] = ORANGE
            LAST_POS = (row, col)
            return
        
        grid[last_pos[0]][last_pos[1]] = drawing_color
        second_pos = (row, col)
        row_diff = abs(last_pos[0] - second_pos[0])
        col_diff = abs(last_pos[1] - second_pos[1])
        
        arrow_state = ""
        
        if(col_diff == 0 and row_diff == 0):
            LAST_POS = (-1, -1)
            return
        
        if(col_diff == 0): # if straight arrow up/down
            if(last_pos[0] > second_pos[0]): #up arrow
                arrow_state = "UP"
                for i in range(row_diff):
                    grid[second_pos[0] + i][col] = drawing_color
                for i in range(1,3): #draws arrowhead
                    grid[second_pos[0] + i][second_pos[1] + i] = drawing_color
                    grid[second_pos[0] + i][second_pos[1] - i] = drawing_color
            else:
                arrow_state = "DOWN"
                for i in range(row_diff): #down arrow
                    grid[last_pos[0] + i][col] = drawing_color
                for i in range(1,3): #draws arrowhead
                    grid[second_pos[0] - i][second_pos[1] + i] = drawing_color
                    grid[second_pos[0] - i][second_pos[1] - i] = drawing_color
                    
        elif(row_diff == 0):# if straight arrow left/right
            if(last_pos[1] > second_pos[1]): #left arrow
                arrow_state = "LEFT"
                for i in range(col_diff):
                    grid[row][second_pos[1]+i] = drawing_color
                for i in range(1,3): #draws arrowhead
                    grid[second_pos[0] - i][second_pos[1] + i] = drawing_color
                    grid[second_pos[0] + i][second_pos[1] + i] = drawing_color
            else:
                arrow_state = "RIGHT"
                for i in range(col_diff):
                    grid[row][last_pos[1]+i] = drawing_color
                for i in range(1,3): #draws arrowhead
                    grid[second_pos[0] - i][second_pos[1] - i] = drawing_color
                    grid[second_pos[0] + i][second_pos[1] - i] = drawing_color
        
        elif row_diff == col_diff:
            if((last_pos[0] > second_pos[0]) and (last_pos[1] < second_pos[1])): # upper right diagonal
                arrow_state = "U_RIGHT"
                r, c = last_pos
                while((r, c) != second_pos):
                    grid[r][c] = drawing_color
                    r -= 1; c += 1
                del r, c
                for i in range(1,3):
                    grid[row+i][col] = drawing_color
                    grid[row][col-i] = drawing_color
                    
            elif ((last_pos[0] > second_pos[0]) and (last_pos[1] > second_pos[1])): # upper left diagonal
                arrow_state = "U_LEFT"
                r, c = last_pos
                while((r, c) != second_pos):
                    grid[r][c] = drawing_color
                    r -= 1; c -= 1
                del r, c
                for i in range(1,3):
                    grid[row][col+i] = drawing_color
                    grid[row+i][col] = drawing_color
                    
            elif ((last_pos[0] < second_pos[0]) and (last_pos[1] > second_pos[1])): # lower left diagonal
                arrow_state = "L_LEFT"
                r, c = last_pos
                while((r, c) != second_pos):
                    grid[r][c] = drawing_color
                    r += 1; c -= 1
                del r, c
                for i in range(1,3):
                    grid[row-i][col] = drawing_color
                    grid[row][col+i] = drawing_color
            
            elif ((last_pos[0] < second_pos[0]) and (last_pos[1] < second_pos[1])): # lower right diagonal
                arrow_state = "L_RIGHT"
                r, c = last_pos
                while((r, c) != second_pos):
                    grid[r][c] = drawing_color
                    r += 1; c += 1
                del r, c
                for i in range(1,3):
                    grid[row-i][col] = drawing_color
                    grid[row][col-i] = drawing_color
            
        if MULTI_HEAD:
            self.make_second_arrow_head(grid, arrow_state, drawing_color)
            pass
        
        LAST_POS = (-1,-1)

    def make_second_arrow_head(self, grid, arrow_state, drawing_color):
        row, col = LAST_POS
        if arrow_state == "UP":
            for i in range(1,3): #draws arrowhead
                    grid[row - i][col + i] = drawing_color
                    grid[row - i][col - i] = drawing_color
        elif arrow_state == "DOWN":
            for i in range(1,3): 
                    grid[row + i][col + i] = drawing_color
                    grid[row + i][col - i] = drawing_color
        elif arrow_state == "LEFT":
            for i in range(1,3): 
                    grid[row - i][col - i] = drawing_color
                    grid[row + i][col - i] = drawing_color
        elif arrow_state == "RIGHT":
            for i in range(1,3): 
                    grid[row - i][col + i] = drawing_color
                    grid[row + i][col + i] = drawing_color
        elif arrow_state == "U_RIGHT":
            for i in range(1,3): 
                    grid[row - i][col] = drawing_color
                    grid[row][col + i] = drawing_color
        elif arrow_state == "U_LEFT":
            for i in range(1,3): 
                    grid[row - i][col] = drawing_color
                    grid[row][col - i] = drawing_color
        elif arrow_state == "L_LEFT":
            for i in range(1,3): 
                    grid[row + i][col] = drawing_color
                    grid[row][col - i] = drawing_color
        elif arrow_state == "L_RIGHT":
            for i in range(1,3): 
                    grid[row + i][col] = drawing_color
                    grid[row][col + i] = drawing_color

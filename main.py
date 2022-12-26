import pygame as pygame
import math

from utils import *

WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Pyaint")
STATE = "COLOR"
Change = False

def init_grid(rows, columns, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(columns):    #use _ when variable is not required
            grid[i].append(color)
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, SILVER, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(win, SILVER, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

def draw_mouse_position_text(win):
    pos = pygame.mouse.get_pos()
    pos_font = get_font(MOUSE_POSITION_TEXT_SIZE)
    try:
        row, col = get_row_col_from_pos(pos)
        text_surface = pos_font.render(str(row) + ", " + str(col), 1, BLACK)
        win.blit(text_surface, (5 , HEIGHT - TOOLBAR_HEIGHT))
    except IndexError:
        for button in buttons:
            if not button.hover(pos):
                continue
            if button.text == "Clear":
                text_surface = pos_font.render("Clear Everything", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.text == "Erase":
                text_surface = pos_font.render("Erase", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "FillBucket":
                text_surface = pos_font.render("Fill Bucket", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Brush":
                text_surface = pos_font.render("Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Change":
                text_surface = pos_font.render("Swap Toolbar", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Arrow":
                text_surface = pos_font.render("Arrow", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Line":
                text_surface = pos_font.render("Line", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Dotted-Line":
                text_surface = pos_font.render("Dotted Line", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Full-Multiline":
                text_surface = pos_font.render("Full-Multiline", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Pen":
                text_surface = pos_font.render("Pen", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Pencil":
                text_surface = pos_font.render("Pencil", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break

            if button.name == "Multi-Head":
                text_surface = pos_font.render("Draw Multi-Head Arrow", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            
            if button.name == "Anti-Aliasing":
                text_surface = pos_font.render("Anti-Aliasing", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            
            if button.name == "CB1":
                text_surface = pos_font.render("Gradient Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            
            if button.name == "CB2":
                text_surface = pos_font.render("Snowflake", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            
            if button.name =="Add-Brush":
                text_surface = pos_font.render("Add Custom Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break

            r,g,b = button.color
            text_surface = pos_font.render("( " + str(r) + ", " + str(g) + ", " + str(b) + " )", 1, BLACK)
            
            win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
        
        for button in brush_widths:
            if not button.hover(pos):
                continue
            if button.width == size_small:
                text_surface = pos_font.render("Small-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_medium:
                text_surface = pos_font.render("Medium-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_large:
                text_surface = pos_font.render("Large-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10 , HEIGHT - TOOLBAR_HEIGHT))
                break    

def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    for dropdown in drop_downs:
        dropdown.draw(win)
        
    for text in texts:
        text.draw(win)
        
    draw_brush_widths(win)
    draw_mouse_position_text(win)
    pygame.display.update()


def draw_brush_widths(win):
    brush_widths = [
        Button(rtb_x - size_small/2, 480, size_small, size_small, drawing_color, None, None, "ellipse"),    
        Button(rtb_x - size_medium/2, 510, size_medium, size_medium, drawing_color, None, None, "ellipse") , 
        Button(rtb_x - size_large/2, 550, size_large, size_large, drawing_color, None, None, "ellipse")  
    ]
    for button in brush_widths:
        button.draw(win)
        # Set border colour
        border_color = BLACK
        if button.color == BLACK:
            border_color = GRAY
        else:
            border_color = BLACK
        # Set border width
        border_width = 2
        if ((BRUSH_SIZE == 1 and button.width == size_small) or (BRUSH_SIZE == 2 and button.width == size_medium) or (BRUSH_SIZE == 3 and button.width == size_large)): 
            border_width = 4
        else:
            border_width = 2
        # Draw border
        pygame.draw.ellipse(win, border_color, (button.x, button.y, button.width, button.height), border_width) #border

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    if col >= COLS:
        raise IndexError
    return row, col


def paint_using_brush(row, col, size):
    if BRUSH_SIZE == 1:
        grid[row][col] = drawing_color
        AntiAliasingGrid.append((row, col))
    else: #for values greater than 1        
        r = row-BRUSH_SIZE+1
        c = col-BRUSH_SIZE+1
        
        for i in range(BRUSH_SIZE*2-1):
            for j in range(BRUSH_SIZE*2-1):
                if r+i<0 or c+j<0 or r+i>=ROWS or c+j>=COLS:
                    continue
                grid[r+i][c+j] = drawing_color
                AntiAliasingGrid.append((r+i, c+j))



def paint_using_pen(row, col,size):       
    r = row-BRUSH_SIZE+1
    c = col-BRUSH_SIZE+1
    
    for i in range(BRUSH_SIZE*2-1):
        for j in range(BRUSH_SIZE*2-1):
            if r+i<0 or c+j<0 or r+i>=ROWS or c+j>=COLS or (i==2 and j == 2) or (i==0 and j == 0) or (i==0 and j ==1) or (i==2 and j ==1):
                continue
            grid[r+i][c+j] = drawing_color
            AntiAliasingGrid.append((r+i,c+j))


def paint_using_pencil(row, col,size): 
    R = drawing_color[0]
    G = drawing_color[1]
    B = drawing_color[2]
    if R<200:
        R=R+55
    if G<200:
        G=G+55
    if B<200:
        B=B+55
    light_color = (R,G,B)
    draw_button.color = light_color
    grid[row][col] = light_color
    AntiAliasingGrid.append((row,col))
    
    
def antialiasing_conversion(AntiAliasingG):
    for Coordinate in AntiAliasingGrid:
        Row = Coordinate[0]
        Column = Coordinate[1]
        
        if (Row < 39 and Row > 0) and (Column < 64 and Column > 0):
            NearColors = [(grid[Row][Column+1]), (grid[Row][Column-1]),(grid[Row+1][Column]), (grid[Row-1][Column])]
            AvgNearColors = tuple(c / 4 for c in(tuple(sum(x) for x in zip(*NearColors))))
            color = grid[Row][Column]
            SumOfColors = tuple(x + y for x, y in zip(AvgNearColors, color))
            grid[Row][Column] = tuple_divided = tuple(x / 2 for x in SumOfColors)
            
        elif (Row == 0 or Row == 39) and (Column < 64 and Column > 0):
            NearColors = [(grid[Row][Column+1]), (grid[Row][Column-1])]
            AvgNearColors = tuple(c / 2 for c in(tuple(sum(x) for x in zip(*NearColors))))
            color = grid[Row][Column]
            SumOfColors = tuple(x + y for x, y in zip(AvgNearColors, color))
            grid[Row][Column] = tuple_divided = tuple(x / 2 for x in SumOfColors)
            
        elif (Column == 0 or Column == 64) and (Row < 39 and Row > 0):
            NearColors = [(grid[Row+1][Column]), (grid[Row-1][Column])]
            AvgNearColors = tuple(c / 2 for c in(tuple(sum(x) for x in zip(*NearColors))))
            color = grid[Row][Column]
            SumOfColors = tuple(x + y for x, y in zip(AvgNearColors, color))
            grid[Row][Column] = tuple_divided = tuple(x / 2 for x in SumOfColors)

# Checks whether the coordinated are within the canvas
def inBounds(row, col):
    if row < 0 or col < 0:
        return 0
    if row >= ROWS or col >= COLS:
        return 0
    return 1

def fill_bucket(row, col, color):
   
  # Visiting array
  vis = [[0 for i in range(101)] for j in range(101)]
     
  # Creating queue for bfs
  obj = []
     
  # Pushing pair of {x, y}
  obj.append([row, col])
     
  # Marking {x, y} as visited
  vis[row][col] = 1
     
  # Until queue is empty
  while len(obj) > 0:
     
    # Extracting front pair
    coord = obj[0]
    x = coord[0]
    y = coord[1]
    preColor = grid[x][y]
   
    grid[x][y] = color
    AntiAliasingGrid.append((x,y))
       
    # Popping front pair of queue
    obj.pop(0)
   
    # For Upside Pixel or Cell
    if inBounds(x + 1, y) == 1 and vis[x + 1][y] == 0 and grid[x + 1][y] == preColor:
      obj.append([x + 1, y])
      vis[x + 1][y] = 1
       
    # For Downside Pixel or Cell
    if inBounds(x - 1, y) == 1 and vis[x - 1][y] == 0 and grid[x - 1][y] == preColor:
      obj.append([x - 1, y])
      vis[x - 1][y] = 1
       
    # For Right side Pixel or Cell
    if inBounds(x, y + 1) == 1 and vis[x][y + 1] == 0 and grid[x][y + 1] == preColor:
      obj.append([x, y + 1])
      vis[x][y + 1] = 1
       
    # For Left side Pixel or Cell
    if inBounds(x, y - 1) == 1 and vis[x][y - 1] == 0 and grid[x][y - 1] == preColor:
      obj.append([x, y - 1])
      vis[x][y - 1] = 1
    
      
def paint_using_custom_brush_1(row, col, color):
    R = drawing_color[0]
    G = drawing_color[1]
    B = drawing_color[2]
    if R<200:
        R=R+55
    if G<200:
        G=G+55
    if B<200:
        B=B+55
    light_color = (R,G,B)
    
    grid[row][col] = drawing_color
    
    up = grid[row - 1][col] == drawing_color
    down = grid[row + 1][col] == drawing_color
    left = grid[row][col - 1] == drawing_color
    right = grid[row][col + 1] == drawing_color
    
    if up and down and left and right:
        return
    
    elif up:
        grid[row][col - 1] = light_color
        grid[row + 1][col] = light_color
        grid[row][col + 1] = light_color
        
    elif down:
        grid[row][col + 1] = light_color
        grid[row][col - 1] = light_color
        grid[row - 1][col] = light_color
    
    elif right:
        grid[row][col - 1] = light_color
        grid[row + 1][col] = light_color
        grid[row - 1][col] = light_color
        
    elif left:
        grid[row][col + 1] = light_color
        grid[row + 1][col] = light_color
        grid[row - 1][col] = light_color
    
    else:
        grid[row][col + 1] = light_color
        grid[row][col - 1] = light_color
        grid[row + 1][col] = light_color
        grid[row - 1][col] = light_color
        

def paint_using_custom_brush_2(row, col, color):
    grid[row][col] = drawing_color
    
    for i in range(1,4):
        grid[row + i][col] = drawing_color
        grid[row][col + i] = drawing_color
        grid[row + i][col + i] = drawing_color
        grid[row -i][col] = drawing_color
        grid[row][col - i] = drawing_color
        grid[row - i][col - i] = drawing_color
        grid[row -i][col + i] = drawing_color
        grid[row +i][col - i] = drawing_color


def paint_using_user_brush(row, col, color):
    height = int(drop_downs[0].selected_option)
    width = int(drop_downs[1].selected_option)
    diag = int(drop_downs[2].selected_option)
    
    grid[row][col] = drawing_color
    
    for i in range(height):
        grid[row+i][col] = drawing_color
        grid[row-i][col] = drawing_color
        
    for i in range(width):
        grid[row][col+i] = drawing_color
        grid[row][col-i] = drawing_color

    for i in range(diag):
        grid[row+i][col+i] = drawing_color
        grid[row-i][col-i] = drawing_color
        grid[row+i][col-i] = drawing_color
        grid[row-i][col+i] = drawing_color

          
def make_arrow(row, col, color):
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
        make_second_arrow_head(arrow_state)
        pass
    
    LAST_POS = (-1,-1)

def make_second_arrow_head(arrow_state):
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

run = True

clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_width = 40
button_height = 40
button_y_top_row = HEIGHT - TOOLBAR_HEIGHT/2  - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT/2   + 1
button_space = 42

size_small = 25
size_medium = 35
size_large = 50

rtb_x = WIDTH + RIGHT_TOOLBAR_WIDTH/2
brush_widths = [
    Button(rtb_x - size_small/2, 480, size_small, size_small, drawing_color, None, "ellipse"),    
    Button(rtb_x - size_medium/2, 510, size_medium, size_medium, drawing_color, None, "ellipse") , 
    Button(rtb_x - size_large/2, 550, size_large, size_large, drawing_color, None, "ellipse")
]

button_y_top_row = HEIGHT - TOOLBAR_HEIGHT/2  - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT/2   + 1
button_space = 42


# Adding Buttons
buttons = []
drop_downs = []
texts = []

for i in range(int(len(COLORS)/2)):
    buttons.append( Button(100 + button_space * i, button_y_top_row, button_width, button_height, COLORS[i]) )

for i in range(int(len(COLORS)/2)):
    buttons.append( Button(100 + button_space * i, button_y_bot_row, button_width, button_height, COLORS[i + int(len(COLORS)/2)]) )

#Right toolbar buttonst
# need to add change toolbar button.
for i in range(10):
    if i == 0:
        buttons.append(Button((WIDTH) + 0.5*button_width,(i*button_height)+5,button_width,button_height,WHITE,name="Change"))#Change toolbar buttons
    else: 
        buttons.append(Button((WIDTH) + 0.5*button_width,(i*button_height)+5,button_width,button_height,WHITE,"B"+str(i-1), BLACK))#append tools

buttons.append(Button(WIDTH + 0.4*button_width,(button_height + 375)+5,button_width,button_height,WHITE, name="Anti-Aliasing", image_url="assets/anti-aliasing.png"))
buttons.append(Button(WIDTH - button_space, button_y_top_row, button_width, button_height, WHITE, "Erase", BLACK))  # Erase Button
buttons.append(Button(WIDTH - button_space, button_y_bot_row, button_width, button_height, WHITE, "Clear", BLACK))  # Clear Button
buttons.append(Button(WIDTH - 2*button_space, button_y_top_row,button_width-5, button_height-5, name = "FillBucket",image_url="assets/paint-bucket.png")) #FillBucket
buttons.append(Button(WIDTH - 3*button_space, button_y_top_row,button_width-5, button_height-5, name = "Brush",image_url="assets/paint-brush.png")) #Brush
buttons.append(Button(WIDTH - 2*button_space, button_y_bot_row,button_width-5, button_height-5, name = "Arrow",image_url="assets/arrow-up.png")) #Arrows
buttons.append(Button(WIDTH - 3*button_space, button_y_bot_row,button_width-5, button_height-5, name = "Line",image_url="assets/line.png")) #Line
buttons.append(Button(WIDTH - 4*button_space, button_y_bot_row,button_width-5, button_height-5, name = "Pen",image_url="assets/Pen.png")) #Pen
buttons.append(Button(WIDTH - 4*button_space, button_y_top_row,button_width-5, button_height-5, name = "Pencil",image_url="assets/Pencil.png")) #Pencil

FIX_SIZE = False
AntiAliasingGrid = []
draw_button = Button(5, HEIGHT - TOOLBAR_HEIGHT/2 - 30, 60, 60, drawing_color)
buttons.append(draw_button)

# *************************Draw Normal Straight LINE Starts****************
line_draw_count = 0
start_line, end_line = {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}
# first_coord_chosen = False

def same_row_diff_col(start, end, start_col_bigger):
    global line_draw_count, start_line, end_line, grid
    if start_col_bigger:
        for num in range(end["col"], start["col"] + 1):
            grid[start["row"]][num] = drawing_color
    else:
        for num in range(start["col"] + 1, end["col"] + 1):
            grid[start["row"]][num] = drawing_color
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def same_col_diff_row(start, end, start_row_bigger):
    global line_draw_count, start_line, end_line, grid
    if start_row_bigger:
        for num in range(end["row"], start["row"]):
            grid[num][start["col"]] = drawing_color
    else:
        for num in range(start["row"] + 1, end["row"] + 1):
            grid[num][start["col"]] = drawing_color
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def end_col_bigger_row_smaller(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1):
        row_to_color, col_to_color = start["row"] - count, start["col"] + count
        if row_to_color >= end["row"] or col_to_color <= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color

def end_col_bigger_row_bigger(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1):
        row_to_color, col_to_color = start["row"] + count, start["col"] + count
        if row_to_color <= end["row"] or col_to_color <= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color

def end_col_smaller_row_smaller(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1):
        row_to_color, col_to_color = start["row"] - count, start["col"] - count
        if row_to_color >= end["row"] or col_to_color >= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color

def end_col_smaller_row_bigger(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1):
        row_to_color, col_to_color = start["row"] + count, start["col"] - count
        if row_to_color <= end["row"] or col_to_color >= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color

def diff_col_diff_row(start, end):
    global line_draw_count, start_line, end_line
    if end["col"] > start["col"]:
        if end["row"] < start["row"]:
            end_col_bigger_row_smaller(start, end)
        else:
            end_col_bigger_row_bigger(start, end)
    else:
        if end["row"] < start["row"]:
            end_col_smaller_row_smaller(start, end)
        else:
            end_col_smaller_row_bigger(start, end)
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def draw_full_straight_line(row_num, col_num):
    global line_draw_count, start_line, end_line
    if line_draw_count == 0:
        start_line["row"], start_line["col"] = row_num, col_num
        grid[row_num][col_num] = drawing_color
        line_draw_count = 1

    elif line_draw_count == 1:
        end_line["row"], end_line["col"] = row_num, col_num
        if start_line["row"] == end_line["row"] and start_line["col"] != end_line["col"]:
            if start_line["col"] < end_line["col"]:
                same_row_diff_col(start_line, end_line, False)
            else:
                same_row_diff_col(start_line, end_line, True)

        elif start_line["col"] == end_line["col"] and start_line["row"] != end_line["row"]:
            if start_line["row"] < end_line["row"]:
                same_col_diff_row(start_line, end_line, False)
            else:
                same_col_diff_row(start_line, end_line, True)

        elif start_line["col"] != end_line["col"] and start_line["row"] != end_line["row"]:
            diff_col_diff_row(start_line, end_line)
        
        else:
            grid[start_line["row"]][start_line["col"]] = drawing_color
            line_draw_count = 0 

# *************************Draw Normal Straight LINE Ends****************


# *************************Draw Dotted Straight LINE Starts****************

def same_row_diff_col_dotted(start, end, start_col_bigger):
    global line_draw_count, start_line, end_line, grid
    if start_col_bigger:
        for num in range(end["col"], start["col"] + 1, 2):
            grid[start["row"]][num] = drawing_color
    else:
        for num in range(start["col"] + 1, end["col"] + 1, 2):
            grid[start["row"]][num] = drawing_color
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def same_col_diff_row_dotted(start, end, start_row_bigger):
    global line_draw_count, start_line, end_line, grid
    if start_row_bigger:
        for num in range(end["row"], start["row"], 2):
            grid[num][start["col"]] = drawing_color
    else:
        for num in range(start["row"] + 1, end["row"] + 1, 2):
            grid[num][start["col"]] = drawing_color
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def end_col_bigger_row_smaller_dotted(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1, 2):
        row_to_color, col_to_color = start["row"] - count, start["col"] + count
        if row_to_color >= end["row"] or col_to_color <= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color

def end_col_bigger_row_bigger_dotted(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1, 2):
        row_to_color, col_to_color = start["row"] + count, start["col"] + count
        if row_to_color <= end["row"] or col_to_color <= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color

def end_col_smaller_row_smaller_dotted(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1, 2):
        row_to_color, col_to_color = start["row"] - count, start["col"] - count
        if row_to_color >= end["row"] or col_to_color >= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color

def end_col_smaller_row_bigger_dotted(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1, 2):
        row_to_color, col_to_color = start["row"] + count, start["col"] - count
        if row_to_color <= end["row"] or col_to_color >= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color

def diff_col_diff_row_dotted(start, end):
    global line_draw_count, start_line, end_line
    if end["col"] > start["col"]:
        if end["row"] < start["row"]:
            end_col_bigger_row_smaller_dotted(start, end)
        else:
            end_col_bigger_row_bigger_dotted(start, end)
    else:
        if end["row"] < start["row"]:
            end_col_smaller_row_smaller_dotted(start, end)
        else:
            end_col_smaller_row_bigger_dotted(start, end)
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def draw_dotted_straight_line(row_num, col_num):
    global line_draw_count, start_line, end_line
    if line_draw_count == 0:
        start_line["row"], start_line["col"] = row_num, col_num
        grid[row_num][col_num] = drawing_color
        line_draw_count = 1

    elif line_draw_count == 1:
        end_line["row"], end_line["col"] = row_num, col_num
        if start_line["row"] == end_line["row"] and start_line["col"] != end_line["col"]:
            if start_line["col"] < end_line["col"]:
                same_row_diff_col_dotted(start_line, end_line, False)
            else:
                same_row_diff_col_dotted(start_line, end_line, True)

        elif start_line["col"] == end_line["col"] and start_line["row"] != end_line["row"]:
            if start_line["row"] < end_line["row"]:
                same_col_diff_row_dotted(start_line, end_line, False)
            else:
                same_col_diff_row_dotted(start_line, end_line, True)

        elif start_line["col"] != end_line["col"] and start_line["row"] != end_line["row"]:
            diff_col_diff_row_dotted(start_line, end_line)
        
        else:
            grid[start_line["row"]][start_line["col"]] = drawing_color
            line_draw_count = 0 

# *************************Draw Dotted Straight LINE ends******************

# *************************Draw Full Multiline Starts**********************

def same_row_diff_col_multi(start, end, start_col_bigger):
    global line_draw_count, start_line, end_line, grid
    if start_col_bigger:
        for num in range(end["col"], start["col"] + 1):
            grid[start["row"]][num] = drawing_color
            grid[start["row"] + 2][num] = drawing_color
    else:
        for num in range(start["col"] + 1, end["col"] + 1):
            grid[start["row"]][num] = drawing_color
            grid[start["row"] + 2][num] = drawing_color
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def same_col_diff_row_multi(start, end, start_row_bigger):
    global line_draw_count, start_line, end_line, grid
    if start_row_bigger:
        for num in range(end["row"], start["row"]):
            grid[num][start["col"]] = drawing_color
            grid[num][start["col"] + 2] = drawing_color
    else:
        for num in range(start["row"] + 1, end["row"] + 1):
            grid[num][start["col"]] = drawing_color
            grid[num][start["col"] + 2] = drawing_color
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def end_col_bigger_row_smaller(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1):
        row_to_color, col_to_color = start["row"] - count, start["col"] + count
        if row_to_color >= end["row"] or col_to_color <= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color
            grid[row_to_color + 2][col_to_color + 2] = drawing_color

def end_col_bigger_row_bigger(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1):
        row_to_color, col_to_color = start["row"] + count, start["col"] + count
        if row_to_color <= end["row"] or col_to_color <= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color
            grid[row_to_color + 2][col_to_color - 2] = drawing_color

def end_col_smaller_row_smaller(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1):
        row_to_color, col_to_color = start["row"] - count, start["col"] - count
        if row_to_color >= end["row"] or col_to_color >= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color
            grid[row_to_color - 2][col_to_color + 2] = drawing_color

def end_col_smaller_row_bigger(start, end):
    global grid
    hypotenuse = int(math.sqrt(((end["row"] - start["row"]) ** 2) + ((end["col"] - start["col"]) ** 2)))
    for count in range(0, hypotenuse + 1):
        row_to_color, col_to_color = start["row"] + count, start["col"] - count
        if row_to_color <= end["row"] or col_to_color >= end["col"]:
            grid[row_to_color][col_to_color] = drawing_color
            grid[row_to_color + 2][col_to_color + 2] = drawing_color

def diff_col_diff_row(start, end):
    global line_draw_count, start_line, end_line
    if end["col"] > start["col"]:
        if end["row"] < start["row"]:
            end_col_bigger_row_smaller(start, end)
        else:
            pass
            end_col_bigger_row_bigger(start, end)
    else:
        if end["row"] < start["row"]:
            pass
            end_col_smaller_row_smaller(start, end)
        else:
            pass
            end_col_smaller_row_bigger(start, end)
    line_draw_count, start_line, end_line = 0, {"row" : 0, "col" : 0}, {"row" : 0, "col" : 0}

def draw_full_straight_multiline(row_num, col_num):
    global line_draw_count, start_line, end_line
    if line_draw_count == 0:
        start_line["row"], start_line["col"] = row_num, col_num
        grid[row_num][col_num] = drawing_color
        line_draw_count = 1

    elif line_draw_count == 1:
        end_line["row"], end_line["col"] = row_num, col_num
        if start_line["row"] == end_line["row"] and start_line["col"] != end_line["col"]:
            if start_line["col"] < end_line["col"]:
                same_row_diff_col_multi(start_line, end_line, False)
            else:
                same_row_diff_col_multi(start_line, end_line, True)

        elif start_line["col"] == end_line["col"] and start_line["row"] != end_line["row"]:
            if start_line["row"] < end_line["row"]:
                same_col_diff_row_multi(start_line, end_line, False)
            else:
                same_col_diff_row_multi(start_line, end_line, True)

        elif start_line["col"] != end_line["col"] and start_line["row"] != end_line["row"]:
            diff_col_diff_row(start_line, end_line)
        
        else:
            grid[start_line["row"]][start_line["col"]] = drawing_color
            grid[start_line["row"]][start_line["col"] + 2] = drawing_color
            line_draw_count = 0 

# *************************Draw Full Multiline Ends**********************    
 

while run:
    clock.tick(FPS) #limiting FPS to 60 or any other value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #if user closed the program
            run = False
        
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)

                if STATE == "COLOR":
                    paint_using_brush(row, col, BRUSH_SIZE)

                elif STATE == "LINE":
                    draw_full_straight_line(row, col)

                elif STATE == "DOTTED-LINE":
                    draw_dotted_straight_line(row, col)

                elif STATE == "FULL-MULTILINE":
                    draw_full_straight_multiline(row, col)

                elif STATE == "FILL":
                    fill_bucket(row, col, drawing_color)
                
                elif STATE == "PEN":
                    paint_using_pen(row, col, BRUSH_SIZE)

                elif STATE == "PENCIL":
                    paint_using_pencil(row, col, BRUSH_SIZE)

                elif STATE == "ARROW":
                    make_arrow(row, col, drawing_color)
                
                elif STATE == "CB1":
                    paint_using_custom_brush_1(row, col, drawing_color)
                    
                elif STATE == "CB2":
                    paint_using_custom_brush_2(row, col, drawing_color)
                    
                elif STATE == "UB1":
                    paint_using_user_brush(row, col, drawing_color)
                            

            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if button.text == "Clear":
                        FIX_SIZE = False
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        draw_button.color = drawing_color
                        line_draw_count = 0
                        STATE = "COLOR"
                        break

                    if button.name == "FillBucket":
                        FIX_SIZE = False
                        STATE = "FILL"
                        break
                    
                    if button.name == "Change":
                        FIX_SIZE = False
                        Change = not Change
                        for i in range(10):
                            if i == 0:
                                buttons.append(Button(WIDTH + 0.5*button_width,(i*button_height)+5,button_width,button_height,WHITE,name="Change"))
                            else:
                                if Change == False:  
                                    buttons.append(Button(WIDTH + 0.5*button_width,(i*button_height)+5,button_width,button_height,WHITE,"B"+str(i-1), BLACK))
                                if Change == True:
                                   buttons.append(Button(WIDTH + 0.5*button_width,(i*button_height)+5,button_width,button_height,WHITE,"C"+str(i-1), BLACK))
                        break
                     
                    if button.name == "Brush":
                        STATE = "COLOR"
                        FIX_SIZE = False
                        custom_brushes = []
                        custom_brushes.append(Button(WIDTH - 11.5*button_space, button_y_top_row,button_width-5, button_height-5, BLACK, name = "CB1", image_url="assets/Gradient-Brush.png"))
                        custom_brushes.append(Button(WIDTH - 11.5*button_space, button_y_bot_row,button_width-5, button_height-5, BLACK, name = "CB2", image_url="assets/Snowflake.png"))
                        custom_brushes.append(Button(WIDTH - 10.5*button_space, button_y_bot_row,button_width-5, button_height-5, BLACK, name = "Add-Brush", image_url="assets/plus.png"))
                        buttons.extend(custom_brushes)
                        break

                    if button.name == "CB1":
                        STATE = "CB1" 
                        BRUSH_SIZE = 1
                        break
                    
                    if button.name == "CB2":
                        STATE = "CB2" 
                        BRUSH_SIZE = 3
                        break
                    
                    if button.name == "Pen":
                        STATE = "PEN"
                        BRUSH_SIZE = 2
                        FIX_SIZE = True
                        break

                    if button.name == "Pencil":
                        STATE = "PENCIL"
                        BRUSH_SIZE = 1
                        FIX_SIZE = True
                        break

                    if button.name == "Line":
                        STATE = "LINE"
                        dotted_line_btn = Button(WIDTH - 11.5 * button_space, button_y_top_row,button_width-5, button_height-5, name = "Dotted-Line",image_url="assets/dotted_line.jpg")
                        full_multiline_btn = Button(WIDTH - 11.5 * button_space, button_y_top_row + 40,button_width-5, button_height-5, name = "Full-Multiline",image_url="assets/two-lines.png")
                        buttons.append(dotted_line_btn)
                        buttons.append(full_multiline_btn)
                        break
                    
                    if button.name == "Dotted-Line":
                        STATE = "DOTTED-LINE"
                        break

                    if button.name == "Full-Multiline":
                        STATE = "FULL-MULTILINE"
                        break

                    if button.name == "Arrow":
                        STATE = "ARROW"
                        MULTI_HEAD_BUTTON = Button(WIDTH - 11.5*button_space, button_y_top_row,button_width-5, button_height-5, name = "Multi-Head",image_url="assets/multihead.png")
                        buttons.append(MULTI_HEAD_BUTTON)
                        break
                    
                    if button.name == "Multi-Head":
                        MULTI_HEAD = not MULTI_HEAD
                        break
                    
                    if button.name == "Add-Brush":
                        drop_downs.append(Dropdown(WIDTH - 7.5*button_space, button_y_top_row, 40, 25, get_font(12), ['1', '2', '3', '4', '5'], name="dp1"))
                        drop_downs.append(Dropdown(WIDTH - 5.5*button_space, button_y_top_row, 40, 25, get_font(12), ['1', '2', '3', '4', '5'], name="dp2"))
                        drop_downs.append(Dropdown(WIDTH - 9.5*button_space, button_y_top_row, 40, 25, get_font(12), ['1', '2', '3', '4', '5'], name="dp3"))
                        texts.append(Text(WIDTH - 8.5*button_space, button_y_top_row+5, get_font(12), 'Height:'))
                        texts.append(Text(WIDTH - 6.5*button_space, button_y_top_row+5, get_font(12), 'Width:'))
                        texts.append(Text(WIDTH - 10.5*button_space-5, button_y_top_row+5, get_font(12), 'Diagonal:'))
                        STATE = "UB1"
                        break
                    
                    if button.name == "Anti-Aliasing":
                        if (STATE == "PENCIL") or (STATE == "PEN") or (STATE == "FILL") or (STATE == "COLOR"): 
                            antialiasing_conversion(AntiAliasingGrid)
                            break
                        break

                    drawing_color = button.color
                    draw_button.color = drawing_color
                    
                    break
                
                for button in brush_widths:
                    if not button.clicked(pos):
                        continue
                    if FIX_SIZE:
                        continue
                    #set brush width
                    if button.width == size_small:
                        BRUSH_SIZE = 1
                    elif button.width == size_medium:
                        BRUSH_SIZE = 2
                    elif button.width == size_large:
                        BRUSH_SIZE = 3

                    STATE = "COLOR"
                
                for dropdown in drop_downs:
                    if dropdown.name == "dp1":
                        dropdown.handle_event(event)
                    
                    if dropdown.name == "dp2":
                        dropdown.handle_event(event)
                    
                    if dropdown.name == "dp3":
                        dropdown.handle_event(event)

                
    if STATE != "ARROW":
            LAST_POS = (-1,-1)
            MULTI_HEAD = False
            for button in buttons:
                if button.name == "Multi-Head":
                    buttons.remove(button)

    if STATE != "LINE" and STATE  != "DOTTED-LINE" and STATE  != "FULL-MULTILINE":
        for button in buttons:
            if button.name == "Dotted-Line":
                buttons.remove(button)
            if button.name == "Full-Multiline":
                buttons.remove(button)
    
    if STATE != "COLOR" and STATE !="CB1" and STATE !="CB2" and STATE != "UB1":
        for button in buttons:
            if button.name == "CB1":
                buttons.remove(button)
            if button.name == "CB2" or button.name == "Add-Brush":
                buttons.remove(button)
                
    if STATE != "UB1":
        drop_downs = []
        texts = []
                

    draw(WIN, grid, buttons)

pygame.quit()

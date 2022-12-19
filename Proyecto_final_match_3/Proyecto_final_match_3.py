import pygame
import random
import os
#GlobaL Variables

list_colors = { 1 :"red.png",               #Uses gem.color method to change sprite
                2 :"orange.png",
                3 :"yellow.png",
                4 :"green.png",
                5 :"blue.png",
                6 :"purple.png",
                7 :"special.png",
                0 : "empty.png"
                }

list_selected = {   1 :"red_s.png",
                    2 :"orange_s.png",
                    3 :"yellow_s.png",
                    4 :"green_s.png",
                    5 :"blue_s.png",
                    6 :"purple_s.png",
                    7 :"special_s.png",
                    0 : "empty.png",
                    }

list_swapped = {    1 :"red_b.png",         #Visual reference for the gems being swapped
                    2 :"orange_b.png",
                    3 :"yellow_b.png",
                    4 :"green_b.png",
                    5 :"blue_b.png",
                    6 :"purple_b.png",
                    7 :"special_b.png",
                    0 : "empty.png"
                    }
panels = {  1: "title.png",
            2: "score.png",
            3: "play_chart.png"
            }

list_grid = []
list_panel = []
list_text = []
list_text_s = []
empty_ocurrences = 0
empty_ocurrences1 = 0
list_gem = []
list_gem2 = []

gem_horizontal_pop2 = []
gem_vertical_pop2 = []
gem_horizontal_pop1 = []
gem_vertical_pop1 = []

n_size = 64
n_pos = n_size
n_grid = 7
char_count4 = 0

grid_size = 5
offset_x = 300
offset_y = 100
contadorX = offset_x
contadorY = offset_y

gem_comp_color1 = 0
gem_comp_color2 = 0
gem_compy = 0
gem_compx = 0
gem_compy1 = 0
gem_compx2 = 0
gem_comp_color1a = 0
score_ingame = 0

gem_comp_ID1 = 0
gem_comp_ID2 = 0
gem_comp_ID1a = 0
user_name = "Invitado"
selection = False
pos_x = 0
pos_y = 0
game_over = 0
local_score = 0
brown_color = (206, 124, 64)
white = (255, 255, 255)


class grid_background():                        #Creates grid instance
    def __init__(self):
        self.image = pygame.image.load("grid.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
      
class background():                        #Creates backgrund instance
    def __init__(self):
        self.image = pygame.image.load("wallpaper.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class panel():                        #Creates backgrund instance
    def __init__(self):
        self.image = pygame.image.load("play_chart.png")
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.x = 0
        self.rect.y = 0

class text():
    def __init__(self):
        self.font = pygame.font.Font("arial.ttf", 28)
        self.text = self.font.render("", True, white, brown_color)
        self.rect = self.text.get_rect()
        self.rect.center = (0, 0)
        self.Is_Score = 0

    def change_text(self, string1):
        self.text = self.font.render(string1, True, white, brown_color)
    def change_text_size(self, num):
         self.font = pygame.font.Font("arial.ttf", num)
    pass

class gem_instance():                           #Creates gem instance
    def __init__(self):
        self.ID = 0
        self.image = pygame.image.load("empty.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.actual_color = 0
        self.clicked = False
        self.dummy = 1
        
    def gem_swap(self):                                         #If gem swap is sucessful list changes to represent both gems being swapped
        self.image = pygame.image.load(list_swapped[self.actual_color])

    def color_gem(self, color):                             #Changes color of instance, imports parameter color integer and asociates with string...
        self.image = pygame.image.load(list_colors[color])  #see list_colors for details
        self.actual_color = color                           #Sets color value for diferent color variations

    def gem_clicked(self):                                  #Doesn´t change color, changes sprite list to visualize selection, uses color member as key for color
        self.clicked = True                                 #Sets value to clicked
        self.image = pygame.image.load(list_selected[self.actual_color])    ##see list_selected for details
    
    def gem_unclick(self):                                  #unselects current gem and reassigns  "list_colors"
        self.clicked = False
        self.image = pygame.image.load(list_colors[self.actual_color])


def grid_place():                               #CREATES AND PLACES grid background
    global contadorY, offset_y
    global contadorX, offset_x
    contadorY = offset_y
    while contadorY < (n_size * n_grid + offset_y):
        contadorX = offset_x
        while contadorX < (n_size * n_grid + offset_x):            
            grid_back = grid_background()
            grid_back.rect.x = contadorX
            grid_back.rect.y = contadorY
            list_grid.append(grid_back)
            contadorX += n_size
        contadorY += n_size

def draw_grid():                                #Draws grid
    for grid_back1 in list_grid:
        screen.blit(grid_back1.image, grid_back1.rect)

def gems_place():                               #CREATES AND PLACES gems
    ID_gem = 1
    global offset_y
    global offset_x
    contadorY = offset_y
    while contadorY < (n_size * n_grid + offset_y):
        contadorX = offset_x
        while contadorX < (n_size * n_grid + offset_x):            
            gem = gem_instance()                #Creates gem
            gem.ID = ID_gem                     #Assigns ID
            ID_gem += 1
            gem.rect.x = contadorX              #Assigns position
            gem.rect.y = contadorY
            gem.color_gem(random.randint(1, 6)) #Randomly assigns color using class method color gem
            list_gem.append(gem)                #Appends to list
            contadorX += n_size
        contadorY += n_size

def score_place():
    score = panel()
    score.rect.x = 50
    score.rect.y = 100
    score.image = pygame.image.load("chart_empty.png")
    menu = panel()
    menu.rect.x = 50
    menu.rect.y = 200
    menu.image = pygame.image.load("menu.png")
    list_panel.append(menu)
    list_panel.append(score)
    score_rect = text()
    score_rect.rect.center = (70, 130)
    score_rect.Is_Score = 1
    list_text.append(score_rect)
    pass

def scramble_gems():                            #scrambles already existing gems
    for gem in list_gem:
        gem.color_gem(random.randint(1, 6))

def unselect_gems():                            #Unselects gems and sets previous selection to false, uses class method "Unclick"
    global selection
    selection = False
    for gem in list_gem:
        gem.gem_unclick()

def draw_gem():                                 #Draws current state of gems
    for gem in list_gem:
        screen.blit(gem.image, gem.rect)

def draw_panels():                                 #Draws panels
    for panel1 in list_panel:
        screen.blit(panel1.image, panel1.rect)

def draw_score():
    global score_ingame, user_name
    for score_rect1 in list_text:
        if score_rect1.Is_Score == 1:
            score_rect1.text = score_rect1.font.render(user_name + " " + str(score_ingame), True, (255, 255, 255), (206, 124, 64))        
        screen.blit(score_rect1.text, score_rect1.rect)
    pass

def update_screen():                            #Uses combinations of functions to update the screen
    draw_panels()
    draw_grid()
    draw_gem()
    draw_score()
    pygame.display.flip()

def one_row_adder():
    global empty_ocurrences1
    empty_ocurrences1 = 0
    for gem in list_gem:
        if gem.actual_color == 0 and (gem.rect.y < n_size + offset_y):
            gem.color_gem(random.randint(1, 6))
            empty_ocurrences1 +=1
            update_screen()
            pygame.time.delay(100)
        elif gem.actual_color == 0 and (gem.rect.y >= n_size + offset_y):
            empty_checker()          
    if empty_ocurrences1 != 0:
        one_row_adder()
    pass

def empty_checker():                            #Reversive function, scans for empty occurences every cycle, if none existe it means no swapped was made
    global n_pos, empty_ocurrences              #wich means no more cycles neaded
    n_pos = 0
    empty_ocurrences = 0
    for gem in list_gem:
        if gem.actual_color != 0:
            end = 0
            precompare_gem(gem)
            while (end == 0):
                end = check_empty_V()           #cycles vertically downwards for empty spaces
    if empty_ocurrences != 0:
        empty_checker()
    pass

def check_empty_V():                            #If an empty slot exists below the actual slot, swaps gem and adds one to occurences
    global n_pos, empty_ocurrences
    global gem_compy, gem_comp_color1
    n_pos = n_size
    for gem in list_gem:
        if (gem_compx == gem.rect.x and (gem_compy == (gem.rect.y - n_pos))) and (gem.actual_color == 0):
            change_gem(gem)
            update_screen()
            empty_ocurrences += 1
            return 0
    return 1
    pass

def list_eraser(gem):
    gem_vertical_pop2.clear()
    gem_horizontal_pop2.clear()
    gem_horizontal_pop2.append(gem.dummy)       #Dummy member in gem class is used to obtain number of matchable gems
    gem_vertical_pop2.append(gem.dummy)
    gem_vertical_pop1.clear()
    gem_horizontal_pop1.clear()
    gem_horizontal_pop1.append(gem.ID)          #Obtains ID of gems in case of being matchable
    gem_vertical_pop1.append(gem.ID)

def match3_checker(gem):                        #Algorithm for checking match 3 every time a gem was sucessfully swapped
    global n_pos, score_ingame
    global selection, gem_compx, gem_compy, gem_comp_color1
    list_eraser(gem)
    for gem1 in list_gem:
        n_pos = n_size
        if (gem_compy == gem1.rect.y and (gem_compx == (gem1.rect.x + n_pos))) and (gem1.actual_color == gem_comp_color1):      #Scans every side for posible matches
            gem1.gem_clicked()
            gem_horizontal_pop2.append(gem1.dummy)
            gem_horizontal_pop1.append(gem1.ID)
            HP = True
            while(HP == True):                                                                                                  #If a match is found this function scans more matches in the same direction  
                HP = check_adyacent_h_plus()                                                                                    #until a different color gem is found, exits the loop
        elif (gem_compy == gem1.rect.y and (gem_compx == (gem1.rect.x - n_pos))) and (gem1.actual_color == gem_comp_color1):    #Repeats process for each side
            gem1.gem_clicked()
            gem_horizontal_pop2.append(gem1.dummy)
            gem_horizontal_pop1.append(gem1.ID)
            HM = True
            while(HM == True):
                HM = check_adyacent_h_minus()                                                                                   #<----These functions scan in one direction for matches
        elif (gem_compx == gem1.rect.x and (gem_compy == (gem1.rect.y + n_pos))) and (gem1.actual_color == gem_comp_color1):
            gem1.gem_clicked()
            gem_vertical_pop2.append(gem1.dummy)
            gem_vertical_pop1.append(gem1.ID)
            VP = True
            while(VP == True):
                VP = check_adyacent_v_plus()
        elif (gem_compx == gem1.rect.x and (gem_compy == (gem1.rect.y - n_pos))) and (gem1.actual_color == gem_comp_color1):
            gem1.gem_clicked()
            gem_vertical_pop2.append(gem1.dummy)
            gem_vertical_pop1.append(gem1.ID)
            VM = True
            while(VM == True):
                VM = check_adyacent_v_minus()
        else:            
            continue

    if gem_horizontal_pop2.count(1) < 3:                 #If less than 3 gems are matched on an axis the axis list is cleared before exiting the function
         gem_horizontal_pop1.clear()
    if gem_vertical_pop2.count(1) < 3:
        gem_vertical_pop1.clear()

    if gem_vertical_pop2.count(1) < 3 and gem_horizontal_pop2.count(1) < 3:
        return False
    else:
        if gem_horizontal_pop2.count(1) >= 3:
            score_ingame += gem_horizontal_pop2.count(1) * 10
        if gem_vertical_pop2.count(1) >= 3:
            score_ingame += gem_vertical_pop2.count(1) * 10
        return True
    pass 

def check_adyacent_h_plus():
    global n_pos
    global gem_compy, gem_comp_color1
    n_pos += n_size
    for gem in list_gem:
        if (gem_compy == gem.rect.y and (gem_compx == (gem.rect.x + n_pos))) and (gem.actual_color == gem_comp_color1):
            gem.gem_clicked()
            gem_horizontal_pop2.append(gem.dummy)
            gem_horizontal_pop1.append(gem.ID)
            return True
    return False
    pass

def check_adyacent_h_minus():
    global n_pos
    global gem_compy, gem_comp_color1
    n_pos += n_size
    for gem in list_gem:
        if (gem_compy == gem.rect.y and (gem_compx == (gem.rect.x - n_pos))) and (gem.actual_color == gem_comp_color1):
            gem.gem_clicked()
            gem_horizontal_pop2.append(gem.dummy)
            gem_horizontal_pop1.append(gem.ID)
            return True
    return False
    pass

def check_adyacent_v_plus():
    global n_pos
    global gem_compy, gem_comp_color1
    n_pos += n_size
    for gem in list_gem:
        if (gem_compx == gem.rect.x and (gem_compy == (gem.rect.y + n_pos))) and (gem.actual_color == gem_comp_color1):
            gem.gem_clicked()
            gem_vertical_pop2.append(gem.dummy)
            gem_vertical_pop1.append(gem.ID)
            return True
    return False
    pass

def check_adyacent_v_minus():
    global n_pos
    global gem_compy, gem_comp_color1
    n_pos += n_size
    for gem in list_gem:
        if (gem_compx == gem.rect.x and (gem_compy == (gem.rect.y - n_pos))) and (gem.actual_color == gem_comp_color1):
            gem.gem_clicked()
            gem_vertical_pop2.append(gem.dummy)
            gem_vertical_pop1.append(gem.ID)
            return True
    return False
    pass

def precompare_gem(gem):                    #Stores values of selected gem before swapping
    global selection
    global gem_compx, gem_compy, gem_comp_ID1, gem_comp_color1
    selection = True
    gem_compx = gem.rect.x
    gem_compy = gem.rect.y
    gem_comp_ID1 = gem.ID
    gem_comp_color1 = gem.actual_color
    pass

def precompare_gem_persistant(gem):                    #Stores values of selected gem during second selections, persists and if theres no match swaps original gems
    global selection
    global gem_compx1, gem_compy1, gem_comp_ID1a, gem_comp_color1a
    selection = True
    gem_compx1 = gem.rect.x
    gem_compy1 = gem.rect.y
    gem_comp_ID1a = gem.ID
    gem_comp_color1a = gem.actual_color
    pass

def change_gem(gem):                          #Stores values of the second gem selected, then swaps values for the first ones
    global gem_comp_color2, gem_comp_color1, gem_comp_ID1
    gem_comp_color2 = gem.actual_color
    gem.actual_color = gem_comp_color1
    gem.gem_swap()
    for gem in list_gem:
        if gem.ID == gem_comp_ID1:
            gem.actual_color = gem_comp_color2
            gem.gem_swap()
            update_screen()
            pygame.time.delay(100)
    pass


def un_change_gem(gem):                          #Swap gems back to original positions using th persistent values
    global gem_comp_color2, gem_comp_color1a, gem_comp_ID1a
    gem_comp_color1a = gem.actual_color
    gem.actual_color = gem_comp_color2
    gem.gem_swap()
    for gem in list_gem:
        if gem.ID == gem_comp_ID1a:
            gem.actual_color = gem_comp_color1a
            gem.gem_swap()
            update_screen()
            pygame.time.delay(100)
    pass
    
def clear_gem(list):                          #Removes gems after match 3
    for id in list:
        for gem in list_gem:
            if gem.ID == id:
                gem.color_gem(0)
    pass

def swap_gem(gem):                              #Evaluates if its posible to swap a gem, if posible it swaps
    change_gem(gem)
    precompare_gem(gem)
    unselect_gems()
    if match3_checker(gem) == False:
        precompare_gem(gem)
        un_change_gem(gem)
        game_over_screen()
        return 1                                #<---- If theres no match exits function leaving without changes
    update_screen()                             #Else it continues
    pygame.time.delay(200)
    clear_gem(gem_horizontal_pop1)
    clear_gem(gem_vertical_pop1)
    update_screen()
    pygame.time.delay(200)
    empty_checker()
    unselect_gems()
    one_row_adder()
    unselect_gems()
    return 0

def game_placement():                           #Initial game placement
    grid_place()
    draw_grid()
    gems_place()
    draw_gem()
    score_place()

def game_execution():                           #Executes games
    global game_over, wall
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_file()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            save_file()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for panel1 in list_panel:
                    if panel1.rect.collidepoint(pos):
                        if panel1.rect.y == 200 and panel1.rect.x == 50:
                            save_file()
                            return 1
                if selection == False:
                    for gem in list_gem:
                        if gem.rect.collidepoint(pos):
                            if gem.clicked == False:
                                gem.gem_clicked()
                                precompare_gem(gem)
                                precompare_gem_persistant(gem)
                            else:
                                unselect_gems()
                elif selection == True:
                    for gem in list_gem:
                        if gem.rect.collidepoint(pos):
                            if gem.clicked == False:
                                if ((gem.rect.x) == (gem_compx - n_size)) and ((gem.rect.y) < (gem_compy + n_size) and (gem.rect.y) > (gem_compy - n_size)):
                                    game_over = swap_gem(gem)
                                    break
                                if ((gem.rect.x) == (gem_compx + n_size)) and ((gem.rect.y) < (gem_compy + n_size) and (gem.rect.y) > (gem_compy - n_size)):
                                    game_over = swap_gem(gem)
                                    break
                                if ((gem.rect.y) == (gem_compy + n_size)) and ((gem.rect.x) < (gem_compx + n_size) and (gem.rect.x) > (gem_compx - n_size)):
                                    game_over = swap_gem(gem)
                                    break
                                if ((gem.rect.y) == (gem_compy - n_size)) and ((gem.rect.x) < (gem_compx + n_size) and (gem.rect.x) > (gem_compx - n_size)):
                                    game_over = swap_gem(gem)
                                    break
                                else:
                                    unselect_gems()
                            else:
                                unselect_gems()

        screen.blit(wall.image, wall.rect)
        update_screen()
        frame_rate.tick(60)
    return game_over

def Initial_placement():
    global wall    
    screen.fill((0, 0, 0))
    screen.blit(wall.image, wall.rect)

def main_menu():
    global list_panel
    list_panel.clear()
    list_text.clear()
    list_text_s.clear()
    screen.blit(wall.image, wall.rect)
    play = panel()
    play.rect.x = 310
    play.rect.y = 200
    list_panel.append(play)
    update_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:
                pos = pygame.mouse.get_pos()
                if play.rect.collidepoint(pos):
                    play.clicked = True
                    list_panel.clear()
                    return 1
    frame_rate.tick(60)
    return 0

def dif_menu():
    global list_panel
    high = panel()
    medium = panel()
    low = panel()
    high.rect.x = 310
    high.rect.y = 200
    medium.rect.x = 310
    medium.rect.y = 300
    low.rect.x = 310
    low.rect.y = 400
    high.image = pygame.image.load("high.png")
    medium.image = pygame.image.load("medium.png")
    low.image = pygame.image.load("low.png")
    list_panel.append(high)
    list_panel.append(medium)
    list_panel.append(low)
    update_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:
                pos = pygame.mouse.get_pos()
                if low.rect.collidepoint(pos):
                    low.clicked = True
                    list_panel.clear()
                    return 3
                if medium.rect.collidepoint(pos):
                    medium.clicked = True
                    list_panel.clear()
                    return 4
                if high.rect.collidepoint(pos):
                    high.clicked = True
                    list_panel.clear()
                    return 5
    frame_rate.tick(60)
    return 1


def game_over_screen():
    global list_panel
    game_over_panel = panel()
    game_over_panel.image = pygame.image.load("game_over.png")
    game_over_panel.rect.x = 300
    game_over_panel.rect.y = 100
    screen.blit(game_over_panel.image, game_over_panel.rect)
    save_file()
    pygame.display.flip()
    pygame.time.delay(2000)
    pass

def game_loop():
    global value, game_over, wall, n_grid, list_gem, list_grid, score_ingame
    Initial_placement()
    value = 0
    while value < 7:
        while value == 0:
            value = main_menu()
        while value == 1:
            value = dif_menu()
        while value == 2:
            value = score_menu()
        if value == 3:
            n_grid = 7
            game_placement()
            while game_over == 0:
                game_over = game_execution()
            list_gem.clear()
            list_grid.clear()
            list_panel.clear()
            list_text.clear()
            update_screen()
            game_over = 0
            score_ingame = 0
            game_loop()
        if value == 4:
            n_grid = 6
            game_placement()
            while game_over == 0:
                game_over = game_execution()           
            list_gem.clear()
            list_grid.clear()
            list_panel.clear()
            list_text.clear()
            update_screen()
            game_over = 0
            score_ingame = 0
            game_loop()
        if value == 5:
            n_grid = 5
            game_placement()
            while game_over == 0:
                game_over = game_execution()
            list_gem.clear()
            list_grid.clear()
            list_panel.clear()
            list_text.clear()
            update_screen()
            game_over = 0
            score_ingame = 0
            game_loop()
        pass

def create_file_initial():
    if os.path.isfile("scores.dat"):
        return 1
    else:
        f = open("scores.dat", 'x')
        f.close()
    return 1

pygame.init()
screen = pygame.display.set_mode((800, 600))
frame_rate = pygame.time.Clock()
wall = background()

create_file_initial()
game_loop()

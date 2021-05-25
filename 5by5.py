from ctypes import Structure
import os, sys
import random
import pygame
from pygame.locals import *

def arcticSelector():
    num = random.randint(1, 4)
    if num == 1:
        return("Frozen Ocean")
    elif num == 2:
        return("Tundra")
    elif num == 3:
        return("Conifer Forest")
    elif num == 4:
        return("Icy Mountains")

def subArcticSelector():
    num = random.randint(1, 8)
    if num == 1:
        return("Frozen Ocean")
    elif num == 2:
        return("Swamp")
    elif num == 3:
        return("Tundra")
    elif num == 4:
        return("Plains")
    elif num == 5:
        return("Conifer Forest")
    elif num == 6:
        return("Temperate Forest")
    elif num == 7:
        return("Icy Mountains")
    elif num == 8:
        return("Hills")


def temperateSelector():
    num = random.randint(1, 4)
    if num == 1:
        return("Swamp")
    elif num == 2:
        return("Plains")
    elif num == 3:
        return("Temperate Forest")
    elif num == 4:
        return("Hills")

def subTropicalSelector():
    num = random.randint(1, 8)
    if num == 1:
        return("Desert")
    elif num == 2:
        return("Swamp")
    elif num == 3:
        return("Savanna")
    elif num == 4:
        return("Plains")
    elif num == 5:
        return("Jungle")
    elif num == 6:
        return("Temperate Forest")
    elif num == 7:
        return("Tropical Mountains")
    elif num == 8:
        return("Hills")

def tropicalSelector():
    num = random.randint(1, 4)
    if num == 1:
        return("Desert")
    elif num == 2:
        return("Savanna")
    elif num == 3:
        return("Jungle")
    elif num == 4:
        return("Tropical Mountains")

class Screen:
    def __init__ (self, number, biome):
        self.number = number
        self.biome = biome

screen1 = Screen(1, arcticSelector())
screen2 = Screen(2, arcticSelector())
screen3 = Screen(3, arcticSelector())
screen4 = Screen(4, arcticSelector())
screen5 = Screen(5, arcticSelector())
screen6 = Screen(6, subArcticSelector())
screen7 = Screen(7, subArcticSelector())
screen8 = Screen(8, subArcticSelector())
screen9 = Screen(9, subArcticSelector())
screen10 = Screen(10, subArcticSelector())
screen11 = Screen(11, "Plains")
screen12 = Screen(12, temperateSelector())
screen13 = Screen(13, temperateSelector())
screen14 = Screen(14, temperateSelector())
screen15 = Screen(15, temperateSelector())
screen16 = Screen(16, subTropicalSelector())
screen17 = Screen(17, subTropicalSelector())
screen18 = Screen(18, subTropicalSelector())
screen19 = Screen(19, subTropicalSelector())
screen20 = Screen(20, subTropicalSelector())
screen21 = Screen(21, tropicalSelector())
screen22 = Screen(22, tropicalSelector())
screen23 = Screen(23, tropicalSelector())
screen24 = Screen(24, tropicalSelector())
screen25 = Screen(25, tropicalSelector())



current_screen = 11

class template:
    def __init__ (self, x, y, selection):
        self.x = x
        self.y = y
        self.selection = selection
structure = template(400, 200, 1)
mob1 = template(100, 100, 2)
mob2 = template(400, 100, 4)
mob3 = template(700, 100, 1)
mob4 = template(100, 375, 5)
mob5 = template(400, 375, 3)
mob6 = template(700, 375, 4)
resource1 = template(200, 25, 3)
resource2 = template(400, 25, 3)
resource3 = template(600, 25, 3)
resource4 = template(800, 25, 2)
resource5 = template(200, 250, 2)
resource6 = template(400, 250, 2)
resource7 = template(600, 250, 1)
resource8 = template(800, 250, 1)
resource9 = template(200, 400, 1)
resource10 = template(400, 400, 3)
resource11 = template(600, 400, 3)
resource12 = template(800, 400, 3)

def random_horizontal():
    num = random.randint(0, 850)
    return num

def random_vertical():
    num = random.randint(0, 450)
    return num




GRASSGREEN = (0, 255, 0)
FORESTGREEN = (0, 153, 0)
SWAMPGREEN = (51, 102, 0)
STONEGREY = (128, 128, 128)

SANDYYELLOW = (255, 255, 153)
DRYGRASS = (204, 204, 0)
JUNGLEGREEN = (0, 153, 76)
ORANGE = (255, 128, 0)

ICEBLUE = (153, 204, 255)
WHITE = (255, 255, 255)
CONIFERGREEN = (0, 102, 51)
DIRTBROWN = (128, 70, 27)

FPS = 60

player_character_image = pygame.image.load("assets/images/5by5chr.png")
mob1_image = pygame.image.load("assets/images/Sheep.png")
mob2_image = pygame.image.load("assets/images/cow.png")
mob3_image = pygame.image.load("assets/images/horse.png")
resource1_image = pygame.image.load("assets/images/scrub.png")
resource2_image = pygame.image.load("assets/images/quarry.png")
resource3_image = pygame.image.load("assets/images/lake.png")
resource4_image = pygame.image.load("assets/images/carrot.png")
resource5_image = pygame.image.load("assets/images/potato.png")
resource6_image = pygame.image.load("assets/images/wheat.png")



def populate():
    global resource1
    global resource2
    global resource3
    global resource4
    global resource5
    global resource6
    global resource7
    global resource8
    global resource9
    global resource10
    global resource11
    global resource12
    global mob1
    global mob2
    global mob3
    global mob4
    global mob5
    global mob6

    resource1.x = random_horizontal()
    resource1.y = random_vertical()
    resource2.x = random_horizontal()
    resource2.y = random_vertical()
    resource3.x = random_horizontal()
    resource3.y = random_vertical()
    resource4.x = random_horizontal()
    resource4.y = random_vertical()
    resource5.x = random_horizontal()
    resource5.y = random_vertical()
    resource6.x = random_horizontal()
    resource6.y = random_vertical()
    resource7.x = random_horizontal()
    resource7.y = random_vertical()
    resource8.x = random_horizontal()
    resource8.y = random_vertical()
    resource9.x = random_horizontal()
    resource9.y = random_vertical()
    resource10.x = random_horizontal()
    resource10.y = random_vertical()
    resource11.x = random_horizontal()
    resource11.y = random_vertical()
    resource12.x = random_horizontal()
    resource12.y = random_vertical()
    mob1.x = random_horizontal()
    mob1.y = random_vertical()
    mob2.x = random_horizontal()
    mob2.y = random_vertical()
    mob3.x = random_horizontal()
    mob3.y = random_vertical()
    mob4.x = random_horizontal()
    mob4.y = random_vertical()
    mob5.x = random_horizontal()
    mob5.y = random_vertical()
    mob6.x = random_horizontal()
    mob6.y = random_vertical()
    mob1.selection = random.randint(1, 6)
    mob2.selection = random.randint(1, 6)
    mob3.selection = random.randint(1, 6)
    mob4.selection = random.randint(1, 6)
    mob5.selection = random.randint(1, 6)
    mob6.selection = random.randint(1, 6)
    resource1.selection = random.randint(1, 3)
    resource2.selection = random.randint(1, 3)
    resource3.selection = random.randint(1, 3)
    resource4.selection = random.randint(1, 3)
    resource5.selection = random.randint(1, 3)
    resource6.selection = random.randint(1, 3)
    resource7.selection = random.randint(1, 3)
    resource8.selection = random.randint(1, 3)
    resource9.selection = random.randint(1, 3)
    resource10.selection = random.randint(1, 3)
    resource11.selection = random.randint(1, 3)
    resource12.selection = random.randint(1, 3)

    


def plains(WIN):
    if mob1.selection == 1:
        WIN.blit(mob3_image, (mob1.x, mob1.y))
    elif mob1.selection <4:
        WIN.blit(mob2_image, (mob1.x, mob1.y))
    else: 
        WIN.blit(mob1_image, (mob1.x, mob1.y))

    if mob2.selection == 1:
        WIN.blit(mob3_image, (mob2.x, mob2.y))
    elif mob2.selection <4:
        WIN.blit(mob2_image, (mob2.x, mob2.y))
    else: 
        WIN.blit(mob1_image, (mob2.x, mob2.y))

    if mob3.selection == 1:
        WIN.blit(mob3_image, (mob3.x, mob3.y))
    elif mob3.selection <4:
        WIN.blit(mob2_image, (mob3.x, mob3.y))
    else: 
        WIN.blit(mob1_image, (mob3.x, mob3.y))

    if mob4.selection == 1:
        WIN.blit(mob3_image, (mob4.x, mob4.y))
    elif mob4.selection <4:
        WIN.blit(mob2_image, (mob4.x, mob4.y))
    else: 
        WIN.blit(mob1_image, (mob4.x, mob4.y))

    if mob5.selection == 1:
        WIN.blit(mob3_image, (mob5.x, mob5.y))
    elif mob5.selection < 4:
        WIN.blit(mob2_image, (mob5.x, mob5.y))
    else: 
        WIN.blit(mob1_image, (mob5.x, mob5.y))

    if mob6.selection == 1:
        WIN.blit(mob3_image, (mob6.x, mob6.y))
    elif mob6.selection < 4:
        WIN.blit(mob2_image, (mob6.x, mob6.y))
    else: 
        WIN.blit(mob1_image, (mob6.x, mob6.y))

    if resource1.selection == 1:
        WIN.blit(resource4_image, (resource1.x, resource1.y))
    elif resource1.selection == 2:
        WIN.blit(resource5_image, (resource1.x, resource1.y))
    else:
        WIN.blit(resource6_image, (resource1.x, resource1.y))

    if resource2.selection == 1:
        WIN.blit(resource4_image, (resource2.x, resource2.y))
    elif resource2.selection == 2:
        WIN.blit(resource5_image, (resource2.x, resource2.y))
    else:
        WIN.blit(resource6_image, (resource2.x, resource2.y))

    if resource3.selection == 1:
        WIN.blit(resource4_image, (resource3.x, resource3.y))
    elif resource3.selection == 2:
        WIN.blit(resource5_image, (resource3.x, resource3.y))
    else:
        WIN.blit(resource6_image, (resource3.x, resource3.y))

    if resource4.selection == 1:
        WIN.blit(resource4_image, (resource4.x, resource4.y))
    elif resource4.selection == 2:
        WIN.blit(resource5_image, (resource4.x, resource4.y))
    else:
        WIN.blit(resource6_image, (resource4.x, resource4.y))

    if resource5.selection == 1:
        WIN.blit(resource4_image, (resource5.x, resource5.y))
    elif resource5.selection == 2:
        WIN.blit(resource5_image, (resource5.x, resource5.y))
    else:
        WIN.blit(resource6_image, (resource5.x, resource5.y))

    if resource6.selection == 1:
        WIN.blit(resource4_image, (resource6.x, resource6.y))
    elif resource6.selection == 2:
        WIN.blit(resource5_image, (resource6.x, resource6.y))
    else:
        WIN.blit(resource6_image, (resource6.x, resource6.y))

    if resource7.selection == 1:
        WIN.blit(resource4_image, (resource7.x, resource7.y))
    elif resource7.selection == 2:
        WIN.blit(resource5_image, (resource7.x, resource7.y))
    else:
        WIN.blit(resource6_image, (resource7.x, resource7.y))

    if resource8.selection == 1:
        WIN.blit(resource4_image, (resource8.x, resource8.y))
    elif resource8.selection == 2:
        WIN.blit(resource5_image, (resource8.x, resource8.y))
    else:
        WIN.blit(resource6_image, (resource8.x, resource8.y))   

    if resource9.selection == 1:
        WIN.blit(resource4_image, (resource9.x, resource9.y))
    elif resource9.selection == 2:
        WIN.blit(resource5_image, (resource9.x, resource9.y))
    else:
        WIN.blit(resource6_image, (resource9.x, resource9.y))

    if resource10.selection == 1:
        WIN.blit(resource4_image, (resource10.x, resource10.y))
    elif resource10.selection == 2:
        WIN.blit(resource5_image, (resource10.x, resource10.y))
    else:
        WIN.blit(resource6_image, (resource10.x, resource10.y))

    if resource11.selection == 1:
        WIN.blit(resource4_image, (resource11.x, resource11.y))
    elif resource11.selection == 2:
        WIN.blit(resource5_image, (resource11.x, resource11.y))
    else:
        WIN.blit(resource6_image, (resource11.x, resource11.y))

    if resource12.selection == 1:
        WIN.blit(resource4_image, (resource12.x, resource12.y))
    elif resource12.selection == 2:
        WIN.blit(resource5_image, (resource12.x, resource12.y))
    else:
        WIN.blit(resource6_image, (resource12.x, resource12.y))

    if current_screen == 11:
        WIN.blit(resource1_image, (200, 200))
        WIN.blit(resource2_image, (800, 200))


    
def draw_window():
    global current_screen
    if current_screen == screen1.number:
        biome = screen1.biome
    if current_screen == screen2.number:
        biome = screen2.biome
    if current_screen == screen3.number:
        biome = screen3.biome
    if current_screen == screen4.number:
        biome = screen4.biome
    if current_screen == screen5.number:
        biome = screen5.biome
    if current_screen == screen6.number:
        biome = screen6.biome
    if current_screen == screen7.number:
        biome = screen7.biome
    if current_screen == screen8.number:
        biome = screen8.biome
    if current_screen == screen9.number:
        biome = screen9.biome
    if current_screen == screen10.number:
        biome = screen10.biome
    if current_screen == screen11.number:
        biome = screen11.biome
    if current_screen == screen12.number:
        biome = screen12.biome
    if current_screen == screen13.number:
        biome = screen13.biome
    if current_screen == screen14.number:
        biome = screen14.biome
    if current_screen == screen15.number:
        biome = screen15.biome
    if current_screen == screen16.number:
        biome = screen16.biome
    if current_screen == screen17.number:
        biome = screen17.biome
    if current_screen == screen18.number:
        biome = screen18.biome
    if current_screen == screen19.number:
        biome = screen19.biome
    if current_screen == screen20.number:
        biome = screen20.biome
    if current_screen == screen21.number:
        biome = screen21.biome
    if current_screen == screen22.number:
        biome = screen22.biome
    if current_screen == screen23.number:
        biome = screen23.biome
    if current_screen == screen24.number:
        biome = screen24.biome
    if current_screen == screen25.number:
        biome = screen25.biome
    
    
    if biome == "Plains":
        WIN.fill(GRASSGREEN)
        plains(WIN)
    elif biome == "Temperate Forest":
        WIN.fill(FORESTGREEN)
    elif biome == "Hills":
        WIN.fill(DIRTBROWN)
    elif biome == "Swamp":
        WIN.fill(SWAMPGREEN)
    elif biome == "Desert":
        WIN.fill(SANDYYELLOW)
    elif biome == "Savanna":
        WIN.fill(DRYGRASS)
    elif biome == "Jungle":
        WIN.fill(JUNGLEGREEN)
    elif biome == "Tropical Mountains":
        WIN.fill(ORANGE)
    elif biome == "Frozen Ocean":
        WIN.fill(ICEBLUE)
    elif biome == "Tundra":
        WIN.fill(WHITE)
    elif biome == "Conifer Forest":
        WIN.fill(CONIFERGREEN)
    elif biome == "Icy Mountains":
        WIN.fill(STONEGREY)
    
    pygame.display.set_caption(f"5 by 5: {current_screen}: {biome}") 
    return biome

    

def player_handle_movement(player, keys_pressed):
    global current_screen
    if keys_pressed[pygame.K_LEFT] and player.x-1 > 0:
        player.x -= 5
    if keys_pressed[pygame.K_RIGHT] and player.x+1 < 850:
        player.x += 5   
    if keys_pressed[pygame.K_UP] and player.y-1 > 0:
        player.y -= 5
    if keys_pressed[pygame.K_DOWN] and player.y+1 < 450:
        player.y += 5
    
    if current_screen !=1 and current_screen !=6 and current_screen !=11 and current_screen !=16 and current_screen !=21: 
        if keys_pressed[pygame.K_LEFT] and player.x-1 < 0:
            player.x =850
            current_screen -= 1
            populate()
            
    if current_screen !=5 and current_screen !=10 and current_screen !=15 and current_screen !=20 and current_screen !=25: 
        if keys_pressed[pygame.K_RIGHT] and player.x+1 > 850:
            current_screen += 1
            player.x = 0
            populate()
           
    if current_screen > 5: 
        if keys_pressed[pygame.K_UP] and player.y-1 < 0:
            player.y = 450
            current_screen -= 5
            populate()
            
    if current_screen < 21:
        if keys_pressed[pygame.K_DOWN] and player.y+1 > 450:
            player.y = 0
            current_screen += 5
            populate()
            
    




WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5 by 5")

def main():
    player = pygame.Rect(0, 200, 50, 50)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        draw_window()
        player_handle_movement(player, keys_pressed) 
        WIN.blit(player_character_image, (player.x, player.y))
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()

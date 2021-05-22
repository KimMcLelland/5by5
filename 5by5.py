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
structure = ""
mob1 = 2
mob2 = 4
mob3 = 1
mob4 = 5
mob5 = 3
mob6 = 4
resource1 = 3
resource2 = 3
resource3 = 3
resource4 = 2
resource5 = 2
resource6 = 2
resource7 = 1
resource8 = 1
resource9 = 1
resource10 = 3
resource11 = 3
resource12 = 3

def three_equal_items():
    num = random.randint(1, 3)
    return num

def three_unequal_items():
    num = random.randint(1, 5)
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

    resource1 = three_equal_items()
    resource2 = three_equal_items()
    resource3 = three_equal_items()
    resource4 = three_equal_items()
    resource5 = three_equal_items()
    resource6 = three_equal_items()
    resource7 = three_equal_items()
    resource8 = three_equal_items()
    resource9 = three_equal_items()
    resource10 = three_equal_items()
    resource11 = three_equal_items()
    resource12 = three_equal_items()
    mob1 = three_unequal_items()
    mob2 = three_unequal_items()
    mob3 = three_unequal_items()
    mob4 = three_unequal_items()
    mob5 = three_unequal_items()
    mob6 = three_unequal_items()


def plains(WIN):
    if mob1 == 1:
        WIN.blit(mob3_image, (100, 100))
    elif mob1 <4:
        WIN.blit(mob2_image, (100, 100))
    else: 
        WIN.blit(mob1_image, (100, 100))

    if mob2 == 1:
        WIN.blit(mob3_image, (400, 100))
    elif mob2 <4:
        WIN.blit(mob2_image, (400, 100))
    else: 
        WIN.blit(mob1_image, (400, 100))

    if mob3 == 1:
        WIN.blit(mob3_image, (700, 100))
    elif mob3 <4:
        WIN.blit(mob2_image, (700, 100))
    else: 
        WIN.blit(mob1_image, (700, 100))

    if mob4 == 1:
        WIN.blit(mob3_image, (100, 325))
    elif mob4 <4:
        WIN.blit(mob2_image, (100, 325))
    else: 
        WIN.blit(mob1_image, (100, 325))

    if mob5 == 1:
        WIN.blit(mob3_image, (400, 325))
    elif mob5 < 4:
        WIN.blit(mob2_image, (400, 325))
    else: 
        WIN.blit(mob1_image, (400, 325))

    if mob6 == 1:
        WIN.blit(mob3_image, (700, 325))
    elif mob6 < 4:
        WIN.blit(mob2_image, (700, 325))
    else: 
        WIN.blit(mob1_image, (700, 325))

    if resource1 == 1:
        WIN.blit(resource4_image, (200, 25))
    elif resource1 == 2:
        WIN.blit(resource5_image, (200, 25))
    else:
        WIN.blit(resource6_image, (200, 25))

    if resource2 == 1:
        WIN.blit(resource4_image, (400, 25))
    elif resource2 == 2:
        WIN.blit(resource5_image, (400, 25))
    else:
        WIN.blit(resource6_image, (400, 25))

    if resource3 == 1:
        WIN.blit(resource4_image, (600, 25))
    elif resource3 == 2:
        WIN.blit(resource5_image, (600, 25))
    else:
        WIN.blit(resource6_image, (600, 25))

    if resource4 == 1:
        WIN.blit(resource4_image, (800, 25))
    elif resource4 == 2:
        WIN.blit(resource5_image, (800, 25))
    else:
        WIN.blit(resource6_image, (800, 25))

    if resource5 == 1:
        WIN.blit(resource4_image, (200, 250))
    elif resource5 == 2:
        WIN.blit(resource5_image, (200, 250))
    else:
        WIN.blit(resource6_image, (200, 250))

    if resource6 == 1:
        WIN.blit(resource4_image, (400, 250))
    elif resource6 == 2:
        WIN.blit(resource5_image, (400, 250))
    else:
        WIN.blit(resource6_image, (400, 250))

    if resource7 == 1:
        WIN.blit(resource4_image, (600, 250))
    elif resource7 == 2:
        WIN.blit(resource5_image, (600, 250))
    else:
        WIN.blit(resource6_image, (600, 250))

    if resource8 == 1:
        WIN.blit(resource4_image, (800, 250))
    elif resource8 == 2:
        WIN.blit(resource5_image, (800, 250))
    else:
        WIN.blit(resource6_image, (800, 250))   

    if resource9 == 1:
        WIN.blit(resource4_image, (200, 400))
    elif resource9 == 2:
        WIN.blit(resource5_image, (200, 400))
    else:
        WIN.blit(resource6_image, (200, 400))

    if resource10 == 1:
        WIN.blit(resource4_image, (400, 400))
    elif resource10 == 2:
        WIN.blit(resource5_image, (400, 400))
    else:
        WIN.blit(resource6_image, (400, 400))

    if resource11 == 1:
        WIN.blit(resource4_image, (600, 400))
    elif resource11 == 2:
        WIN.blit(resource5_image, (600, 400))
    else:
        WIN.blit(resource6_image, (600, 400))

    if resource12 == 1:
        WIN.blit(resource4_image, (800, 400))
    elif resource12 == 2:
        WIN.blit(resource5_image, (800, 400))
    else:
        WIN.blit(resource6_image, (800, 400))

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

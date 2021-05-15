import random
import pygame

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
LIGHTGREY = (192, 192, 192)

FPS = 60

player_character_image = pygame.image.load("assets/images/5by5chr.png")
mob1_image = pygame.image.load("assets/images/Sheep.png")
mob2_image = pygame.image.load("assets/images/cow.png")
resource1_image = pygame.image.load("assets/images/scrub.png")
resource2_image = pygame.image.load("assets/images/quarry.png")
resource3_image = pygame.image.load("assets/images/lake.png")

def plains():
    cow = pygame.Rect(400, 100, 50, 50)
    sheep = pygame.Rect(700, 400, 50, 50)
    quarry = pygame.Rect(200, 300, 50, 50)
    shrub = pygame.Rect(400, 300, 50, 50)
    lake = pygame.Rect(600, 100, 50, 50)

    def handle_sheep_movement(sheep):
        num = random.randint(1, 4)
        if num == 1 and sheep.x-1: 
            sheep.x -= 2
        if num == 2 and sheep.x+1 < 850: 
            sheep.x += 2
        if num == 3 and sheep.y-1 > 0: 
            sheep.y -= 2
        if num == 4 and sheep.y+1 < 450:
            sheep.y += 2

    def handle_cow_movement(cow):
        num = random.randint(1, 4)
        if num == 1 and cow.x-1: 
            cow.x -= 2
        if num == 2 and cow.x+1 < 850: 
            cow.x += 2
        if num == 3 and cow.y-1 > 0: 
            cow.y -= 2
        if num == 4 and cow.y+1 < 450:
            cow.y += 2

    handle_sheep_movement(sheep)
    handle_cow_movement(cow)
    WIN.blit(mob1_image, (sheep.x, sheep.y))
    WIN.blit(mob2_image, (cow.x, cow.y))
    WIN.blit(resource1_image, (shrub.x, shrub.y))
    WIN.blit(resource2_image, (quarry.x, quarry.y))
    WIN.blit(resource3_image, (lake.x, lake.y))


def draw_window (player):
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
        plains()
    elif biome == "Temperate Forest":
        WIN.fill(FORESTGREEN)
    elif biome == "Hills":
        WIN.fill(STONEGREY)
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
        WIN.fill(LIGHTGREY)

    WIN.blit(player_character_image, (player.x, player.y)) 
    pygame.display.set_caption(f"5 by 5: {current_screen}: {biome}")
    

    

    

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
            draw_window(player)

    if current_screen !=5 and current_screen !=10 and current_screen !=15 and current_screen !=20 and current_screen !=25: 
        if keys_pressed[pygame.K_RIGHT] and player.x+1 > 850:
            current_screen += 1
            player.x = 0
            draw_window(player)

    if current_screen > 5: 
        if keys_pressed[pygame.K_UP] and player.y-1 < 0:
            player.y = 450
            current_screen -= 5
            draw_window(player)

    if current_screen < 21:
        if keys_pressed[pygame.K_DOWN] and player.y+1 > 450:
            player.y = 0
            current_screen += 5
            draw_window(player)
            
    




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
        draw_window(player)
        player_handle_movement(player, keys_pressed) 
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()

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

screen1 = arcticSelector()
screen2 = arcticSelector()
screen3 = arcticSelector()
screen4 = arcticSelector()
screen5 = arcticSelector()

arcticZone = [screen1, screen2, screen3, screen4, screen5]


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

screen6 = subArcticSelector()
screen7 = subArcticSelector()
screen8 = subArcticSelector()
screen9 = subArcticSelector()
screen10 = subArcticSelector()

subArcticZone = [screen6, screen7, screen8, screen9, screen10]


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

screen11 = "Plains"
screen12 = temperateSelector()
screen13 = temperateSelector()
screen14 = temperateSelector()
screen15 = temperateSelector()

temperateZone = [screen11, screen12, screen13, screen14, screen15]


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

screen16 = subTropicalSelector()
screen17 = subTropicalSelector()
screen18 = subTropicalSelector()
screen19 = subTropicalSelector()
screen20 = subTropicalSelector()

subTropicalZone = [screen16, screen17, screen18, screen19, screen20]


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

screen21 = tropicalSelector()
screen22 = tropicalSelector()
screen23 = tropicalSelector()
screen24 = tropicalSelector()
screen25 = tropicalSelector()

tropicalZone = [screen21, screen22, screen23, screen24, screen25]

current_screen = screen11

GREEN = (124, 252, 0)

FPS = 60

player_character_image = pygame.image.load("assets/images/5by5chr.png")
mob1_image = pygame.image.load("assets/images/Sheep.png")
mob2_image = pygame.image.load("assets/images/cow.png")
resource1_image = pygame.image.load("assets/images/scrub.png")
resource2_image = pygame.image.load("assets/images/quarry.png")
resource3_image = pygame.image.load("assets/images/lake.png")

def draw_window(player, sheep, cow, quarry, shrub, lake):
    if current_screen == "Plains":
        WIN.fill((GREEN))
        WIN.blit(mob1_image, (sheep.x, sheep.y))
        WIN.blit(mob2_image, (cow.x, cow.y))
        WIN.blit(resource1_image, (shrub.x, shrub.y))
        WIN.blit(resource2_image, (quarry.x, quarry.y))
        WIN.blit(resource3_image, (lake.x, lake.y))
    WIN.blit(player_character_image, (player.x, player.y)) 
    
    pygame.display.update()

def player_handle_movement(player, keys_pressed):
    if keys_pressed[pygame.K_LEFT] and player.x-1 > 0:
        player.x -= 5
    if keys_pressed[pygame.K_RIGHT] and player.x+1 < 850:
        player.x += 5
    if keys_pressed[pygame.K_UP] and player.y-1 > 0:
        player.y -= 5
    if keys_pressed[pygame.K_DOWN] and player.y+1 < 450:
        player.y += 5

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



WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5 by 5")
def main():
    player = pygame.Rect(0, 200, 50, 50)
    cow = pygame.Rect(400, 100, 50, 50)
    sheep = pygame.Rect(700, 400, 50, 50)
    quarry = pygame.Rect(200, 300, 50, 50)
    shrub = pygame.Rect(400, 300, 50, 50)
    lake = pygame.Rect(600, 100, 50, 50)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(player, keys_pressed)
        handle_sheep_movement(sheep)
        handle_cow_movement(cow)
        draw_window(player, sheep, cow, quarry, shrub, lake)

    pygame.quit()

if __name__ == "__main__":
    main()

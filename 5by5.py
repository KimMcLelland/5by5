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

GREEN = (124, 252, 0)

FPS = 60

player_character_image = pygame.image.load("assets/images/5by5chr.png")

def draw_window(player):
    WIN.fill((GREEN))
    WIN.blit(player_character_image, (player.x, player.y)) 
    pygame.display.update()


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
        if keys_pressed[pygame.K_LEFT]:
            player.x -= 5
        if keys_pressed[pygame.K_RIGHT]:
            player.x += 5
        if keys_pressed[pygame.K_UP]:
            player.y -= 5
        if keys_pressed[pygame.K_DOWN]:
            player.y += 5
        draw_window(player)

    pygame.quit()

if __name__ == "__main__":
    main()

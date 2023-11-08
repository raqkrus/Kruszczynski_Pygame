import pygame

pygame.init()

#define window dimentions

screen_width = 800
screen_height = 600

#create pygame screen surface

screen = pygame.display.set_mode((screen_width, screen_height))

#set title of window
pygame.display.set_caption("Pygame Background")

#set image to background
background_image = pygame.image.load("images/tilebackground.jpg")

#scale background to window size
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

#create loop to continuously run background
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False


    #blit background image onto scree
    screen.blit(background_image, (0,0))

    pygame.display.update()
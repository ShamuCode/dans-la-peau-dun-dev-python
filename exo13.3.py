import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))  # Dimensions de la fenêtre
pygame.display.set_caption("Ma fenêtre Pygame")  # Titre de la fenêtre

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

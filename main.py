import pygame
pygame.init()

Widht = 720
Height = 480
tilesize = 35
FPS = 60

window = pygame.display.set_mode((Widht, Height))
clock = pygame.time.Clock()

world = [[1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1,1,1]]

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    window.fill('black')
    for row in range(len(world)):
        for col in range(len(world[row])):
            x = col * tilesize
            y = row * tilesize

            if world[row][col] == 1:
                pygame.draw.rect(window, 'green', (x, y, tilesize, tilesize))

            pygame.draw.rect(window, 'gray10', (x, y, tilesize, tilesize), 1)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
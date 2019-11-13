import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('My window title')

clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
carImg = pygame.transform.scale(carImg, (100, 100))
carImg_rotated = pygame.transform.rotate(carImg, 45)

done = False
i=0
while not done:
    carImg_rotated = pygame.transform.rotate(carImg, i)
    i+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done  = True
        
    x,y = pygame.mouse.get_pos()
        
    gameDisplay.fill((255,255,255))
    gameDisplay.blit(carImg_rotated, (x,y))
        
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()

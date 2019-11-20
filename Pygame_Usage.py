import pygame

pygame.init()
background = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()


class color:
	black = (0, 0, 0)
	white = (255,255,255)
	red = (255,0,0)
	greed = (0,255,0)
	blue = (0,0,255)
	def new(r,g,b):
		return (r,g,b) #possibly the most useless function

class image:
	img1 = pygame.image.load('img.jpg')
	img1 = pygame.transform.rotate(img1, 90)
	img1 = pygame.transform.scale(img1, (50, 50))

def draw(img, position):
	background.blit(img, position)

def mouse_pos():
		return pygame.mouse.get_pos()

pygame.display.set_caption('Hello World!')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	background.fill(color.white)

	draw(image.img1, mouse_pos())
	pygame.display.update()
	clock.tick(60)

import pygame

pygame.init()
background = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()

def getKeys():
	pressed_keys = pygame.key.get_pressed()
	#119: W
	#97:  A
	#115: S
	#100: D
	#32:  space
	return [pressed_keys[119],pressed_keys[97],pressed_keys[115],pressed_keys[100],pressed_keys[32]]

class color:
	black = (0, 0, 0)
	white = (255,255,255)
	red = (255,0,0)
	greed = (0,255,0)
	blue = (0,0,255)
	def new(r,g,b):
		return (r,g,b) #possibly the most useless function

partpos = [0,0]
partvel = [0,0]
partacc = [0,0.1]

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

	partpos = [partpos[0] + partvel[0], partpos[1] + partvel[1]]
	partvel = [partvel[0] + partacc[0], partvel[1] + partacc[1]]
	partacc[0] = (getKeys()[3]-getKeys()[1])/2
	partvel[0]/=1.1
	if partvel[0] > 5:
		partvel[0] = 5
	if partvel[0] < -5:
		partvel[0] = -5
	#hit the ground
	if partpos[1] >= 500-50:
		partpos[1] = 500-50
		partvel[1] = 0
		#jump
		if getKeys()[-1]:
			partvel[1] -= 5
	#hit a wall
	if not(0 <= partpos[0] <= 800-50):
		partvel[0] = 0
		partacc[0] = 0
		if partpos[0] > 0:
			partpos[0] = 800-50
		else:
			partpos[0] = 0


	draw(image.img1, partpos)
	pygame.display.update()
	clock.tick(60)

import pygame
import os

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game !")

WHITE = (255,255,255)

FPS = 60
VEL = 5


SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load(
	os.path.join('Assets', 'spaceship_yellow.png')), 90)


YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))


RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load(
	os.path.join('Assets', 'spaceship_red.png')), 270)
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))

def draw_window(red, yellow):
	WIN.fill(WHITE)
	WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
	WIN.blit(RED_SPACESHIP, (red.x, red.y))
	pygame.display.update()




def main():
	red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)



	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw_window(red, yellow)
		
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_q]:
			yellow.x -= VEL

		if keys_pressed[pygame.K_d]:
			yellow.x += VEL

		if keys_pressed[pygame.K_z]:
			yellow.y -= VEL 

		if keys_pressed[pygame.K_s]:
			yellow.y += VEL

	pygame.QUIT()

if __name__ == "__main__":
	main()
import pygame
import os

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game !")

WHITE = (255,255,255)

FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load(
	os.path.join('Assets', 'spaceship_yellow.png')), 90)


YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55,40))


RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load(
	os.path.join('Assets', 'spaceship_red.png')), 270)
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (55,40))

def draw_window():
	WIN.fill(WHITE)
	WIN.blit(YELLOW_SPACESHIP, (300,100))
	WIN.blit(RED_SPACESHIP, (100,300))
	pygame.display.update()




def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw_window()

	pygame.QUIT()

if __name__ == "__main__":
	main()
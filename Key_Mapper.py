# William Edward Hahn
# August 2021
import pygame
import numpy as np


pygame.init()
font = pygame.font.SysFont('futura', 30)

clock = pygame.time.Clock()
fps = 60

screen_width = 100
screen_height = 100

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('William Hahn\'s Key Mapper')

def keys():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	return np.where(pygame.key.get_pressed())[0]

def mouse():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	return (pygame.mouse.get_pos(), np.where(pygame.mouse.get_pressed())[0])


run = True
while run:

	clock.tick(fps)


	print(keys())

	print(mouse())


	pygame.display.update()

pygame.quit()

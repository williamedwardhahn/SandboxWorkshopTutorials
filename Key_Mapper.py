# William Edward Hahn
# August 2021
import pygame as pg
import numpy as np

pg.init()
font = pg.font.SysFont('futura', 30)

clock = pg.time.Clock()
fps = 60

screen_width = 100
screen_height = 100

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('William Hahn\'s Key Mapper')

def keys():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
	return np.where(pg.key.get_pressed())[0]

def mouse():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
	return (pg.mouse.get_pos(), np.where(pg.mouse.get_pressed())[0])


run = True
while run:

	clock.tick(fps)

	print(keys())

	print(mouse())

	pg.display.update()

pg.quit()

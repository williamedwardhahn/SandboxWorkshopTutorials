import pygame
import numpy as np
from skimage import io as io
import matplotlib.pyplot as plt
from skimage.util import view_as_blocks

def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x, cmap = 'gray')
    ax.axis('off')
    fig.set_size_inches(18, 10)
    plt.show()

def flipimg(x):
    x = np.fliplr(x)
    x = np.rot90(x,k=1,axes=(0,1))
    return x

background    = io.imread("https://github.com/williamedwardhahn/SandboxWorkshopTutorials/raw/main/Space%20Background(2).png")[:,:,:3]
planet_frames = io.imread("https://github.com/williamedwardhahn/SandboxWorkshopTutorials/raw/main/Planet.png")
planet_frames = view_as_blocks(planet_frames, block_shape=(100,100,4))

background = pygame.surfarray.make_surface(background)
planet     = [pygame.surfarray.make_surface(flipimg(planet_frames[0,i,0,:,:,:3])) for i in range(planet_frames.shape[1])]


pygame.init()

screen_width  = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('William Hahn\'s Digital Universe')

clock = pygame.time.Clock()
fps = 60

run = True
while run:

    for i in range(500):

        screen.fill((0,0,0))

        screen.blit(background, ( 0, 0 ))

        screen.blit(planet[(i//5)%50], ( 400, 400 ))

        clock.tick(fps)
        pygame.display.update()

    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		run = False

pygame.quit()

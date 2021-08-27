# William Edward Hahn
# August 2021
import pygame
import numpy as np
from skimage import io as io
import os
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

def draw_bg():
	screen.fill((0,0,0))
	screen.blit(background_s, (0,0))

def get_google_slide(url):
    url_head = "https://docs.google.com/presentation/d/"
    url_body = url.split('/')[5]
    page_id = url.split('.')[-1]
    return url_head + url_body + "/export/png?id=" + url_body + "&pageid=" + page_id

url1 = "https://docs.google.com/presentation/d/1evbdOf5w0Rv71DS-rWxjA5t1Z9lPIsfNFCePSfJ_UCE/edit#slide=id.p"

url1 = get_google_slide(url1)

background = io.imread(url1)[:,:,:3]

background_s  = pygame.surfarray.make_surface(background)

icons1 = io.imread("https://img.itch.zone/aW1nLzE4ODY2MTEucG5n/original/wkYIuw.png")
i,j = 598,591
s = 40
icon_agent = icons1[i-s//2:i+s//2+1,j-s//2:j+s//2+1,:3]


x = 0
y = 0


#################################################
up = 82
down = 81
left = 80
right = 79

def keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # return np.where(pygame.key.get_pressed())[0]
    return np.array(pygame.key.get_pressed())
###################################################

pygame.init()
font = pygame.font.SysFont('futura', 30)

clock = pygame.time.Clock()
fps = 60

screen_width = background.shape[1]
screen_height = background.shape[0]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('William Hahn\'s Digital Universe')

agent_image = pygame.surfarray.make_surface(flipimg(icon_agent)).convert()
agent_image.set_colorkey(agent_image.get_at((0,0)))

speed = 10

run = True
while run:

    clock.tick(fps)

    draw_bg()

    screen.blit(agent_image, (x,y))

    k = keys()

    y -= speed*k[up]
    y += speed*k[down]
    x -= speed*k[left]
    x += speed*k[right]

    pygame.display.update()

pygame.quit()

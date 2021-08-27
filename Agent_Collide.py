# William Edward Hahn
# August 2021
import numpy as np
from skimage import io as io
import os
import matplotlib.pyplot as plt
from skimage.util import view_as_blocks
import pygame as pg

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

def get_google_slide(url):
    url_head = "https://docs.google.com/presentation/d/"
    url_body = url.split('/')[5]
    page_id = url.split('.')[-1]
    return url_head + url_body + "/export/png?id=" + url_body + "&pageid=" + page_id

def blit_array(b,xy):
    screen.blit(pg.surfarray.make_surface(b*1.0),(xy[0],xy[1]))


url1 = "https://docs.google.com/presentation/d/1evbdOf5w0Rv71DS-rWxjA5t1Z9lPIsfNFCePSfJ_UCE/edit#slide=id.p"

url1 = get_google_slide(url1)

background = io.imread(url1)[:,:,:3]

background_s  = pg.surfarray.make_surface(background)

url1 = "https://img.itch.zone/aW1nLzE4ODY2MTEucG5n/original/wkYIuw.png"
url1 = "https://upload.wikimedia.org/wikipedia/commons/b/bc/IKB_191.jpg"
icons1 = io.imread(url1)

i,j = 600,591
h,w = 40,40
icon_agent = icons1[i-h//2:i+h//2+1,j-w//2:j+w//2+1,:3]

mask  = np.mean(background,2)
mask -= mask[0,0]
mask = (mask > 0)
# mask = (mask + 1) % 2


x = 160
y = 160

#################################################
up = 82
down = 81
left = 80
right = 79

def keys():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    return np.array(pg.key.get_pressed())
###################################################

pg.init()
font = pg.font.SysFont('futura', 30)

clock = pg.time.Clock()
fps = 60

screen_width = background.shape[1]
screen_height = background.shape[0]

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('William Hahn\'s Digital Universe')

agent_image = pg.surfarray.make_surface(flipimg(icon_agent)).convert()
agent_image.set_colorkey(agent_image.get_at((0,0)))

speed = 5

run = 1
while run:

    clock.tick(fps)

    screen.fill((0,0,0))
    screen.blit(background_s, (0,0))
    screen.blit(agent_image, (x,y))


    blit_array(mask[x:x+w,y:y+h],(0,0))

    k = keys()

    y -= speed*k[up]
    y += speed*k[down]
    x -= speed*k[left]
    x += speed*k[right]


    print(np.prod(mask[x:x+w,y:y+h]))



    pg.display.update()

pg.quit()

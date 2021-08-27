import os
os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
from DeepZoo import *

image = io.imread("https://opengameart.org/sites/default/files/chicken_walk.png")[:,:,:3]

plot(image)

up    = 0
left  = 1
down  = 2
right = 3

avatars = cut_sprites(image, (32,32,3))

init()
screen = setup(1000,1000)

run = True
while run:

    for i in range(100):

        clear(screen)

        screen.blit(avatars[right][(i//3)%4], ( 400 + i*5, 400 ))

        tick()
        update()

quit()

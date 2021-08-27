import os
os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
from DeepZoo import *


background = io.imread("https://github.com/williamedwardhahn/SandboxWorkshopTutorials/raw/main/Space%20Background(2).png")[:,:,:3]
background = load(background)

planet_frames = io.imread("https://github.com/williamedwardhahn/SandboxWorkshopTutorials/raw/main/Planet.png")
planet = cut_sprites(planet_frames,(100,100,4))[0]


init()
screen = setup(1000,1000)

run = True
while run:

    for i in range(500):

        screen.fill((0,0,0))

        screen.blit(background, ( 0, 0 ))

        screen.blit(planet[(i//5)%50], ( 400, 400 ))

        tick()
        update()

quit()

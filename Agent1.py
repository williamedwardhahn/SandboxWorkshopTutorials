# William Edward Hahn
# August 2021
import os
os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
from DeepZoo import *


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


###################################################

init()

screen = setup(background.shape[0],background.shape[1])

agent_image = load(flipimg(icon_agent)).convert()
agent_image.set_colorkey(agent_image.get_at((0,0)))

speed = 10

run = True
while run:

    tick()

    screen.fill((0,0,0))

    screen.blit(background_s, (0,0))

    screen.blit(agent_image, (x,y))

    k = keys_vector()

    y -= speed*k[up]
    y += speed*k[down]
    x -= speed*k[left]
    x += speed*k[right]


    update()

quit()

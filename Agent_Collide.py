# William Edward Hahn
# August 2021
import os
os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
from DeepZoo import *


url1 = "https://docs.google.com/presentation/d/1evbdOf5w0Rv71DS-rWxjA5t1Z9lPIsfNFCePSfJ_UCE/edit#slide=id.p"

url1 = get_google_slide(url1)

background = io.imread(url1)[:,:,:3]

background_s  = load(background)

# url1 = "https://img.itch.zone/aW1nLzE4ODY2MTEucG5n/original/wkYIuw.png"
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

init()

screen = setup(background.shape[0],background.shape[1])

agent_image = load(flipimg(icon_agent)).convert()
agent_image.set_colorkey(agent_image.get_at((0,0)))

speed = 5

run = 1
while run:

    tick()

    screen.fill((0,0,0))
    screen.blit(background_s, (0,0))
    screen.blit(agent_image, (x,y))


    blit_array(screen,mask[x:x+w,y:y+h],(0,0))

    k = keys_vector()

    y -= speed*k[up]
    y += speed*k[down]
    x -= speed*k[left]
    x += speed*k[right]


    collision = mask[x:x+w,y:y+h]
    collision = np.sum(collision==1) / len(collision.flatten())
    print(collision)
    # run *= collision


    update()

quit()

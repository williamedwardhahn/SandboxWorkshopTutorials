import os
os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
from DeepZoo import *

init()

display = setup(256,256)

while True:

    img = 256*np.random.random((256,256,3))

    draw(display, img)

quit()

# William Edward Hahn
# August 2021
import os
os.system("pip install --ignore-installed  git+https://github.com/williamedwardhahn/DeepZoo")
from DeepZoo import *

init()

display = setup(256,256)

run = True
while run:

	tick()

	print(keys())

	print(mouse())

quit()

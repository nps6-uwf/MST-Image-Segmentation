
# All code based on: Implementation of Efficient Graph Based Image Segmentation
# Paper url: http://cs.brown.edu/people/pfelzens/papers/seg-ijcv.pdf
# Paper Author:  Pedro F. Felzenszwalb
#   
# Implementation: Nick Sebasco
# Date: 10/16/2021

# Created Modules
from utils import color_text
from segment_image import segment
# 3rd Party/ STL Modules
import numpy as np
from sys import argv, exit
from PIL import Image

# (1) arguments temporarily defined as variables:
# c++ arguments: ./segment 0.7 1000 80 'testImages/twoSquares.ppm' twoSquares
if len(argv) < 2:
    print("Error: Missing arguments.") 
    print("Please append the following arguments:",color_text('input file path','magenta'))
    exit()

sigma = float(argv[2]) if len(argv) > 2 else 0.5 
k = int(argv[3]) if len(argv) > 3 else 1000
minSize = int(argv[4]) if len(argv) > 4 else 80
ifile = argv[1]
ofile = argv[5] if len(argv) > 5 else "segmented.png"

# (2) load ifile as an image
# Use PIL
img = Image.open(ifile)
width, height = img.size
M = np.asarray(img)
print(M.shape)

newImg, numCcs = segment(M, sigma, k, minSize)
Image.fromarray(newImg).save(ofile)
print(f"Segment complete, found: {numCcs} segments.")
print(f"output file: {ofile} saved.")

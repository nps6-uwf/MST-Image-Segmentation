
# All code based on: Implementation of Efficient Graph Based Image Segmentation
# Paper url: http://cs.brown.edu/people/pfelzens/papers/seg-ijcv.pdf
# Paper Author:  Pedro F. Felzenszwalb
#   
# Implementation: Nick Sebasco
# Date: 10/20/2021
#
# Version: 2
# Updates:
# 1. Timing segmentation
# 2. Added countingEdgeSort + manhattan distance

# Created Modules
from utils import color_text
from segment_image import segment
# 3rd Party/ STL Modules
import numpy as np
from sys import argv, exit
from PIL import Image
from time import time

# (1) arguments temporarily defined as variables:
# c++ arguments: ./segment 0.7 1000 80 'testImages/twoSquares.ppm' twoSquares
if len(argv) < 2:
    print("Error: Missing arguments.") 
    print("Please append the following arguments:",color_text('input file path','magenta'))
    exit()
# 0.5, K = 500, min = 50
sigma = float(argv[2]) if len(argv) > 2 else 0.5
k = int(argv[3]) if len(argv) > 3 else 500
minSize = int(argv[4]) if len(argv) > 4 else 50
ifile = argv[1]
ofile = argv[5] if len(argv) > 5 else "segmented.png"
dist = "manhattan" # changing this value to anything other than "manhattan" -> disimilarity metric = euclidean.

# (2) load ifile as an image
# Option 1) Using Keras preproccessing
# Issue, I need a target_size
#from keras_preprocessing import image
#train_image = image.load_img(path, target_size = (height, width)) 
#train_image = image.img_to_array(train_image)

# Option 2) Use PIL
img = Image.open(ifile)
width, height = img.size
print(img)
M = np.asarray(img)
print(M)
print(M.shape)

t0 = time()
newImg, numCcs = segment(M, sigma, k, minSize, dist=dist)
Image.fromarray(newImg).save(ofile)
tf = time()
print(f"Segment complete, found: {numCcs} segments.  Elapsed time: {tf-t0}s")
print(f"output file: {color_text(ofile,'green')} saved.")
# Graph Based Image Segmentation

Pure python implementation of <i>Implementation of Efficient Graph Based Image Segmentation</i>, by
Pedro F. Felzenszwalb.  The full paper from which the code was created can be found here: <a href="http://cs.brown.edu/people/pfelzens/papers/seg-ijcv.pdf">Paper</a>.

## Dependencies

Python 3
PIL
Numpy
Scipy

installation:
pip3 install pillow numpy scipy

## Arguments
### Required

ifile: input file path

### Optional

sigma: [default] 0.5 - Parameter used by gaussian blurring preproccessing.
k: [defualt] 1000 - Value for the threshold function.
minSize: [defualt] 80 - Minimum component size enforced by post-processing.
ofile: [default] 'segmented.png' - Name of the output file.

### Usage

(1) only specifying ifile:
python main.py 'testImages/xSqrOv.png'

(2) specifying all optionals
python main.py 'testImages/xSqrOv.png' 0.7 900 50 'seg_xSqrOv.png'




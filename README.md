# Graph Based Image Segmentation

<table>
  <tbody>
    <tr>
      <td><img src="https://github.com/nps6-uwf/Efficient-Graph-Based-Image-Segmentation/blob/main/testImages/ghostshell.png?raw=true"></img></td>
      <td><img src="https://github.com/nps6-uwf/Efficient-Graph-Based-Image-Segmentation/blob/main/results/seg_ghostshell.png?raw=true"></img></td>
    </tr>
  </tbody>
</table>

Pure python implementation of <i>Implementation of Efficient Graph Based Image Segmentation</i>, by
Pedro F. Felzenszwalb.  The full paper from which the code was created can be found here: <a href="http://cs.brown.edu/people/pfelzens/papers/seg-ijcv.pdf">Paper</a>.  Pseudocode explaining how one can use the disjoint set data structure to improve Kruskal's algorithm for computing the MST, <a href="http://www.csl.mtu.edu/cs4321/www/Lectures/Lecture%2019%20-%20Kruskal%20Algorithm%20and%20Dis-joint%20Sets.htm">Kruskal's Algorithm and Disjoint Sets<a>

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




import numpy as np

np.seterr(over='ignore')

# convolve image with gaussian filter
def smooth(src, sigma):
    mask = make_fgauss(sigma)
    mask = normalize(mask)
    tmp = convolve_even(src, mask)
    dst = convolve_even(tmp, mask)
    return dst


# gaussian filter
def make_fgauss(sigma, width = 4.0):
    sigma = max(sigma, 0.01)
    length = int(np.ceil(sigma * width)) + 1
    mask = np.zeros(shape=length, dtype=float)
    for i in range(length):
        mask[i] = np.exp(-0.5 * np.power(i / sigma, i / sigma))
    return mask


# normalize mask so it integrates to one
def normalize(mask):
    sum = 2 * np.sum(np.absolute(mask)) + abs(mask[0])
    return np.divide(mask, sum)


# convolve src with mask.  output is flipped!
def convolve_even(src, mask):
    output = np.zeros(shape=src.shape, dtype=float)
    height, width,c = src.shape
    length = len(mask)

    for y in range(height):
        for x in range(width):
            sum = float(mask[0] * src[y, x])
            for i in range(1, length):
                sum += mask[i] * (src[y, max(x - i, 0)] + src[y, min(x + i, width - 1)])
            output[y, x] = sum
    return output
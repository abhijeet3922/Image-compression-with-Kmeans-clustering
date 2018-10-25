# -*- coding: utf-8 -*-

from skimage import io
import numpy as np

centers = np.load('codebook_tiger.npy')
c_image = io.imread('compressed_tiger.png')
image = centers[c_image]

io.imsave('reconstructed_tiger.png',image);
io.imshow(image)
io.show()

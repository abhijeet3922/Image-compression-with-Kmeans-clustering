# -*- coding: utf-8 -*-

from skimage import io
import numpy as np

centers = np.load('codebook_tiger.npy')

c_image = io.imread('compressed_tiger.png')

image = np.zeros((c_image.shape[0],c_image.shape[1],3),dtype=np.uint8 )
for i in range(c_image.shape[0]):
    for j in range(c_image.shape[1]):
            image[i,j,:] = centers[c_image[i,j],:]
    
io.imsave('reconstructed_tiger.png',image);
io.imshow(image)
io.show()

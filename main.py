import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import numpy as np
import cv2
from Elastic import elastic


o_img = cv2.imread('/home/mlpasujong/바탕화면/train-volume.tif')
elMat = elastic(o_img, alpha=3000, sigma=20, random_state=None)

cv2.namedWindow('origin',0)
cv2.imshow('origin', o_img)
cv2.namedWindow('elastic',0)
cv2.imshow('elastic', elMat)

cv2.waitKey(0)
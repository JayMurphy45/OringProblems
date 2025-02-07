import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def threshold(img, thresh):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img[y, x] > thresh:
                img[y, x] = 255
            else:
                img[y, x] = 0

def hist(img):
    h = np.zeros(256)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            h[img[y, x]] += 1
    return h

def find_thresh(hist):
    t = 100  # Placeholder for actual threshold finding logic
    return t

# read a image 
i = 1
process = True
while process:
    index = i % 16
    if index != 0:
        print(index)
        img = cv.imread('Orings/Oring'+str(index)+'.jpg', cv.IMREAD_GRAYSCALE)
        h = hist(img)
        plt.plot(h)
        plt.show()
        thresh = find_thresh(h)
        threshold(img, thresh)
        cv.imshow('Oring'+str(index), img)
        k = cv.waitKey(0)
        if k == ord('q'): # press 'q' to quit
            process = False
    i += 1
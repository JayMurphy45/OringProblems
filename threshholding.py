import numpy as np

# finds peak of histogram
def find_thresh(hist):
    t = 0
    for i in range(len(hist)):  
        if hist[i] > hist[t]:
            t = i  
    return t - 50

# after findinsh thresh apply to image by setting pixel to 0 or 255
def threshold(img, thresh):
    for y in range(img.shape[0]):  
        for x in range(img.shape[1]):  
            if img[y, x] > thresh:
                img[y, x] = 0 
            else:
                img[y, x] = 255
    return img 

# generate histogram
def hist(img):
    h = np.zeros(256)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            h[img[y, x]] += 1  
    return h

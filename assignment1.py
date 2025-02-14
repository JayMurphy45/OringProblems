import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Define a structuring element (3x3 square)
structuring_element = np.ones((3, 3), dtype=np.uint8)

# Dilate image
def dilate(img, square):
    rows, cols = img.shape
    matrix = square.shape[0]  
    pad = matrix // 2  
    output = img.copy()

    # loop through image
    for i in range(pad, rows - pad):
        for j in range(pad, cols - pad):
            # if any pixel in square is 1 then set pixel to 255
            if np.any(img[i - pad:i + pad + 1, j - pad:j + pad + 1] & square):
                output[i, j] = 255  

    return output

# Erode image
def erode(img, square):
    rows, cols = img.shape
    matrix = square.shape[0]
    pad = matrix // 2
    output = img.copy()

    # lopop through image
    for i in range(pad, rows - pad):
        for j in range(pad, cols - pad):
            # if all pixels in square are 1 then set pixel to 255
            if np.all(img[i - pad:i + pad + 1, j - pad:j + pad + 1] & square):
                output[i, j] = 255
            # else set pixel to 0 
            else:
                output[i, j] = 0  

    return output

# Closing operation
def closing(img, square):
    dilated = dilate(img, square)
    closed = erode(dilated, square)
    return closed

# generate histogram
def hist(img):
    h = np.zeros(256)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            h[img[y, x]] += 1  
    return h

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

# loading images
i = 1
process = True
while process:
    index = i % 16
    if index != 0:
        print("Processing image:", index)
        img = cv.imread(f'Orings/Oring{index}.jpg', cv.IMREAD_GRAYSCALE)

        h = hist(img)
        # plt.plot(h)
        # plt.show()

        cv.imshow(f'Original O-ring', img)

        thresh = find_thresh(h)
        binary_img = threshold(img, thresh) 
        closed_img = closing(binary_img, structuring_element) 
        cv.imshow(f'Threshholded O-ring ', binary_img)
        cv.imshow(f'Closed O-ring ', closed_img)  
        k = cv.waitKey(0)
        if k == ord('q'):  
            process = False

    i += 1  

cv.destroyAllWindows()


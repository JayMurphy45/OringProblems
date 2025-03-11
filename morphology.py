import numpy as np

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

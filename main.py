import time
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from threshholding import find_thresh, threshold, hist
from morphology import closing
from connected_components import connected_components
from isValid import is_valid_oring, invert

# Define a structuring element (3x3 square)
structuring_element = np.ones((3, 3), dtype=np.uint8)
# loading images
i = 1
process = True
while process:
    before = time.time()
    index = i % 16
    if index != 0:
        print("Processing image:", index)
        img = cv.imread(f'Orings/Oring{index}.jpg', cv.IMREAD_GRAYSCALE)
        img_color = cv.imread(f'Orings/Oring{index}.jpg', cv.IMREAD_COLOR)

        h = hist(img)
        # plt.plot(h)
        # plt.show()

        cv.imshow(f'Original O-ring', img)

        thresh = find_thresh(h)
        binary_img = threshold(img, thresh) 
        closed_img = closing(binary_img, structuring_element)
        labels =connected_components(closed_img)
        cv.imshow(f'Threshholded O-ring ', binary_img)
        cv.imshow(f'Closed O-ring ', closed_img)
        cv.imshow(f'Connected Components O-ring ', labels * 100)

        inverted_img = invert(closed_img)
        labels = connected_components(inverted_img)
        cv.imshow(f'Inverted O-ring ', inverted_img)

        after = time.time()

        print("Time taken: ", after - before)

        colourGreen = (0, 255, 0)
        colourRed = (0, 0, 255)
        colourBlue = (255, 0, 0)

        if is_valid_oring(labels):
            print('pass')
            cv.putText(img_color, 'pass', (10, 20), cv.FONT_ITALIC, 1, colourGreen, 3)
            
        else:
            print('fail')
            cv.putText(img_color, 'Fail', (10, 20), cv.FONT_ITALIC, 1, colourRed, 3)
        cv.putText(img_color, 'time: ' + str(round(after - before, 2)), (10, 60), cv.FONT_ITALIC, 1, colourBlue, 3)
        cv.imshow(f'annotaded O-ring ', img_color)    
        # cv.imshow(f'Connected Components O-ring ', image_labels)
        k = cv.waitKey(0)
        if k == ord('q'):  
            process = False

    i += 1  

cv.destroyAllWindows()


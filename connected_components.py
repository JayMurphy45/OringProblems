import numpy as np

def connected_components(img):
    pad_img = np.pad(img, 1)
    queue = []
    labels = np.zeros((pad_img.shape[0], pad_img.shape[1]), dtype=np.uint8)
    currLabel = 1

    # loop through image
    for y in range(1, pad_img.shape[0] - 1):
        for x in range(1, pad_img.shape[1] - 1):
            if pad_img[y, x] == 255 and labels[y, x] == 0:
                labels[y, x] = currLabel
                queue.append((y,x))
                while len(queue) > 0:
                    y,x = queue.pop()
                    # check neighbours and add to queue if they are 255 and not already labelled
                    if(pad_img[y-1,x] == 255 and labels[y-1,x] == 0):
                        labels[y-1,x] = currLabel
                        queue.append((y-1,x))
                    if(pad_img[y+1,x] == 255 and labels[y+1,x] == 0):
                        labels[y+1,x] = currLabel
                        queue.append((y+1,x))
                    if(pad_img[y,x-1] == 255 and labels[y,x-1] == 0):
                        labels[y,x-1] = currLabel
                        queue.append((y,x-1))
                    if(pad_img[y,x+1] == 255 and labels[y,x+1] == 0):
                        labels[y,x+1] = currLabel
                        queue.append((y,x+1))
                    
                currLabel += 1
                 
    return labels
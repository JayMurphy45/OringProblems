import numpy as np

# using connected components to check validation of oring
def is_valid_oring(labels):
    unique_labels = np.unique(labels)  
    num_labels = len(unique_labels) 
    
    if num_labels == 3:  
        return True  
    return False  

def invert(img):
    return 255 - img

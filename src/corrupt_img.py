import cv2
import numpy as np
import os


#-----------------------------------------------------------
# SET DIRECTORY PATHS AND IMAGE/MASK SIZES HERE

img_directory = './Desktop/test/source'
mask_directory = './Desktop/test/masks'

train_dest_directory = './Desktop/test/corrupt train'
test_dest_directory = './Desktop/test/corrupt test'
dim = (512, 512)
training_size = 27000
#-----------------------------------------------------------

count = 0
# Iterate over training images
for filename in os.listdir(img_directory):
    
    img_path = os.path.join(img_directory, filename)
    mask_path = os.path.join(mask_directory, filename)
    
    img = cv2.imread(img_path)
    mask = cv2.imread(mask_path, 0)

    img = cv2.resize(img, dim)
    mask = cv2.resize(mask, dim)
        
    # Apply the mask to the original image
    corrupted_img = cv2.bitwise_and(img, img, mask=mask)

    if count <training_size:
    # Save the corrupted image as a new file
        dest_name = os.path.join(train_dest_directory, filename)
    else:
        dest_name = os.path.join(test_dest_directory, filename)
    cv2.imwrite(dest_name, corrupted_img)
    count+=1


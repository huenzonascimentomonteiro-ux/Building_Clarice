import cv2 as cv
from help_functions import get_contours

# Classify the contour size;

for contour in get_contours("figure_1.png"):
    area = cv.contourArea(contour)
    
    if area <= 4000:
        contour_size = "Small"
    elif area <= 10000:
        contour_size = "Medium"
    else:
        contour_size = "Really Great"
    
    print(contour_size)
    


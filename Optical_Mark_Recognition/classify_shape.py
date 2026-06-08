import cv2 as cv
from help_functions import get_contour

contour = get_contour("shape_1.png", 0)

vertices = cv.approxPolyDP(
    contour,
    2,
    True
)

if len(vertices) == 4:
    print("Square")
elif len(vertices) == 3:
    print("Triangle")
else:
    print("Circle")



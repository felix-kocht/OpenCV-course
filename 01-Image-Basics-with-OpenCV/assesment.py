# TASK: (NOTE: YOU WILL NEED TO RUN THIS AS A SCRIPT). Create a script that opens the picture and allows you to draw empty red circles whever you click the RIGHT MOUSE BUTTON DOWN.
import cv2
import numpy as np  
import matplotlib.pyplot as plt
# Create a function based on a CV2 Event (Left button  DOUBLE click)


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), 10)


# Create a black image
img = cv2.imread('DATA/dog_backpack.jpg')
# This names the window so we can reference it
cv2.namedWindow(winname='my_drawing')
# Connects the mouse button to our callback function
cv2.setMouseCallback('my_drawing', draw_circle)

while True:  # Runs forever until we break with Esc key on keyboard
    # Shows the image window
    cv2.imshow('my_drawing', img)
    # EXPLANATION FOR THIS LINE OF CODE:
    if cv2.waitKey(20) & 0xFF == 27:
        break
# Once script is done, its usually good practice to call this line
# It closes all windows (just in case you have multiple windows called)
cv2.destroyAllWindows()

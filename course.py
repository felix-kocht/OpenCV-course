import cv2
import matplotlib.pyplot as plt

# reading in 'Computer-Vision-with-Python/DATA/00-puppy.jpg' with cv2  and displaying in extra window until esc is pressed
image = cv2.imread('DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy Image', image)
    if cv2.waitKey(1) & 0xFF == 27:
        print("esc pressed")
        break
cv2.destroyAllWindows()


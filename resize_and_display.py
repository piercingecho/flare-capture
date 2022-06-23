import cv2

def resize_and_display(image, multiplier):
    width = int(image.shape[1] * multiplier)
    height = int(image.shape[0] * multiplier)

    resized = cv2.resize(image, (width, height))
    cv2.imshow("Shapes", resized)

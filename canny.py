import cv2
import matplotlib.pyplot as plot
image=cv2.imread('red_rose.jpg', cv2.IMREAD_GRAYSCALE)
low=int(input("Please give the lower threshold value: "))
high=int(input("Please give the higher threshold value: "))
canny_img=cv2.Canny(image, low, high)
plot.imshow(canny_img, cmap='gray')
plot.show()

import cv2
import matplotlib.pyplot as plot
image=cv2.imread('red_rose.jpg', cv2.IMREAD_GRAYSCALE)
sobelx=cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
plot.imshow(sobelx, cmap='gray')
plot.show()
sobely=cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
plot.imshow(sobely, cmap='gray')
plot.show()
combined_sobel=cv2.bitwise_or(cv2.convertScaleAbs(sobelx), cv2.convertScaleAbs(sobely))
plot.imshow(combined_sobel, cmap='gray')
plot.show()
import cv2
import matplotlib.pyplot as plot
image=cv2.imread('red_rose.jpg', cv2.IMREAD_GRAYSCALE)
laplacian=cv2.Laplacian(image, cv2.CV_64F)
laplacian_final=cv2.convertScaleAbs(laplacian)
plot.imshow(laplacian_final, cmap='gray')
plot.show()
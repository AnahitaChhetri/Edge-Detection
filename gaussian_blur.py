import cv2
import matplotlib.pyplot as plot
image=cv2.imread('red_rose.jpg', cv2.IMREAD_GRAYSCALE)
kernel_size=int(input("Enter the Gaussian Blur kernel size. Make sure it's an odd number: "))
blur=cv2.GaussianBlur(image, (kernel_size,kernel_size), 0)
plot.imshow(blur, cmap='gray')
plot.title("Gaussian Blur")
plot.show()
import cv2
import matplotlib.pyplot as plot

image=cv2.imread("red_rose.jpg", cv2.IMREAD_GRAYSCALE)

def normal_image():
    plot.imshow(image)
    plot.title("Unfiltered Image")
    plot.show()

def laplacian():
    lplcn=cv2.Laplacian(image, cv2.CV_64F)
    final_lplcn=cv2.convertScaleAbs(lplcn)
    plot.imshow(final_lplcn, cmap="gray")
    plot.title("Laplacian")
    plot.show()
def sobel():
    sobelx=cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely=cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobelxy=cv2.bitwise_or(cv2.convertScaleAbs(sobelx), cv2.convertScaleAbs(sobely))
    plot.imshow(sobelxy, cmap="gray")
    plot.title("Sobel")
    plot.show()

def canny():
    lower_threshold=int(input("What is the lower threshold value?:"))
    higher_threshold=int(input("What is the higher threshold value?:"))
    canny=cv2.Canny(image, lower_threshold, higher_threshold)
    plot.imshow(canny, cmap="gray")
    plot.title("Canny")
    plot.show()

def gaussian_blur():
    kernel_size=int(input("Enter an odd number for the kernel size.: "))
    if kernel_size%2==0:
        kernel_size+=1
    gaussian_blur=cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    plot.imshow(gaussian_blur, cmap="gray")
    plot.title("Gaussian Blur")
    plot.show()

print("Welcome to the image filteration toolkit! First, the original image will be shown, and then the filtered image!:")
def image_showing():
    filter_choice=input("Press 1 for Canny, 2 for Sobel, 3 for Laplacian, 4 for Gaussian Blur, and 5 for a comparison of all the filters: ")

    if filter_choice=="1":
        normal_image()
        canny()
    elif filter_choice=="2":
        normal_image()
        sobel()
    elif filter_choice=="3":
        normal_image()
        laplacian()
    elif filter_choice=="4":
        normal_image()
        gaussian_blur()
    else:
        normal_image()
        canny()
        sobel()
        laplacian()
        gaussian_blur()
x=True
while x:
    image_showing()
    go_again_question_mark=input("Do you want to look at more filters? Press 1 for yes, and 9 for no: ")
    if go_again_question_mark=="1":
        x=True
    else:
        x=False
        print("Thank you for using the image filteration tool!")




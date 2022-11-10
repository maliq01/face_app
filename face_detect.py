import cv2
#importing the trained library and attaching it to a variable.
trained_face_data = cv2.CascadeClassifier('haarcascade_fronatalface_defult.xml')

#importing the image which we will detect the face.
img = cv2.imread("pic.png")
#turning the image to grayscale for the computer to read it well.
grayscaled_img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)






cv2.imshow("developed face detector", grayscaled_img)
cv2.waitKey()

print("code successful")

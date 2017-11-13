from imutils import paths
import argparse
import dlib
import cv2
import os

path = os.getcwd() + os.sep 
path_test = path + "../db_aulas/Imagens/minibases/data_101/data_101/car_side_test"

# load the detector
detector = dlib.simple_object_detector('car_sign.svm')

# loop over the testing images
for testingPath in paths.list_images(path_test):
	# load the image and make predictions
	image = cv2.imread(testingPath)
	boxes = detector(image)

	# loop over the bounding boxes and draw them
	for b in boxes:
		(x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
		cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
		print("(%d,%d),(%d,%d)"%(x,y,w,h))
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)

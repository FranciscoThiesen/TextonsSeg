from TextonsSeg.texton_color_utils import Textons
import cv2
'''
The goal of this test suite is to come up with a reasonable way to measure the performance
of the Texton based Segmentation against Human ground-truth segmentation.

Having such information helps us validate changes to the code, like:
1 - Usage of other distances (Minkowskim, etc)
2 - Changes to the K-Means algorithm.
	2.1 - Adding some rule based stop condition.
	2.2 - Tuning for finding the optimal number of centroids,
	.
	.
3 - Test whether the position of each pixel should really be added to the image
'''

def calculate_score(img_path, ground_truth_path):
	'''
	I am assuming that the ground truth version of the imge is following the .seg
	format, used at https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/
	In such format .seg, each line of the image is of the form
	(s, r, c1, c2) stating that every column in the [c1, c2] range on the r-th row
	belongs to the segment with index s
	'''
	img = cv2.imread(img_path)
	tex = Textons(img, 5, 5, 1)
	img = tex.textons()

	cv2.imshow('test_img', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.waitKey(1)


# calculate_score('BSDS300/images/test/3096.jpg', 'BSDS300/images/test/3096.jpg')
img_path = input()
ground_truth_path = input()
calculate_score(img_path, ground_truth_path)
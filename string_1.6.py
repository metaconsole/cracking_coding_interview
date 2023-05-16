# 1 6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees Can you do this in place?

# 5x5
# (1,0) <- (0,3) <- (3,4) <- (4,1) <- (1,0)
# (0,3)  - (3,4) - (4,1) - (1,0)
# assumption: each pixel is tuple of len 4
# n * n * 4 
import numpy as np

class Stack:
	def __init__(self):
		self.top = None
	
	def push(self, d):
		new_top = Node(d, )

def rotate_img(img):
	n = len(img[0])
	print(n)
	cut = n//2 + n%2
	print(cut)
	for i in range(n -1):
		for k in range(i, n - i -1):
			print(i, k)
			img_0 = img[i][k]
			img[i][k] = img[k][n -1 - i]
			img[k][n -1 - i] = img[n -1 -i][n -1 - k]
			img[n -1 -i][n -1 - k] = img[n- 1 -k][i]
			img[n - 1 -k][i] = img_0
	return(img)

img = [[1, 2], [3,4]]
img_large = [[i + k for k in range(5)] for i in range(0, 21, 5)]
img_debug = [[(x, y) for y in range(5)] for x in range(5)]

print(img_debug)
print(rotate_img(img_debug))
print(np.array(img_large))
print(np.array(rotate_img(img_large)))
print(img)
print([2, 4, 3, 1])
print(rotate_img(img))



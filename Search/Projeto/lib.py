import os
import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
from scipy.stats import chisquare

def compute_descriptors(img):
		surf = cv.xfeatures2d.SURF_create()
		kp, des = surf.detectAndCompute(img, None)
		return des

def get_path(dirs, max_items=5):
		paths = []
		PATH = './101_ObjectCategories/'
		for _dir in dirs:
			if(_dir[0] == '.'):
					continue
			actual_path = PATH + _dir + '/'
			images_list = sorted(os.listdir(actual_path))
			for i in range(max_items):
					img = cv.imread(actual_path + images_list[i])
					paths.append(actual_path + images_list[i])
		return paths

def read_descriptors(dirs, max_items=5):
		paths = []
		list_descriptors = []
		PATH = './101_ObjectCategories/'
		for _dir in dirs:
				if(_dir[0] == '.'):
						continue
				actual_path = PATH + _dir + '/'
				images_list = sorted(os.listdir(actual_path))
				for i in range(max_items):
						img = cv.imread(actual_path + images_list[i])
						paths.append(actual_path + images_list[i])
						descriptors = compute_descriptors(img)
						list_descriptors.append(descriptors)
		return np.vstack(list_descriptors), paths


def create_vocabulary(descriptors, sz=300):
		k = KMeans(sz, random_state=0)
		k.fit(descriptors)
		return (k.cluster_centers_, k)


def histogram(img, vocab):
		img = cv.imread(img)
		d = compute_descriptors(img)
		h = vocab[1].predict(d)
		ret = [1 for i in range(len(vocab[0]))]
		for i in range(len(h)):
				ret[h[i]] +=1
#     plt.hist(h)
#     plt.show()
#     print(ret)
		return ret

def chi_squared(hist1, hist2):
		s = 0 
		for a, b in zip(hist1, hist2):
				s += ((a - b) ** 2)/a
		# check if nan
		if(s != s):
				return 0
		return s * 0.5

# def chi_squared(hist1, hist2):
# 		print(chisquare(hist1, f_exp=hist2))
# 		return chisquare(hist1, f_exp=hist2)

def show_5(dist_list, original):
		plt.imshow(cv.imread(original))
		plt.show()
		for i in range(5):
				print(f"Distance: {dist_list[i][0]}")
				plt.imshow(cv.imread(dist_list[i][1]))
				plt.show()
				
def search(PATH, vocab, hist_list, paths):
		hist = histogram(PATH, vocab)
		dist_list = [((chi_squared(hist_list[i], hist)), paths[i]) for i in range(len(hist_list))]
		sorted_list = sorted(dist_list, key=lambda x: x[0])
		return sorted_list
		# show_5(sorted_list, PATH)
		
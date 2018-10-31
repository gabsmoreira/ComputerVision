"""1. Predict with pre-trained SSD models
==========================================

This article shows how to play with pre-trained SSD models with only a few
lines of code.

First let's import some necessary libraries:
"""

from gluoncv import model_zoo, data, utils
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import os
import pickle

net = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)

# im_fname = utils.download('https://github.com/dmlc/web-data/blob/master/' +
#                           'gluoncv/detection/street_small.jpg?raw=true',
#                           path='street_small.jpg')

list_images_processed = []
directories = os.listdir('./dataset-projeto-3-2')
for dirs in directories:
  print(dirs)
  if(dirs != '.DS_Store'):
    paths = './dataset-projeto-3-2' + '/' + dirs
    user_imgs = os.listdir(paths)
    for imgs in user_imgs:
      image_processed = []
      image_path = paths + '/' + imgs
      # print(paths+ '/' + imgs)
      image_processed.append(image_path)
      x, img = data.transforms.presets.ssd.load_test(image_path, short=512)
      class_IDs, scores, bounding_boxs = net(x)
      image_processed.append(class_IDs)
      image_processed.append(scores)
      image_processed.append(bounding_boxs)
      list_images_processed.append(image_processed)

pickle_out = open("./files/processed.pickle","wb")
pickle.dump(list_images_processed, pickle_out)    
# print('Shape of pre-processed image:', x.shape)

# PATH = './imgs/cachorro.jpg'
# print(class_IDs[0])
# print(net.classes)

# ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],
#                          class_IDs[0], class_names=net.classes)
# plt.show()

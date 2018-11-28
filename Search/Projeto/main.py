import pickle
from lib import *
import sys 

DATASET = ["Faces", "garfield", "platypus", "nautilus", "elephant", "gerenuk"]

print(len(paths))

pickle_in = open("vocab.pickle","rb")
vocab = pickle.load(pickle_in)

pickle_in = open("paths.pickle","rb")
paths = pickle.load(pickle_in)

pickle_in = open("hist.pickle","rb")
hist_list = pickle.load(pickle_in)

# PATH = './101_ObjectCategories/rhino/image_0001.jpg'
path = sys.argv[1]
s_list = search(path, vocab, hist_list, paths)

for i in range(5):
  print(f"""
Distance: {s_list[i][0]}
Imagem: {s_list[i][1]}                  
-------------------------------- """)
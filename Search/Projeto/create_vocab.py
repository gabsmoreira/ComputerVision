import pickle
from lib import *

DATASET = ["Faces", "garfield", "platypus", "nautilus", "elephant", "gerenuk"]
# DATASET = os.listdir('./101_ObjectCategories/')
MAX_ITEMS = 10
des, paths = read_descriptors(DATASET, MAX_ITEMS)
vocab = create_vocabulary(des)
pickle_out = open("vocab.pickle","wb")
pickle.dump(vocab, pickle_out)
pickle_out.close()

pickle_out = open("paths.pickle","wb")
pickle.dump(paths, pickle_out)
pickle_out.close()

hist_list = [histogram(paths[i], vocab) for i in range (len(DATASET) * MAX_ITEMS)]
pickle_out = open("hist.pickle","wb")
pickle.dump(hist_list, pickle_out)
pickle_out.close()
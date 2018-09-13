import cv2 as cv
import numpy as np

captura = cv.VideoCapture(0)

# Para não deixar encavalar os frames
captura.set(cv.CAP_PROP_BUFFERSIZE, 1)
lk_params = dict( winSize  = (15,15),
				  maxLevel = 2,
				  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Parametriza a funcao do OpenCV
dt_params = dict( maxCorners = 100,
				  qualityLevel = 0.3,
				  minDistance = 7,
				  blockSize = 7 )

# Gera cores de forma aleatória
color = np.random.randint(0,255,(100,3))

first = True
ret, frame = captura.read()
previous = frame
previous_gray = cv.cvtColor(previous, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(previous_gray, mask = None, **dt_params)
mask = np.zeros_like(previous)
rows, cols, r = frame.shape
maX = 0
maY = 0

while(1):
	ret, frame = captura.read()
	actual = frame
	actual_gray = cv.cvtColor(actual, cv.COLOR_BGR2GRAY)
	p1, st, err = cv.calcOpticalFlowPyrLK(previous_gray, actual_gray, p0, None, **lk_params)
	good_new = p1[st==1]
	good_old = p0[st==1]
	for i,(new, old) in enumerate(zip(good_new, good_old)):
		a,b = new.ravel()
		c,d = old.ravel()
		# mask = cv.line(mask, (a,b),(c,d), [0,0,255], 2)
		actual = cv.circle(actual,(a,b),5,color[i].tolist(),-1)
	
	img = cv.add(actual, mask)
	l = len(good_new)
	mX = 0
	mY = 0
	for j in range (l):
		mX += good_old[0][0] - good_new[0][0]
		mY += good_old[0][1] - good_new[0][1]
	mX/= l
	mY/= l
	maX += mX
	maY += mX
	# print('X: {0}'.format(mX))
	# print('Y: {0}'.format(mY))
	
	# M = cv.getRotationMatrix2D((mX + cols/2, mX + cols/2), 0, 1)
	M = np.array([[1, 0, maY], [0, 1, maX]], dtype=np.float32)
	dst = cv.warpAffine(img, M, (cols, rows))
	cv.imshow("Video", dst)
	# cv.imshow("Video", mask)
	previous_gray = actual_gray.copy()
	p0 = good_new.reshape(-1,1,2)
	# Pressione ESC para sair do loop
	k = cv.waitKey(30) & 0xff
	if k == 27:
		break

captura.release()
cv.destroyAllWindows()


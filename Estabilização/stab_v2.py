import cv2 as cv
import numpy as np
import math

captura = cv.VideoCapture(0)

# Para nao deixar encavalar os frames
captura.set(cv.CAP_PROP_BUFFERSIZE, 1)

ret, frame = captura.read()
rows, cols, r = frame.shape
x1, x2 = 200, rows-200
# x1, x2 = rows//3, 2*rows//3
y1, y2 = 500, cols - 500

print(rows, cols)
# previous = frame[100:rows-100, cols//3:2*cols//3]
previous = frame[x1:x2, y1:y2]
previous_gray = cv.cvtColor(previous, cv.COLOR_BGR2GRAY)
maX = 0
maY = 0
center = (cols // 2, rows // 2)
cX = 0
cY = 0
nx1 = 0
nx2 = 0
ny1 = 0
ny2 = 0
while(1):
	ret, frame = captura.read()
	actual = frame
	actual = actual[int(x1):int(x2), int(y1):int(y2)]
	actual_gray = cv.cvtColor(actual, cv.COLOR_BGR2GRAY)
	flow = cv.calcOpticalFlowFarneback(previous_gray, actual_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	mX = np.mean(flow[:,:,0])
	mY = np.mean(flow[:,:,1])
	maX += mX
	maY += mY
	x1 += mY
	x2 += mY
	y1 += mX
	y2 += mX
	M = np.array([[1, 0, -maX], [0, 1, -maY]], dtype=np.float32)
	dst = cv.warpAffine(frame, M, (cols, rows))
	x1 = min(720, max(0, x1))
	x2 = min(720, max(0, x2))
	y1 = min(1280, max(0, y1))
	y2 = min(1280, max(0, y2))

	yl = int(rows - np.abs(maY))
	xl = int(cols - np.abs(maX))

	cv.rectangle(dst,(int(y1),int(x2)), (int(y2),int(x1)), (0,0,255), 3)

	

	if(maY > 0):
		cy2 = int(rows - maY)
		cy1 = 0
		#cortar em baixo
	else:
		cy1 = int(-maY)
		cy2 = rows
		# cortar em cima	
	if (maX > 0):
		cx2 = int(cols - maX)
		cx1 = 0
		# cortar na direita
	else:
		cx1 = int(-maX)
		cx2 = cols
		#cortar na esquerda
	# print(cx1, cx2)
	
	if(16/9 > xl/yl):
		cY = ((-9/16) * xl) + yl
	
	else:
		cX = ((-16/9) * yl) + xl
	
	print(cx1, cy1, cx2, cy2)
	

	dst = dst[cy1:cy2 - int(cY), cx1:cx2 - int(cX)]
	dst = cv.resize(dst, (cols, rows), fx=1, fy=1) 
	cv.imshow("Video", dst)
	previous_gray = actual_gray.copy()
	k = cv.waitKey(30) & 0xff
	if k == 27:
		break

captura.release()		
cv.destroyAllWindows()

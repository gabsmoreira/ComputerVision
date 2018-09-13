import cv2 as cv
import numpy as np
import math

captura = cv.VideoCapture(0)

# Para nao deixar encavalar os frames
captura.set(cv.CAP_PROP_BUFFERSIZE, 1)

ret, frame = captura.read()
rows, cols, r = frame.shape
#cols -> x
#rows -> y
y1, y2 = int(0.34 * rows), rows - int(0.34 * rows)
# y1, y2 = 200, rows - 200
x1, x2 = int(0.42 * cols), cols - int(0.42 * cols)
# x1, x2 = 480, cols - 480

print(rows, cols)
previous = frame[y1:y2, x1:x2]
previous_gray = cv.cvtColor(previous, cv.COLOR_BGR2GRAY)

maX = 0
maY = 0

while(1):
	ret, frame = captura.read()
	actual = frame
	actual = actual[int(y1):int(y2), int(x1):int(x2)]
	actual_gray = cv.cvtColor(actual, cv.COLOR_BGR2GRAY)
	flow = cv.calcOpticalFlowFarneback(previous_gray, actual_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	fx = np.mean(flow[:,:,0])
	fy = np.mean(flow[:,:,1])
	maX += fx
	maY += fy
	y1 = min(rows, max(0, y1 + fy))
	y2 = min(rows, max(0, y2 + fy))
	x1 = min(cols, max(0, x1 + fx))
	x2 = min(cols, max(0, x2 + fx))
	M = np.array([[1, 0, -maX], [0, 1, -maY]], dtype=np.float32)
	dst = cv.warpAffine(frame, M, (cols, rows))

	yl = rows - np.abs(int(maY))
	xl = cols - np.abs(int(maX))

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

	cY = 0
	cX = 0
	
	if(16/9 > xl/yl):
		cY = ((-9/16) * xl) + yl
	
	else:
		cX = ((-16/9) * yl) + xl
	# print(cX, cY)
	print((cx2-cx1 - int(cX)) / (cy2-cy1 - int(cY)))
	
	dst = dst[cy1:cy2 - int(cY), cx1:cx2 - int(cX)]

	# M2 = np.float32([[1,0,cx1],[0,1,cy1]])
	# dst = cv.warpAffine(dst , M2, (cols,rows))
	cv.rectangle(dst,(int(x1),int(y1)), (int(x2),int(y2)), (0,0,255), 3)
	dst = cv.resize(dst, (cols, rows), interpolation = cv.INTER_CUBIC) 
	# print((cx2-cx1) / (cy2-cy1))
	cv.imshow("Video", dst)
	previous_gray = actual_gray.copy()
	k = cv.waitKey(30) & 0xff
	if k == 27:
			break

captura.release()		
cv.destroyAllWindows()


# cs = (dx**2+dy**2)**0.5 cs = cs/100 s = 1 + cs 
# res = cv2.resize(img_rect, None, fx=s, fy=s, interpolation=cv2.INTER_LINEAR)


# c = sqr[4] newx = int(c[0]*s) newy = int(c[1]*s) 
# res = res[newy - 360 : newy + 360, newx - 640 : newx + 640]
import cv2

img = cv2.imread('sistema solar.jpg')

mercurio = "Mercurio"
venus = "Venus"
terra = "Terra"
marte = "Marte"
jupiter = "Jupiter"
saturno = "Saturno"
urano = "Urano"
netuno = "Netuno"

cv2.putText(img, mercurio, (340,300), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (192,192,192))
cv2.putText(img, venus, (540,110), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (70,130,180))
cv2.putText(img, terra, (320,530), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (160,82,45))
cv2.putText(img, marte, (720,350), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (0,0,128))
cv2.putText(img, jupiter, (620,650), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (0,69,255))
cv2.putText(img, saturno, (1100,250), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (122,160,255))
cv2.putText(img, saturno, (1020,650), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (255,160,122))
cv2.putText(img, netuno, (1270,550), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (255,69,0))

cv2.imshow("sistema solar", img)

cv2.waitKey(0)
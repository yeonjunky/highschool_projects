from PIL import Image
import pytesseract
import argparse
import cv2
import numpy as np
import os

lang = 'kor1'
OemConfig = r'--oem 1, --psm 7'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = cv2.imread("image\\sample10-1.jpg", 0)

sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
dst = cv2.filter2D(image, -1, sharpening)

blur = cv2.GaussianBlur(dst, (3, 3), 0)

ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((1, 1), np.uint8)
mor = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, th)

text = pytesseract.image_to_string(Image.open(filename), lang = lang)
os.remove(filename)

print(text)
cv2.imshow('ori', image)
cv2.imshow('test', mor)
cv2.waitKey(0)
cv2.destroyAllWindows()







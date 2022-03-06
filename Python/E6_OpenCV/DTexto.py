import argparse
import pytesseract
from PIL import Image

tesseract.pytesseract.tesseract_cmd = r'"C:\Program Files\Tesseract-OCR\tesseract.exe"'
#C:\Program Files\Tesseract-OCR
T_imagen = Image.open('C:\\Users\\walte\Desktop\\Python 2022\\Python\\E6_OpenCV\\img4.jpg')
txt = tesseract.image_to_string(T_imagen)
print(txt)   


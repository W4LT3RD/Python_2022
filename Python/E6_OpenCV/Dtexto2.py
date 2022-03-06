import pytesseract
import sys
from pdf2image import convert_from_path
import os

filename='img3.png'
outfile='extraccion.txt'

text=str(((pytesseract.image_to_string(Imagee.open(filename)))))
text=text.remplace('-\n','')
f.write(text)
f.close()
print("Terminado")
from PIL import image
from pytesseract import *

pytesseract.pytesseract.tesseract_cmd = r'"C:\Program Files\Tesseract-OCR\tesseract.exe"'

img = Image.open("imgen.png")

resultado = pytesseract.image_to_string(img)
print(resultado)

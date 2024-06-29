import cv2
from pytesseract import *
import requests
import json

def obtener_producto(codigo_barras):
    url = f'https://world.openfoodfacts.org/api/v3/product/{codigo_barras}.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.content)
        brands = data['product']['brands']
        print(f'brand: {brands}')
        pass
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(r"images\\boleta_2_code.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

text = pytesseract.image_to_string(threshold_img)

lineas = text.splitlines()

for linea in lineas:
    codigos = linea.strip()  
    print(codigos)
    try:
        codigos = int(codigos)
        obtener_producto(codigos)
        print(f"{codigos} es un entero válido.")
    except ValueError:
        print(f"{codigos} no se puede convertir a entero.")



    



import requests
import json

def obtener_producto(codigo_barras):
    # URL de la API con el código de barras
    url = f'https://world.openfoodfacts.org/api/v3/product/{codigo_barras}.json'
    
    try:
        # Hacer la petición GET a la API
        response = requests.get(url)
        # Verificar que la petición fue exitosa
        response.raise_for_status()
        
        # Parsear la respuesta JSON
        # data = response.json()
        data = json.loads(response.content)
        
        brands = data['product']['brands']

        print(brands) 

        return data

    
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

# Usar la función con el código de barras proporcionado
codigo_barras = '7802225640770'
producto = obtener_producto(codigo_barras)
# print(producto)
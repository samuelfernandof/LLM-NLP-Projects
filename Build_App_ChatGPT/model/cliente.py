# Lab 2 - Cliente (Frontend)

# Imports
import requests
import json

# URL da app
url = 'http://localhost:5000/predict'

# Dados de entrada (prompt)
data = {'text': 'The advantages of artificial intelligence are'}

# Prepara os dados no formato JSON
headers = {'Content-Type': 'application/json'}

# Faz um request para a app e coleta a resopsta
response = requests.post(url, data = json.dumps(data), headers = headers)

# Imprime no terminal
print("\nTexto Gerado:\n")
print(response.json())
print("\n")

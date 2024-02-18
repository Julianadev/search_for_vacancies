import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')
url = "https://jsearch.p.rapidapi.com/search"

profissao = input('Digite a vaga que você deseja buscar: ')

querystring = {"query": profissao, "page": "1", "num_pages": "1"}

headers = {
    "X-RapidAPI-Key": os.getenv('API_KEY'),
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()
    parametro = data.get('parameters', None)
    print(parametro)
    vagas = data.get('data', None)
    for chave in vagas:
        print(100 * '-')
        for key, valor in chave.items():
            print(f'{key} - {valor}')
else:
    print(f'Erro: {response.status_code}')

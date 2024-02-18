import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')

def get_response(profissao):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": profissao, "page": "1", "num_pages": "2"}
    headers = {
        "X-RapidAPI-Key": os.getenv('API_KEY'),
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    try:
        if response.status_code == 200:
            df = response.json()
            return df
        return None
    except requests.ConnectionError as e:
        print(f'Erro na solicitação da API: {response.status_code}')

def main():
    profissao = input('Digite a vaga que você deseja buscar: ')
    response_content = get_response(profissao)
    try:
        if response_content is not None:
            parametro = response_content.get('parameters', None)
            print(parametro)
            vagas = response_content.get('data', None)
            for chave in vagas:
                print(100 * '-')
                for key, valor in chave.items():
                    print(f'{key} - {valor}')
        return None
    except Exception as e:
        print('Ocorreu um erro: ', e)


if __name__ == "__main__":
    main()


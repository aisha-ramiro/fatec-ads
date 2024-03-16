#CONVERTER CELSIUS PARA FAHRENHEIT

import os 
import requests

with open('.env', 'r') as file:
    lines = file.readlines()
for line in lines:
    key, value = line.strip().split('=')
    os.environ[key] = value


#chamada API de geolocalização para definir as coordenadas da cidade desejada
def localizacao(cidade): 
  chave = os.environ.get('OWM_API_KEY_WEATHER')
  url = f'http://api.openweathermap.org/geo/1.0/direct?q={cidade}&limit=1&appid={chave}'
  resposta = requests.get(url)
  dados = resposta.json()
  if dados:
    coordenadas = dados[0]["lat"], dados[0]["lon"]
    return coordenadas
  else:
    return None

#chamada API de clima para definir a temperatura da cidade desejada, usanddo
# as coordenadas anteriores
def obter_temperatura(coordenadas):
  chave = os.environ.get('OWM_API_KEY_WEATHER')
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordenadas[0]}&lon={coordenadas[1]}&appid={chave}&units=metric"
  resposta = requests.get(url)
  dados = resposta.json()
  temperatura = dados["main"]["temp"]
  return temperatura

#Usuário digita a cidade e a partir dessa entrada faz a chamada da API
# retornando as coordenadas da cidade pesquisada
cidade = input('Digite a cidade: ')
coordenadas = localizacao(cidade)

#Usando as coordenadas anteriores, chama a API para conseguir
#obter a temperatura.
#A temperatura já vem em graus Celsius, sendo convertida
# para fahrenheit usando a formula. Caso não encontre a cidade, retorna erro.
if coordenadas:
    temperatura_celsius = obter_temperatura(coordenadas)
    temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

    print(f'''
          A temperatura atual em {cidade} é: 
          {temperatura_celsius:.2f}°C;
          {temperatura_fahrenheit:.2f}°F.
          ''')
else:
    print("Cidade não encontrada, tente novamente")
import requests
from bs4 import BeautifulSoup
urls = ['https://www.pagina1.com', 'https://www.pagina2.com', 'https://www.pagina3.com']
for url in urls:
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    titulo = soup.find('h1').text
    parrafos = soup.find_all('p')
with open('informacion.txt', 'w') as f:
    f.write(f'Título: {titulo}\n\n')
    for p in parrafos:
        f.write(f'{p.text}\n\n')
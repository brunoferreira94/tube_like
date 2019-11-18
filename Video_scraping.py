import requests
from bs4 import BeautifulSoup

def get_categorias():
    url_home = 'https://pt.pornhub.com'
    url_categorias = 'https://pt.pornhub.com/categories'
    result = requests.get(url_categorias)
    src = result.content
    soup = BeautifulSoup(src,'html.parser')
    categorias = {'nome':[], 'url':[]}

    for tag in soup.find_all('div',id='categoriesStraightImages'):
        if tag == None:
            print('Nada encontrado na tag div')
        else:
            for item in tag.find_all('a', attrs={'data-mxptype':'Category'}):
                if item == None:
                    print('Nada encontrado na tag a')
                else:
                    categorias['url'].append(url_home + item['href'])
                    categorias['nome'].append(item['data-mxptext'])
    return categorias


def get_videos(categorias, url_home):
    videos = {'id':[], 'nome':[], 'url':[], 'miniatura':[], 'orientacao':[]}
    for categoria in categorias:
        result = requests.get(categoria)
        src = result.content
        soup = BeautifulSoup(src,'html.parser')
        for item  in soup.find_all('li',attrs={'class':' js-pop videoblock videoBox'}):
            videos['id'].append(item['_vkey'])
            videos['orientacao'].append(item['data-segment'])
            item_aux = item.find('a', attrs={'class':'linkVideoThumb js-linkVideoThumb img '})
            videos['nome'].append(item_aux['title'])
            videos['url'].append(url_home + item_aux['href'])







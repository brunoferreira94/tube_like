import requests
from selenium import webdriver
from bs4 import BeautifulSoup

url_home = 'https://pt.pornhub.com'
#header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
driver = webdriver.Firefox()

def get_categorias():
    url_categorias = 'https://pt.pornhub.com/categories'
    driver.get(url_categorias)
    src = driver.page_source
    #result = requests.get(url_categorias, headers=header)
    #src = result.content
    soup = BeautifulSoup(src,'html.parser')
    categorias = []    

    for tag in soup.find_all('div',id='categoriesStraightImages'):
        if tag == None or tag == '':
            print('Nada encontrado na tag div')
        else:
            for item in tag.find_all('a', attrs={'data-mxptype':'Category'}):
                if item == None or item == '':
                    print('Nada encontrado na tag a')
                else:
                    categorias.append ({'url':url_home + item['href'], 'nome':item['data-mxptext']})
    return categorias


def get_videos(categorias, url_home):
    #videos = {'id':[], 'nome':[], 'url':[], 'miniatura':[], 'orientacao':[], 'categoria':[]}
    for categoria in categorias:
        cont = 0
        #result = requests.get(categoria['url']+'&page=9999', headers=header)
        #src = result.content
        driver.get(categoria['url']+'&page=9999')
        src = driver.page_source
        soup = BeautifulSoup(src,'html.parser')
        for item in soup.find_all('li',attrs={'class':' js-pop videoblock videoBox'}):
            if item == None:
                print('Nenhum item na tag li')
            item_aux = item.find('a', attrs={'class':'linkVideoThumb js-linkVideoThumb img '})
            '''
            videos['id'].append(item['_vkey'])
            videos['orientacao'].append(item['data-segment'])
            videos['nome'].append(item_aux['title'])
            videos['url'].append(url_home + item_aux['href'])
            videos['categoria'].append(categoria['nome'])
            '''
            cont+=1
            print(item['_vkey']+'|'+item['data-segment']+'|'+item_aux['title']+'|'+url_home + item_aux['href']+'|'+categoria['nome']+'\n')
            with open('/storage/emulated/0/Download/base.csv','a') as arquivo:
                arquivo.write(item['_vkey']+'|'+item['data-segment']+'|'+item_aux['title']+'|'+url_home + item_aux['href']+'|'+categoria['nome']+'\n')


get_videos(get_categorias(), url_home)

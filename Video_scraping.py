import requests
#from selenium import webdriver
from bs4 import BeautifulSoup

url_home = 'https://pt.pornhub.com'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
#driver = webdriver.Firefox()

def get_categorias():
    url_categorias = 'https://pt.pornhub.com/categories'
    #driver.get(url_categorias)
    #src = driver.page_source
    result = requests.get(url_categorias, headers=header)
    src = result.content
    soup = BeautifulSoup(src,'html.parser')
    categorias = []

    for tag in soup.find_all('a',class_='sidebarIndent js-mxp'):
        if tag == None or tag == '':
            print('Nada encontrado na tag li')
        else:
            print(url_home +'|'+ tag['href'] +'|'+ tag['data-mxptext'])
            categorias.append ({'url':url_home + tag['href'], 'nome':tag['data-mxptext']})
    return categorias


def get_videos(categorias, url_home):
    #videos = {'id':[], 'nome':[], 'url':[], 'miniatura':[], 'orientacao':[], 'categoria':[]}
    for categoria in categorias:
        cont = 1
        #print(categoria)
        while(True):
            if '?' in categoria['url']:
                result = requests.get(categoria['url'] + '&page=' + str(cont), headers=header)
            else:
                result = requests.get(categoria['url'] + '?page=' + str(cont), headers=header)
            src = result.content
            #driver.get(categoria['url']+'&page=9999')
            #src = driver.page_source
            soup = BeautifulSoup(src,'html.parser')
            if soup.find('div',class_='noVideosNotice'):
                print('Acabou a categoria ' + categoria['nome'])
                cont=1
                break
            for item in soup.find_all('li',attrs={'class':'js-pop videoblock videoBox'}):
                if item == None or item == '':
                    print('Nenhum item na tag li')
                    break
                item_aux = item.find('a', attrs={'class':'linkVideoThumb js-linkVideoThumb img'})
                if item_aux == None or item_aux == '':
                    print('Nenhum item na tag a')
                    break
                '''
                videos['id'].append(item['_vkey'])
                videos['orientacao'].append(item['data-segment'])
                videos['nome'].append(item_aux['title'])
                videos['url'].append(url_home + item_aux['href'])
                videos['categoria'].append(categoria['nome'])
                '''
                cont+=1
                print(item['_vkey']+'|'+item['data-segment']+'|'+item_aux['title']+'|'+url_home + item_aux['href']+'|'+categoria['nome']+'\n')
                with open('base.csv','a') as arquivo:
                    arquivo.write(item['_vkey']+'|'+item['data-segment']+'|'+item_aux['title']+'|'+url_home + item_aux['href']+'|'+categoria['nome']+'\n')


get_videos(get_categorias(), url_home)

import requests
from bs4 import BeautifulSoup

url_home = 'https://pt.pornhub.com'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

def get_categorias():
    url_categorias = 'https://pt.pornhub.com/categories'
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
    for categoria in categorias:
        cont = 1
        #print(categoria)
        while(True):
            if '?' in categoria['url']:
                result = requests.get(categoria['url'] + '&page=' + str(cont), headers=header)
            else:
                result = requests.get(categoria['url'] + '?page=' + str(cont), headers=header)
            print('Página '+cont+' da categoria '+categoria['url'])
            src = result.content
            soup = BeautifulSoup(src,'html.parser')
            if soup.find('div',class_='noVideosNotice'):
                print('Acabou a categoria ' + categoria['nome'])
                cont=1
                break
            if soup.find('li',attrs={'class':'js-pop videoblock videoBox'}):
                for item in soup.find_all('li',attrs={'class':'js-pop videoblock videoBox'}):
                    item_aux = item.find('a', attrs={'class':'linkVideoThumb js-linkVideoThumb img'})
                    if item_aux == None or item_aux == '':
                        print('Nenhum item na tag a')
                        break
                    cont+=1
                    print(item['_vkey']+'|'+item['data-segment']+'|'+item_aux['title']+'|'+url_home + item_aux['href']+'|'+categoria['nome']+'\n')
                    with open('base.csv','a') as arquivo:
                        arquivo.write(item['_vkey']+'|'+item['data-segment']+'|'+item_aux['title']+'|'+url_home + item_aux['href']+'|'+categoria['nome']+'\n')
            else:
                print('Nenhum item na tag li')
                break

get_videos(get_categorias(), url_home)

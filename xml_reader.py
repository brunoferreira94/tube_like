import xml.etree.ElementTree as et
from collections import defaultdict

tree = et.parse('videos.xml')
root = tree.getroot()
x = 0
videos = {'url':[], 'nome':[], 'miniatura':[]}
    
for item in root:
    if item.tag == 'entry':
        url = item[4].attrib['href']
        nome = item[3].text
        miniatura = item[8][2].attrib['url']
        videos['url'].append(url)
        videos['nome'].append(nome)
        videos['miniatura'].append(miniatura)
        print('nome: {} \nurl: {} \nminiatura: {}'.format(videos['nome'][x], videos['url'][x], videos['miniatura'][x]))
        x=+1

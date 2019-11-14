import xml.etree.ElementTree as et
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from  .models import Video

class listagem(ListView):
    model = Video
    template_name = 'listagem/home.html'

def lista_xml(request):
    tree = et.parse('/storage/emulated/0/Download/arquivo.xml')
    root = tree.getroot()
    x = 0
    videos = [[], [], []]
    
    for item in root:
        if item.tag == 'entry':
            url = item[4].attrib['href']
            nome = item[3].text
            miniatura = item[8][2].attrib['url']
            videos[0].append(url)
            videos[1].append(nome)
            videos[2].append(miniatura)
            print('nome: {} \nurl: {} \nminiatura: {}'.format(videos[1][x], videos[0][x], videos[2][x]))
            x=+1 x=+1
    return(request, 'listagem/home.html', videos)

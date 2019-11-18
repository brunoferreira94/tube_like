import xml.etree.ElementTree as et
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from  .models import Video

class listagem(ListView):
    model = Video
    template_name = 'listagem/home.html'

def lista_xml(request):
    tree = et.parse('videos.xml')
    root = tree.getroot()
    videos = []
    
    for item in root:
        if item.tag == 'entry':
            url = item[4].attrib['href']
            nome = item[3].text
            miniatura = item[8][2].attrib['url']
            videos.append({'url':url, 'nome':nome, 'miniatura':miniatura})
    for item in videos:
        print(item['nome'])
    return render(request, 'listagem/home.html', {'list':videos})

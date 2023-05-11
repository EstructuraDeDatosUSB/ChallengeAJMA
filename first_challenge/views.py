from django.shortcuts import render
from .Graph_ADT import Graph
from .SpecialFunctions1 import *


def dijkstra(request):
    graph = Graph(weighted=True)
    loadGraph(graph)
    context = {}
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        path = graph.dijkstra(start, end)

        context['path'] = path
        context['start'] = start
        context['end'] = end

    image = graph.draw_graph()
    context['image'] = image
    return render(request, 'first_challenge_template/first_challenge_form.html', context)







from django.shortcuts import render
from .Graph_ADT import cities
from .SpecialFunctions1 import *


def firstChallenge(request):
    context = {}
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')

        path = cities.dijkstra(start, end)

        context['path'] = path
        context['start'] = start
        context['end'] = end

    image = cities.draw_graph()
    context['image'] = image
    return render(request, 'first_challenge_template/first_challenge_form.html', context)


def graphCreation(request):
    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        distance = float(request.POST.get('distance'))

        cities.addEdge(start, end, distance)

        context = {
            'start': start,
            'end': end,
        }

        image = cities.draw_graph()
        context['image'] = image

        context['route'] = start + " hacia " + end + " con distancia de " + str(distance) + " km"

        return render(request, 'graph_creation_template/graph_creation_form.html', context)
    else:
        context = {}
        image = cities.draw_graph()
        context['image'] = image
        return render(request, 'graph_creation_template/graph_creation_form.html', context)

def secondChallenge(request):
    context = {}
    if request.method == "POST":
        city = request.POST.get('city')

        all_paths = cities.find_all_paths(city)

        directed_paths, undirected_paths = direct_or_indirect(all_paths)

        context['directRoutes'] = directed_paths
        context['indirectRoutes'] = undirected_paths
        context['city'] = city

    image = cities.draw_graph()
    context['image'] = image
    return render(request, 'second_challenge_template/second_challenge_form.html', context)
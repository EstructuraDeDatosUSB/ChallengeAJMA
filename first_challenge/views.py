from django.shortcuts import render
from .Graph_ADT import cities
from .SpecialFunctions1 import *


def firstChallenge(request):
    """
        Esta función se encarga de renderizar el template del primer reto, que es el de encontrar la ruta más corta
        :param request: The request object
        :return: The render of the first challenge form
    """

    context = {}

    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')

        path, image_dijkstra, dist = cities.dijkstra(start, end)

        context['path'] = path
        context['start'] = start
        context['end'] = end
        context['image_dijkstra'] = image_dijkstra
        context['dist'] = dist

    context['city_list'] = cities.get_vertices()
    image = cities.draw_graph()
    context['image'] = image

    return render(request, 'first_challenge_template/first_challenge_form.html', context)


def graphCreation(request):
    """
            Esta función se encarga de renderizar el template de la creación del grafo, que consiste en agregar
            rutas y sus distancias
            :param request: The request object
            :return: The render of the first challenge form
        """

    context = {}

    if request.method == "POST":
        start = request.POST.get('start')
        end = request.POST.get('end')
        distance = float(request.POST.get('distance'))

        cities.add_edge(start, end, distance)

        context = {
            'start': start,
            'end': end,
        }

        image = cities.draw_graph()
        context['image'] = image

        context['route'] = start + " hacia " + end + " con distancia de " + str(distance) + " km"

    context['city_list'] = cities.get_vertices()
    image = cities.draw_graph()
    context['image'] = image

    return render(request, 'graph_creation_template/graph_creation_form.html', context)


def secondChallenge(request):
    """
    Esta función se encarga de renderizar el template del segundo reto, que es el de encontrar las rutas directas e
    indirectas de un puerto.
    :param request: The request object
    :return: The render of the second challenge form
    """

    context = {}

    if request.method == "POST":
        city = request.POST.get('city')

        all_paths = cities.find_all_paths(city)

        directed_paths, undirected_paths = direct_or_indirect(all_paths)

        context['directRoutes'] = directed_paths
        context['indirectRoutes'] = undirected_paths
        context['city'] = city

    context['city_list'] = cities.get_vertices()
    image = cities.draw_graph()
    context['image'] = image

    return render(request, 'second_challenge_template/second_challenge_form.html', context)

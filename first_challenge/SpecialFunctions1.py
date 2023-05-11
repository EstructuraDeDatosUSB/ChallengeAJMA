from .Graph_ADT import *

def loadGraph(graph):
    """
    Carga el grafo con las ciudades y sus distancias.
    
    Attributes:
    graph (Graph): El grafo al cual se le agregaran los vertices y aristas.
    """
    graph.addEdge('San Francisco', 'Los Angeles', 349)
    graph.addEdge('San Francisco', 'Denver', 957)
    graph.addEdge('San Francisco', 'Chicago', 1855)
    graph.addEdge('San Francisco', 'New York', 2534)
    graph.addEdge('Los Angeles', 'Denver', 834)
    graph.addEdge('Los Angeles', 'New York', 2451)
    graph.addEdge('Denver', 'Chicago', 908)
    graph.addEdge('Chicago', 'New York', 722)
    graph.addEdge('Chicago', 'Boston', 860)
    graph.addEdge('Chicago', 'Atlanta', 606)
    graph.addEdge('Atlanta', 'New York', 888)
    graph.addEdge('New York', 'Boston', 191)
    graph.addEdge('Atlanta', 'Miami', 595)
    graph.addEdge('Miami', 'New York', 1090)
    
def menu():
    """
    Muestra las opciones del menú y solicita al usuario que ingrese una opción.

    Returns:
    int: Opción elegida por el usuario.
    """
    print("=================================================")
    print("> [1] - Print graph.\n> [2] - Get shortest route.\n> [0] - Exit.")
    print("=================================================\n")
    opcion = int(input("Insert an option: "))
    return opcion 
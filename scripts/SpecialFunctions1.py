def loadGraph(graph):
    """
    Carga el grafo con las ciudades y sus distancias.
    
    Attributes:
    graph (Graph): El grafo al cual se le agregaran los vertices y aristas.
    """
    graph.add_vertex('San Francisco')
    graph.add_vertex('Los Angeles')
    graph.add_vertex('Denver')
    graph.add_vertex('Chicago')
    graph.add_vertex('New York')
    graph.add_vertex('Boston')
    graph.add_vertex('Atlanta')
    graph.add_vertex('Miami')

    graph.add_edge('San Francisco', 'Los Angeles', 349)
    graph.add_edge('San Francisco', 'Denver', 957)
    graph.add_edge('San Francisco', 'Chicago', 1855)
    graph.add_edge('San Francisco', 'New York', 2534)
    graph.add_edge('Los Angeles', 'Denver', 834)
    graph.add_edge('Los Angeles', 'New York', 2451)
    graph.add_edge('Denver', 'Chicago', 908)
    graph.add_edge('Chicago', 'New York', 722)
    graph.add_edge('Chicago', 'Boston', 860)
    graph.add_edge('Chicago', 'Atlanta', 606)
    graph.add_edge('Atlanta', 'New York', 888)
    graph.add_edge('New York', 'Boston', 191)
    graph.add_edge('Atlanta', 'Miami', 595)
    graph.add_edge('Miami', 'New York', 1090)
    
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

def direct_or_indirect(all_path):
    # Inicializar la lista de rutas directas
    direct_paths = []
    # Inicializar la lista de rutas indirectas
    indirect_paths = []

    # Iterar sobre todas las rutas encontradas
    for path in all_path:
        # Si la ruta es directa, agregarla a la lista de rutas directas
        if len(path) == 3:
            direct_paths.append(path)
        # Si la ruta es indirecta, agregarla a la lista de rutas indirectas
        else:
            indirect_paths.append(path)

    return direct_paths, indirect_paths

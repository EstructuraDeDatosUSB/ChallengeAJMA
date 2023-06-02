from io import BytesIO
import base64

import heapq

import networkx as nx

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')


# Para crear un TDA de grafos simples, es necesario primero saber de que esta compuesto un grafo simple
# Un grafo simple esta compuesto por un conjunto de vertices y un conjunto de aristas
# Por ende para modelar el TDA es necesario entenderlo como una clase que contenga una lista de adyacencia
# Con lista de adyasencia me refiero a una lista de listas, donde cada lista interna representa un vertice

# TDA de Grafos Simples

class Graph:
    """
    Esta clase representa la estructura de un grafo simple.

    Attributes:
        adjacent_list (dict): Un diccionario que contiene como llaves los vertices del grafo
            y como valores una lista de los vertices adyacentes a cada vertice.

    Methods:
        add_vertex(vertex): Agrega un nuevo vertice al grafo.
        add_edge(vertex1, vertex2): Agrega una arista entre dos vertices del grafo.
        get_neighbors(vertex): Retorna la lista de vertices adyacentes a un vertice dado.
        get_weight(src, dest): Retorna el peso de la arista entre dos vertices dados.
        bfs(start): Realiza un recorrido BFS del grafo.
        bfs_shortest_path(start, end): Retorna el camino mas corto entre dos vertices dados utilizando BFS.
        dfs(start, end, avoid): Realiza un recorrido DFS del grafo.
        dfs_shortest_path(start, end): Retorna el camino mas corto entre dos vertices dados utilizando DFS.
        dijkstra(start, end): Retorna el camino mas corto entre dos vertices dados utilizando Dijkstra.
        find_all_paths(start): Encuentra todas las rutas desde un nodo de inicio hasta los demás nodos.
        find_paths(start, end, path=[], weight=0): Encuentra todas las rutas desde un nodo de inicio
        hasta un nodo final.
        visualize(): Visualiza el grafo utilizando la libreria networkx.
        draw_graph(): Dibuja el grafo utilizando la libreria NetworkX con un diseño circular.
        __str__(): Retorna una representacion en string del grafo.
    """

    def __init__(self, directed=False, weighted=False):
        """
        Inicializa un grafo simple.

        Args:
        directed (bool): Indica si el grafo es dirigido o no.
        weighted (bool): Indica si el grafo es ponderado o no.
        """
        self.adjacent_list = {}
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, vertex):
        """
        Agrega un vertice al grafo.

        Args:
        vertex (int or str): El vertice a agregar.
        """
        if vertex not in self.adjacent_list:
            self.adjacent_list[vertex] = []

    def add_edge(self, src, dest, weight=None):
        """
        Agrega una arista entre dos vertices del grafo.

        - Si es dirigido, entonces se agrega un vertice a la lista de adyacencia del otro vertice,
        pero el otro vertice no se agrega a la lista de adyacencia del vertice actual.
        - Si es no dirigido, entonces se agrega un vertice a la lista de adyacencia del otro vertice,
        y el otro vertice tambien se agrega a la lista de adyacencia del vertice actual.

        - Si es ponderado, entonces se agrega el peso de la arista entre los dos vertices.

        Args:
        challengeAGMA (any): El vertice de origen.
        dest (any): El vertice de destino.
        weight (int or None): El peso de la arista. Si el grafo es ponderado, este argumento es obligatorio.

        Raises:
        ValueError: Si el grafo es ponderado y no se proporciona un peso para la arista.

        """
        if src not in self.adjacent_list:
            self.add_vertex(src)
        if dest not in self.adjacent_list:
            self.add_vertex(dest)

        if self.weighted and weight is None:
            raise ValueError(
                "Este grafo es ponderado, se debe proporcionar un peso para la arista.")
        elif not self.weighted:
            weight = None

        self.adjacent_list[src].append((dest, weight))

        if not self.directed:
            self.adjacent_list[dest].append((src, weight))

    def get_vertices(self):
        """
        Retorna la lista de vertices del grafo.

        Returns:
        list: La lista de vertices del grafo.
        """
        return list(self.adjacent_list.keys())

    def get_neighbors(self, vertex):
        """
        Retorna la lista de vertices adyacentes a un vertice dado.

        Args:
        vertex (any): El vertice del que se quieren obtener los vertices adyacentes.

        Returns:
        list: La lista de vertices adyacentes al vertice dado.
        """
        return self.adjacent_list[vertex]

    def get_weight(self, src, dest):
        """
        Retorna el peso de la arista entre dos vertices dados.

        Args:
        challengeAGMA (any): El vertice de origen.
        dest (any): El vertice de destino.

        Returns:
        int: El peso de la arista entre los dos vertices dados.
        """
        for neighbor, weight in self.adjacent_list[src]:
            if neighbor == dest:
                return weight

    # =================== BFS (Breadth First Search) ===================

    def bfs(self, start):
        """
        Realiza un recorrido BFS (Breadth First Search / Busqueda en Anchura) del grafo.

        Args:
        start (any): El vertice de inicio del recorrido.

        Returns:
        list: La lista de vertices en el orden en el que fueron visitados.
        """
        visited = []
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                for neighbor, weight in self.adjacent_list[vertex]:
                    queue.append(neighbor)
        return visited

    def bfs_shortest_path(self, start, end):
        """
        Retorna el camino mas corto entre dos vertices dados,
        utilizando un recorrido BFS (Breadth First Search / Busqueda en Anchura)

        Args:
        start (any): El vertice de inicio del recorrido.
        end (any): El vertice de fin del recorrido.

        Returns:
        list: La lista de vertices en el orden en el que fueron visitados.
        """
        visited = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            vertex = path[-1]
            if vertex not in visited:
                visited.append(vertex)
                for neighbor, weight in self.adjacent_list[vertex]:
                    current_path = list(path)
                    current_path.append(neighbor)
                    queue.append(current_path)
                    if neighbor == end:
                        return current_path

    # =====================================================================

    # =================== DFS (Depth First Search) ===================

    def dfs(self, start, end, avoid):
        """
        Realiza un recorrido DFS (Depth First Search / Busqueda en profundidad) del grafo.

        Args:
        start (any): El vertice de inicio del recorrido.
        end (any): El vertice de destino del recorrido.
        avoid (any): El vertice que se debe evitar en el camino.

        Returns:
        list: La lista de vertices en el orden en el que fueron visitados, sin incluir el vértice prohibido.
        """
        path = {start: None}
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex == end:
                break
            for neighbor, weight in self.adjacent_list[vertex]:
                if neighbor == avoid:
                    continue
                if neighbor not in path:
                    path[neighbor] = vertex
                    stack.append(neighbor)

        if end not in path:
            return []

        # Construir la ruta desde el inicio al destino
        current = end
        route = [current]
        while current != start:
            current = path[current]
            route.append(current)
        route.reverse()

        return route

    def dfs_shortest_path(self, start, end):
        """
        Retorna el camino mas corto entre dos vertices dados,
        utilizando el algoritmo de DFS (Depth First Search / Busqueda en profundidad)

        Args:
        start (any): El vertice de inicio del recorrido.
        end (any): El vertice de fin del recorrido.

        Returns:
        list: La lista de vertices en el orden en el que fueron visitados.
        """
        visited = []
        stack = [[start]]
        while stack:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                visited.append(vertex)
                for neighbor, weight in self.adjacent_list[vertex]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
                    if neighbor == end:
                        return new_path

    # =====================================================================

    # =================== Dijkstra ===================

    def dijkstra(self, start, end):
        distances = {}
        previous = {}
        queue = []
        path = []

        for vertex in self.adjacent_list:
            if vertex == start:
                distances[vertex] = 0
                heapq.heappush(queue, [0, vertex])
            else:
                distances[vertex] = float("inf")
                heapq.heappush(queue, [float("inf"), vertex])
            previous[vertex] = None

        while queue:
            current = heapq.heappop(queue)[1]
            if current == end:
                while previous[current]:
                    path.append(current)
                    current = previous[current]
                break
            if current in self.adjacent_list:
                for neighbor, weight in self.adjacent_list[current]:
                    alternative = distances[current] + weight
                    if alternative < distances[neighbor]:
                        distances[neighbor] = alternative
                        previous[neighbor] = current
                        for i in range(len(queue)):
                            if queue[i][1] == neighbor:
                                queue[i][0] = alternative
                                break
                        heapq.heapify(queue)
        result = path[::-1]
        result.insert(0, start)

        # Create a new graph with only the shortest path
        shortest_path_graph = Graph(directed=self.directed, weighted=self.weighted)
        for vertex in result:
            shortest_path_graph.add_vertex(vertex)
        for i in range(len(result) - 1):
            src = result[i]
            dest = result[i + 1]
            weight = self.get_weight(src, dest)
            shortest_path_graph.add_edge(src, dest, weight)

        # Generate the visualization image for the shortest path graph
        image_base64 = shortest_path_graph.draw_graph()

        # Distance:
        dist = 0
        for i in range(len(result) - 1):
            src = result[i]
            dest = result[i + 1]
            weight = self.get_weight(src, dest)
            dist += weight

        return result, image_base64, dist

    # =====================================================================

    def find_all_paths(self, start):
        # Inicializar la lista de rutas
        all_paths = []

        # Iterar sobre todos los nodos en el grafo
        for node in self.adjacent_list:
            # Encontrar todas las rutas indirectas desde el nodo actual hasta los demás nodos
            if node != start:
                paths = self.find_paths(start, node)
                # Agregar las rutas encontradas a la lista de rutas
                all_paths.extend(paths)

        return all_paths

    def find_paths(self, start, end, path=None, weight=0):
        # Añadir el nodo actual al camino
        if path is None:
            path = []
        path = path + [start] if isinstance(start, list) else path + [start]

        # Si el nodo actual es igual al nodo final, hemos encontrado una ruta
        if start == end:
            return [path + weight]

        # Si el nodo actual no está en el grafo, no hay ruta posible
        if start not in self.adjacent_list:
            return []

        # Inicializar la lista de rutas
        paths = []

        # Recorrer todas las conexiones desde el nodo actual
        for node, edge_weight in self.adjacent_list[start]:
            # Evitar ciclos
            if node not in path:
                # Encontrar todas las rutas indirectas desde el nodo adyacente hasta el nodo final
                new_paths = self.find_paths(node, end, path, weight + edge_weight)
                # Agregar las rutas encontradas a la lista de rutas
                paths.extend(new_paths)

        return paths

    def visualize(self):
        """
        Visualiza el grafo utilizando la libreria networkx.
        """
        g_nx = nx.DiGraph()

        # Agregamos los nodos al grafo de NetworkX
        for node in self.get_vertices():
            g_nx.add_node(node)

        # Agregamos las aristas al grafo de NetworkX
        for node in self.get_vertices():
            neighbors = self.get_neighbors(node)
            for neighbor in neighbors:
                g_nx.add_edge(node, neighbor[0])

        # Visualizamos el grafo
        nx.draw(g_nx, with_labels=True)
        plt.show()

    def draw_graph(self):
        """
        Draw the graph using the NetworkX library with an improved layout.
        """
        graph = nx.DiGraph() if self.directed else nx.Graph()

        # Add vertices
        graph.add_nodes_from(self.get_vertices())

        # Add edges
        for vertex in self.adjacent_list:
            for neighbor, weight in self.adjacent_list[vertex]:
                graph.add_edge(vertex, neighbor, weight=weight)

        # Use spring layout for improved spacing
        pos = nx.spring_layout(graph)

        # Create a larger figure
        fig, ax = plt.subplots(figsize=(10, 10))

        # Draw nodes and edges with reduced opacity
        nx.draw_networkx_nodes(graph, pos, node_size=500, alpha=0.8)
        nx.draw_networkx_edges(graph, pos, alpha=0.5)

        # Add node labels
        labels = {v: v for v in graph.nodes()}
        nx.draw_networkx_labels(graph, pos, labels)

        # Add edge labels
        edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

        # Save the figure to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        plt.clf()

        # Encode the image as base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return image_base64

    def __str__(self):
        """
        Retorna una representacion en string del grafo.

        Returns:
        str: Una representacion en string del grafo.
        """
        result = ""
        for vertex in self.adjacent_list:
            result += f"[{vertex}] -----> "
            neighbors = []
            for neighbor, weight in self.adjacent_list[vertex]:
                if weight is not None:
                    neighbors.append(f"[{neighbor}] [{weight}]")
                else:
                    neighbors.append(f"[{neighbor}]")
            result += ", ".join(neighbors)
            result += "\n"
        return result


#   Grafo predefinido


cities = Graph(weighted=True)

cities.add_edge("San Jose", "Cartago", 25)
cities.add_edge("San Jose", "Heredia", 10)
cities.add_edge("Cartago", "Heredia", 15)
cities.add_edge("Cartago", "Turrialba", 40)
cities.add_edge("Heredia", "Alajuela", 30)
cities.add_edge("Heredia", "Guanacaste", 222)
cities.add_edge("Alajuela", "Guanacaste", 200)
cities.add_edge("Alajuela", "Puntarenas", 150)
cities.add_edge("Turrialba", "Limon", 100)
cities.add_edge("Turrialba", "Guanacaste", 300)
cities.add_edge("Limon", "Puntarenas", 300)
cities.add_edge("Limon", "Guanacaste", 350)

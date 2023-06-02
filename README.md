# ChallengeAJMA (Puertos - Grafos)
Este proyecto es parte de un conjunto de programas desarrollados para la empresa AJMA. El objetivo de este programa es modelar el sistema de transporte entre puertos de una empresa que se encarga de transportar materiales, mediante el uso de un TDA (Tipo de Dato Abstracto) de Grafos.

## Tabla de contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Créditos](#créditos)
- [Licencia](#licencia)

## Instalación

### 1. Abre una terminal:
Algunos comandos son:
- Windows: "Windows + R" para abrir el cuadro de diálogo Ejecutar, luego escribe "cmd" y presiona Enter.
- MacOS: "Command + Barra espaciadora", luego escribiendo "Terminal" y presiona Enter.
- Linux: "Ctrl + Alt + T"
### 2. Clona el repositorio a tu máquina local: 
- git clone https://github.com/tu_usuario/proyecto-transporte-puertos.git
### 3. Accede al directorio:
- cd ChallengeAJMA
### 4. Crear un entorno virtual (Opcional - Si deseas no llenar tu máquina local de librerías):
- pip install virtualenv
- mkdir venv
- cd venv

#### - En Windows:
- venv\Scripts\activate

#### - En macOS y Linux:
- source venv/bin/activate
  
### 5. Instala los requerimientos
- pip install -r requirements.txt

## Uso

### 1. Abre una terminal en el proyecto:
### 2. Inicia el servidor de desarrollo de Django:
- python manage.py runserver

## Características

### TDA Grafo:
#### - Estructura de Grafo:
El TDA Graph representa la estructura de un grafo simple. Un grafo simple está compuesto por un conjunto de vértices y un conjunto de aristas. En este TDA, se utiliza una lista de adyacencia para representar las relaciones entre los vértices. La lista de adyacencia es un diccionario en el que las claves son los vértices y los valores son listas de los vértices adyacentes a cada vértice.
#### - Inicialización: 
El TDA se inicializa utilizando el constructor __init__. Se pueden especificar dos parámetros opcionales: directed (booleano) indica si el grafo es dirigido o no, y weighted (booleano) indica si el grafo es ponderado o no.
#### - Agregar Vértices y Aristas: 
El TDA proporciona los métodos add_vertex y add_edge para agregar vértices y aristas al grafo, respectivamente. El método add_vertex agrega un nuevo vértice al grafo, mientras que el método add_edge agrega una arista entre dos vértices del grafo. Si el grafo es dirigido, la arista se agrega solo en un sentido, mientras que si el grafo es no dirigido, la arista se agrega en ambos sentidos.
#### - Recorridos del Grafo: 
El TDA proporciona varios métodos para realizar recorridos del grafo, como BFS (Breadth First Search) y DFS (Depth First Search). Estos métodos permiten recorrer los vértices del grafo en diferentes órdenes y encontrar caminos entre vértices.
#### - Algoritmo de Dijkstra: 
El TDA implementa el algoritmo de Dijkstra para encontrar el camino más corto entre dos vértices del grafo. Este algoritmo se utiliza cuando el grafo es ponderado y encuentra la ruta de menor peso entre dos vértices.
#### - Visualización del Grafo: 
El TDA proporciona métodos para visualizar el grafo utilizando la biblioteca NetworkX y Matplotlib. Se pueden generar representaciones gráficas del grafo y guardarlas en imágenes en formato PNG.
#### - Otras Funcionalidades: 
El TDA también incluye otros métodos, como obtener los vértices del grafo, obtener los vértices adyacentes a un vértice dado, obtener el peso de una arista entre dos vértices, encontrar todas las rutas desde un nodo de inicio hasta los demás nodos, entre otros.

### Aplicación:
#### - Agregar rutas:
La aplicación permite agregar puertos, donde si el puerto no existe es automáticamente creado.
#### - Buscar Ruta más Corta:
La apliación permite al usuario poder ver cual es la ruta más corta entre dos puertos utilizando el algoritmo de Dijkstra
#### - Mirar todas las conexiones de un puerto:
La aplicación le permite al usuario poder saber cuales son todas las conexiones directas e indirectas de un puerto.

## Créditos

Este proyecto fue desarrollado por los siguientes miembros de la organización EstructuraDeDatosUSB en Github:

- Gustavo Camargo
- Dillan Asprilla
- Mariana Cruz
- Juan Manuel Conde
- Jhon Mario Diaz
- Juan David Diaz

Agradecemos a todos los miembros de la organización por su contribución a este proyecto.

## Licencia

Este proyecto se encuentra bajo la siguiente licencia:

[![Licencia CC-BY-NC-ND 4.0](https://i.creativecommons.org/l/by-nc-nd/4.0/80x15.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/deed.es)

El contenido de este proyecto está protegido por la licencia Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internacional. Esto significa que puedes utilizar y compartir este proyecto con otros bajo las siguientes condiciones:

- **Atribución (Attribution):** Debes otorgar crédito adecuado, proporcionando un enlace a la licencia y mencionando a los autores originales.
- **No Comercial (NonCommercial):** No puedes utilizar este proyecto con fines comerciales.
- **No Derivados (NoDerivatives):** No puedes modificar, adaptar o crear obras derivadas a partir de este proyecto.

Para obtener más información sobre los términos y condiciones de esta licencia, puedes visitar el siguiente enlace: [Licencia CC-BY-NC-ND 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/deed.es).

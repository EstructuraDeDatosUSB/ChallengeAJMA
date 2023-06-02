from django.test import TestCase
import unittest
from scripts.Graph_ADT import Graph
from scripts.SpecialFunctions1 import *


class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(directed=True, weighted=True)
        self.graph.add_edge('A', 'B', 2)
        self.graph.add_edge('A', 'C', 4)
        self.graph.add_edge('B', 'C', 1)

    def test_get_weight(self):
        weight = self.graph.get_weight('A', 'B')
        self.assertEqual(weight, 2)

        weight = self.graph.get_weight('A', 'C')
        self.assertEqual(weight, 4)

        weight = self.graph.get_weight('B', 'C')
        self.assertEqual(weight, 1)

    def test_dijkstra(self):
        path, _, distance = self.graph.dijkstra('A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])
        self.assertEqual(distance, 3)

        path, _, distance = self.graph.dijkstra('A', 'A')
        self.assertEqual(path, ['A'])
        self.assertEqual(distance, 0)

        path, _, distance = self.graph.dijkstra('B', 'C')
        self.assertEqual(path, ['B', 'C'])
        self.assertEqual(distance, 1)

    def test_bfs_shortest_path(self):
        path = self.graph.bfs_shortest_path('A', 'C')
        self.assertEqual(path, ['A', 'C'])

        path = self.graph.bfs_shortest_path('A', 'A')
        self.assertEqual(path, None)

        path = self.graph.bfs_shortest_path('B', 'C')
        self.assertEqual(path, ['B', 'C'])

    def test_direct_or_indirect(self):
        # Create a graph
        graph = Graph(directed=True, weighted=True)
        graph.add_edge('A', 'B', 2)
        graph.add_edge('A', 'C', 4)
        graph.add_edge('B', 'C', 1)
        graph.add_edge('C', 'D', 3)
        graph.add_edge('D', 'E', 5)
        graph.add_edge('E', 'F', 2)

        # Find all paths from node 'A'
        all_paths = graph.find_all_paths('A')

        # Call direct_or_indirect function
        direct_paths, indirect_paths = direct_or_indirect(all_paths)

        # Verify the direct paths
        self.assertEqual(direct_paths, [['A', 'B', 2], ['A', 'C', 4]])

        # Verify the indirect paths
        self.assertEqual(indirect_paths, [['A', 'B', 'C', 3], ['A', 'B', 'C', 'D', 6], ['A', 'C', 'D', 7],
                                          ['A', 'B', 'C', 'D', 'E', 11], ['A', 'C', 'D', 'E', 12],
                                          ['A', 'B', 'C', 'D', 'E', 'F', 13], ['A', 'C', 'D', 'E', 'F', 14]])


if __name__ == '__main__':
    unittest.main()

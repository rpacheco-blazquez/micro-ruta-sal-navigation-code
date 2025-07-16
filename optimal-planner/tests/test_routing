import unittest
from core.waypoint import Waypoint
from core.graph import build_graph
from core.routing import find_shortest_path

class TestRouting(unittest.TestCase):
    def setUp(self):
        self.waypoints = [
            Waypoint(38.9089, 1.4321, "Ibiza"),
            Waypoint(39.0, 2.0, "WP1"),
            Waypoint(39.5, 2.5, "WP2"),
            Waypoint(41.3851, 2.1734, "Barcelona")
        ]
        self.graph = build_graph(self.waypoints)

    def test_shortest_path(self):
        path = find_shortest_path(self.graph, 0, 3)
        self.assertIsInstance(path, list)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 3)

if __name__ == '__main__':
    unittest.main()

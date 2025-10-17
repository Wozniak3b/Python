import unittest
from zad3b import Tree, TreeNode

class TestTreeMinimal(unittest.TestCase):
    def test_add_child_returns_node(self):
        t = Tree("R")
        child = t.root.add_child("L", "x")
        self.assertIsInstance(child, TreeNode)
        self.assertEqual(child.value, "L")

    def test_str_has_nodes_and_edges(self):
        t = Tree("R")
        t.root.add_child("L", "x")
        s = str(t).replace(" ", "")
        self.assertIn("'R'", s)
        self.assertIn("['x']→'L'", s)

if __name__ == "__main__":
    unittest.main(verbosity=2)

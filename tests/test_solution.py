from unittest import TestCase
from bst import Node


class TestSolution(TestCase):
    def test_bst_second_largest(self):
        try:
            from build import Solution
        except ImportError:
            self.assertFalse("no class found")

        bst = Solution(None)
        self.assertRaises(TypeError, bst.find_second_largest)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node15 = bst.insert(15)
        node3 = bst.insert(3)
        node8 = bst.insert(8)
        node12 = bst.insert(12)
        node20 = bst.insert(20)
        node2 = bst.insert(2)
        node4 = bst.insert(4)
        node30 = bst.insert(30)
        self.assertEqual(bst.find_second_largest(), node20)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node3 = bst.insert(3)
        node7 = bst.insert(7)
        self.assertEqual(bst.find_second_largest(), node7)
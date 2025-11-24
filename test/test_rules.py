import unittest
from src.decision import decide_structure, DataStructure
from src.questions import Answers


class DecisionRulesTest(unittest.TestCase):

    def test_array_when_random_access(self):
        a = Answers(
            wants_random_access=True,
            needs_lifo=False,
            needs_fifo=False,
            many_middle_insertions=False,
            needs_ordering=False,
            needs_priority=False,
            has_graph_relationships=False,
        )
        self.assertEqual(decide_structure(a), DataStructure.ARRAY)

    def test_stack_when_lifo(self):
        a = Answers(
            wants_random_access=False,
            needs_lifo=True,
            needs_fifo=False,
            many_middle_insertions=False,
            needs_ordering=False,
            needs_priority=False,
            has_graph_relationships=False,
        )
        self.assertEqual(decide_structure(a), DataStructure.STACK)

    def test_queue_when_fifo(self):
        a = Answers(
            wants_random_access=False,
            needs_lifo=False,
            needs_fifo=True,
            many_middle_insertions=False,
            needs_ordering=False,
            needs_priority=False,
            has_graph_relationships=False,
        )
        self.assertEqual(decide_structure(a), DataStructure.QUEUE)

    def test_linked_list_when_many_insertions(self):
        a = Answers(
            wants_random_access=False,
            needs_lifo=False,
            needs_fifo=False,
            many_middle_insertions=True,
            needs_ordering=False,
            needs_priority=False,
            has_graph_relationships=False,
        )
        self.assertEqual(decide_structure(a), DataStructure.LINKED_LIST)

    def test_bst_when_ordering_needed(self):
        a = Answers(
            wants_random_access=False,
            needs_lifo=False,
            needs_fifo=False,
            many_middle_insertions=False,
            needs_ordering=True,
            needs_priority=False,
            has_graph_relationships=False,
        )
        self.assertEqual(decide_structure(a), DataStructure.BST)

    def test_heap_when_priority(self):
        a = Answers(
            wants_random_access=False,
            needs_lifo=False,
            needs_fifo=False,
            many_middle_insertions=False,
            needs_ordering=False,
            needs_priority=True,
            has_graph_relationships=False,
        )
        self.assertEqual(decide_structure(a), DataStructure.HEAP)

    def test_graph_when_relationships(self):
        a = Answers(
            wants_random_access=False,
            needs_lifo=False,
            needs_fifo=False,
            many_middle_insertions=False,
            needs_ordering=False,
            needs_priority=False,
            has_graph_relationships=True,
        )
        self.assertEqual(decide_structure(a), DataStructure.GRAPH)

    # -----------------------------
    # END-TO-END TEST (from docs/example)
    # -----------------------------
    def test_end_to_end_example(self):
        """Simulates the example path described in /docs/example/README.md"""
        a = Answers(
            wants_random_access=False,
            needs_lifo=False,
            needs_fifo=False,
            many_middle_insertions=False,
            needs_ordering=True,
            needs_priority=False,
            has_graph_relationships=False,
        )
        self.assertEqual(decide_structure(a), DataStructure.BST)


if __name__ == "__main__":
    unittest.main()

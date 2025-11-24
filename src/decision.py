from enum import Enum, auto
from .questions import Answers


class DataStructure(Enum):
    ARRAY = auto()
    LINKED_LIST = auto()
    STACK = auto()
    QUEUE = auto()
    BST = auto()
    HEAP = auto()
    GRAPH = auto()


def ds_name(ds: DataStructure) -> str:
    return {
        DataStructure.ARRAY: "Array",
        DataStructure.LINKED_LIST: "Linked List",
        DataStructure.STACK: "Stack",
        DataStructure.QUEUE: "Queue",
        DataStructure.BST: "Binary Search Tree (BST)",
        DataStructure.HEAP: "Heap / Priority Queue",
        DataStructure.GRAPH: "Graph",
    }[ds]


def decide_structure(ans: Answers) -> DataStructure:
    if ans.wants_random_access:
        return DataStructure.ARRAY

    if ans.needs_lifo:
        return DataStructure.STACK

    if ans.needs_fifo:
        return DataStructure.QUEUE

    if ans.many_middle_insertions:
        return DataStructure.LINKED_LIST

    if ans.needs_ordering:
        return DataStructure.BST

    if ans.needs_priority:
        return DataStructure.HEAP

    if ans.has_graph_relationships:
        return DataStructure.GRAPH

    return DataStructure.ARRAY
